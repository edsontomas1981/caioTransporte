from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Classes.utils import dprint,checkBox
from contatos.classes.contato import Contato 
from contatos.classes.tipoContatos import TipoContato
from parceiros.classes.parceiros import Parceiros



@login_required(login_url='/auth/entrar/')
def createContato(request):
    if request.method == 'GET':
        return JsonResponse({'status': 200}) 
    elif request.method == "POST" :
        parceiro=Parceiros()
        statusParceiro=parceiro.readParceiro(request.POST.get('cnpj_cpf'))
        
        tipoContato=TipoContato()
        statusContato=tipoContato.readTipo(request.POST.get('tipo_contato'))
        if statusParceiro==200 and statusContato==200:
            dados=standartData(dict(request.POST.items()))
            dados['tipo']=tipoContato.tipoContato
            dados['parceiro']=parceiro.parceiro

            contato=Contato()
            contato.createContato(dados)
            listaContatos=contato.readContatos(parceiro.parceiro.id)
            return JsonResponse({'status': 200,'listaContatos':listaContatos}) 
        else:
            return JsonResponse({'status': 200}) 


def standartData(response):
     
    envio=''
    
    if 'envio' in response:
        envio=checkBox(response['envio'])
    else:
        envio=False

    return{'cargo':response['cargo'],
            'nome':response['nome'],
            'descContato':response['contato'],
            'envio':envio
            }
