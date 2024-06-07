from enderecos.models.endereco import Enderecos as MdlEnderecos

class Enderecos:
    @classmethod
    def createOrUpdate(cls, dados):
        try:
            endereco = MdlEnderecos(
                cep=dados['cep'],
                logradouro=dados['logradouro'],
                numero=dados['numero'],
                complemento=dados['complemento'],
                bairro=dados['bairro'],
                cidade=dados['cidade'],
                uf=dados['estado']
            )
            endereco.save()
            return 200
        except Exception as e:
            print(f"Erro ao criar ou atualizar endereço: {e}")
            return 400
            
    @classmethod
    def createEndereco(cls, dados):
        try:
            cls.createOrUpdate(dados)
            return 200
        except Exception as e:
            print(f"Erro ao criar endereço: {e}")
            return 400
            
    @classmethod
    def readEndereco(cls, idEndereco):
        try:
            endereco = MdlEnderecos.objects.get(id=idEndereco)
            return endereco
        except MdlEnderecos.DoesNotExist:
            return False        
    
    @classmethod
    def updateEndereco(cls, idEndereco, dados):
        try:
            endereco = MdlEnderecos.objects.get(id=idEndereco)
            cls.createOrUpdate(dados)
            return 200
        except MdlEnderecos.DoesNotExist:
            return 404
        except Exception as e:
            print(f"Erro ao atualizar endereço: {e}")
            return 400 
        
    @classmethod
    def deleteEndereco(cls, idEndereco):
        try:
            endereco = MdlEnderecos.objects.get(id=idEndereco)
            endereco.delete()
            return 200
        except MdlEnderecos.DoesNotExist:
            return 404
        except Exception as e:
            print(f"Erro ao deletar endereço: {e}")
            return 400  
