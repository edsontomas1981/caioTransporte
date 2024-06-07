from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
import os
import xml.etree.ElementTree as ET
from parceiros.classes.parceiros_novo import Parceiros
from enderecos.classes.endereco_novo import Enderecos

@csrf_exempt
@require_http_methods(["POST", "GET"])
def upload_xml(request):
    if request.FILES.getlist('xml_files'):
        xml_files = request.FILES.getlist('xml_files')
        fs = FileSystemStorage()
        errors = []
        results = []

        for xml_file in xml_files:
            filename = fs.save(xml_file.name, xml_file)
            uploaded_file_path = fs.path(filename)

            try:
                tree = ET.parse(uploaded_file_path)
                root = tree.getroot()

                # Ajuste o namespace conforme necessário
                ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
                infNFe = root.find('.//ns:infNFe', ns)
                
                # Se infNFe não for encontrado, adicionar um erro e continuar
                if infNFe is None:
                    errors.append(f'Elemento infNFe não encontrado no arquivo {xml_file.name}')
                    continue
                
                ide = infNFe.find('ns:ide', ns)
                emit = infNFe.find('ns:emit', ns)
                dest = infNFe.find('ns:dest', ns)
                
                data = {
                    'filename': xml_file.name,
                    'ide': {
                        'cUF': get_element_text(ide, 'ns:cUF', ns),
                        'cNF': get_element_text(ide, 'ns:cNF', ns),
                        'natOp': get_element_text(ide, 'ns:natOp', ns),
                        'mod': get_element_text(ide, 'ns:mod', ns),
                        'serie': get_element_text(ide, 'ns:serie', ns),
                        'nNF': get_element_text(ide, 'ns:nNF', ns),
                        'dhEmi': get_element_text(ide, 'ns:dhEmi', ns),
                        'dhSaiEnt': get_element_text(ide, 'ns:dhSaiEnt', ns),
                        'tpNF': get_element_text(ide, 'ns:tpNF', ns),
                        'idDest': get_element_text(ide, 'ns:idDest', ns),
                        'cMunFG': get_element_text(ide, 'ns:cMunFG', ns),
                        'tpImp': get_element_text(ide, 'ns:tpImp', ns),
                        'tpEmis': get_element_text(ide, 'ns:tpEmis', ns),
                        'cDV': get_element_text(ide, 'ns:cDV', ns),
                        'tpAmb': get_element_text(ide, 'ns:tpAmb', ns),
                        'finNFe': get_element_text(ide, 'ns:finNFe', ns),
                        'indFinal': get_element_text(ide, 'ns:indFinal', ns),
                        'indPres': get_element_text(ide, 'ns:indPres', ns),
                        'procEmi': get_element_text(ide, 'ns:procEmi', ns),
                        'verProc': get_element_text(ide, 'ns:verProc', ns)
                    },
                    'emit': {
                        'CNPJ': get_element_text(emit, 'ns:CNPJ', ns),
                        'xNome': get_element_text(emit, 'ns:xNome', ns),
                        'xFant': get_element_text(emit, 'ns:xFant', ns),
                        'xLgr': get_element_text(emit, 'ns:enderEmit/ns:xLgr', ns),
                        'nro': get_element_text(emit, 'ns:enderEmit/ns:nro', ns),
                        'xBairro': get_element_text(emit, 'ns:enderEmit/ns:xBairro', ns),
                        'cMun': get_element_text(emit, 'ns:enderEmit/ns:cMun', ns),
                        'xMun': get_element_text(emit, 'ns:enderEmit/ns:xMun', ns),
                        'UF': get_element_text(emit, 'ns:enderEmit/ns:UF', ns),
                        'CEP': get_element_text(emit, 'ns:enderEmit/ns:CEP', ns),
                        'cPais': get_element_text(emit, 'ns:enderEmit/ns:cPais', ns),
                        'xPais': get_element_text(emit, 'ns:enderEmit/ns:xPais', ns),
                        'fone': get_element_text(emit, 'ns:enderEmit/ns:fone', ns),
                        'IE': get_element_text(emit, 'ns:IE', ns),
                        'CRT': get_element_text(emit, 'ns:CRT', ns)
                    },
                    'dest': {
                        'CNPJ': get_element_text(dest, 'ns:CNPJ', ns),
                        'xNome': get_element_text(dest, 'ns:xNome', ns),
                        'xLgr': get_element_text(dest, 'ns:enderDest/ns:xLgr', ns),
                        'nro': get_element_text(dest, 'ns:enderDest/ns:nro', ns),
                        'xBairro': get_element_text(dest, 'ns:enderDest/ns:xBairro', ns),
                        'cMun': get_element_text(dest, 'ns:enderDest/ns:cMun', ns),
                        'xMun': get_element_text(dest, 'ns:enderDest/ns:xMun', ns),
                        'UF': get_element_text(dest, 'ns:enderDest/ns:UF', ns),
                        'CEP': get_element_text(dest, 'ns:enderDest/ns:CEP', ns),
                        'cPais': get_element_text(dest, 'ns:enderDest/ns:cPais', ns),
                        'xPais': get_element_text(dest, 'ns:enderDest/ns:xPais', ns),
                        'fone': get_element_text(dest, 'ns:enderDest/ns:fone', ns),
                        'indIEDest': get_element_text(dest, 'ns:indIEDest', ns),
                        'IE': get_element_text(dest, 'ns:IE', ns)
                    }
                }

                checa_parceiro_cadastrado(data.get("emit"))
                checa_parceiro_cadastrado(data.get("dest"))
                
                results.append(data)

            except ET.ParseError:
                errors.append(f'Erro ao parsear o arquivo {xml_file.name}')
            except AttributeError:
                errors.append(f'Elementos de CNPJ não encontrados no arquivo {xml_file.name}')

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        return JsonResponse({'message': 'Arquivos XML recebidos com sucesso.', 'data': results})

    return JsonResponse({'error': 'Nenhum arquivo XML encontrado.'}, status=400)


def checa_parceiro_cadastrado(dados_parceiro):
    dados_normalizados_para_cadastro = normaliza_dados_parceiro(dados_parceiro)
    endereco = normaliza_dados_endereco(dados_parceiro)

    if not Parceiros.readParceiro(dados_parceiro.get('CNPJ')):
        endereco = cadastra_endereco(endereco)
        dados_normalizados_para_cadastro['endereco_fk'] = endereco
        cadastra_parceiro(dados_normalizados_para_cadastro)
    else:
        print(Parceiros.readParceiro(dados_parceiro.get('CNPJ')))


def cadastra_parceiro(dados_parceiro):
    Parceiros.createParceiro(dados_parceiro)

def cadastra_endereco(dados_parceiro):
    return Enderecos.createEndereco(dados_parceiro)
    

def normaliza_dados_parceiro(dados_parceiro):
    return{'cnpj':dados_parceiro.get('CNPJ'),
           'razao':dados_parceiro.get('xNome'),
           'fantasia':dados_parceiro.get('xFant'," "),
           'inscr':dados_parceiro.get('IE','ISENTO'),
           }

def normaliza_dados_endereco(dados_parceiro):
    return{'cep':dados_parceiro.get('CEP'),
            'logradouro':dados_parceiro.get('xLgr'),
            'numero':dados_parceiro.get('nro'),
            'complemento':dados_parceiro.get('xLgr'),
            'bairro':dados_parceiro.get('xBairro'),
            'cidade':dados_parceiro.get('xMun'),
            'estado':dados_parceiro.get('UF')
            }

def get_element_text(parent_element, xpath, namespaces):
    element = parent_element.find(xpath, namespaces)
    if element is not None:
        return element.text
    else:
        return None
