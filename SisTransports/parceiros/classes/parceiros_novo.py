from parceiros.models.parceiros import Parceiros as MdlParceiros
from contatos.classes.contato import Contato
from comercial.classes.tabelaFrete import TabelaFrete
from Classes.utils import dprint

class Parceiros():
    @classmethod
    def createParceiro(cls, dados):
        try:
            cls.parceiro = MdlParceiros()
            cls.createOrUpdate(dados)
            cls.parceiro.save()
            return cls
        except Exception as e:
            print(f"Erro ao criar parceiro: {e}")
            return None

    @classmethod
    def createOrUpdate(cls, dados):
        cls.parceiro.cnpj_cpf = dados.get('cnpj')
        cls.parceiro.raz_soc = dados.get('razao')
        cls.parceiro.nome_fantasia = dados.get('fantasia')
        cls.parceiro.insc_est = dados.get('inscr')
        cls.parceiro.observacao = dados.get('obs'," ")
        cls.parceiro.endereco_fk = dados.get('endereco_fk')

    @classmethod
    def readParceiroClassMethod(cls, cnpj):
        try:
            if MdlParceiros.objects.filter(cnpj_cpf=cnpj).exists():
                cls.parceiro = MdlParceiros.objects.filter(cnpj_cpf=cnpj).get()
                contatos = Contato()
                tabelas = TabelaFrete()
                cls.parceiro.tabelasFrete = tabelas.get_tabelas_por_parceiro(cls.parceiro)
                cls.parceiro.listaContatos = contatos.readContatos(cls.parceiro.id)
                return 200
            else:
                return 404
        except Exception as e:
            print(f"Erro ao ler parceiro: {e}")
            return 500

    @classmethod
    def readParceiro(cls, cnpj):
        try:
            if MdlParceiros.objects.filter(cnpj_cpf=cnpj).exists():
                cls.parceiro = MdlParceiros.objects.filter(cnpj_cpf=cnpj).get()
                contatos = Contato()
                tabelas = TabelaFrete()
                cls.parceiro.tabelasFrete = tabelas.get_tabelas_por_parceiro(cls.parceiro)
                cls.parceiro.listaContatos = contatos.readContatos(cls.parceiro.id)
                return cls.parceiro,200
            else:
                return None
        except Exception as e:
            print(f"Erro ao ler parceiro: {e}")
            return 500

    @classmethod
    def readParceiroId(cls, idParceiro):
        if MdlParceiros.objects.filter(id=idParceiro).exists():
            cls.parceiro = MdlParceiros.objects.filter(id=idParceiro).get()
            return cls.parceiro
        else:
            return False

    @classmethod
    def updateParceiro(cls, idParceiro, dados):
        if MdlParceiros.objects.filter(id=idParceiro).exists():
            try:
                cls.parceiro = MdlParceiros.objects.filter(id=idParceiro).get()
                cls.createOrUpdate(dados)
                cls.parceiro.save()
                return 200
            except Exception as e:
                print(f"Erro ao atualizar parceiro: {e}")
                return 400
        else:
            return 404

    @classmethod
    def deleteParceiro(cls, idParceiro):
        if MdlParceiros.objects.filter(id=idParceiro).exists():
            try:
                cls.parceiro = MdlParceiros.objects.filter(id=idParceiro).get()
                cls.parceiro.delete()
                return 200
            except Exception as e:
                print(f"Erro ao deletar parceiro: {e}")
                return 400
        else:
            return 404
