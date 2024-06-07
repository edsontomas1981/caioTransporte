from django.db import models
from django.contrib.auth.models import User
from operacional.models.dtc import Dtc
from django.conf import settings
from datetime import datetime
from parceiros.models.parceiros import Parceiros

class Nota_fiscal_Caio_Transportes(models.Model):
    chave_acesso = models.CharField(max_length=50)
    num_nf = models.CharField(max_length=20)
    remetente_fk=models.ForeignKey(Parceiros, on_delete=models.CASCADE,related_name='remetente_nfe', null=True)
    destinatario_fk=models.ForeignKey(Parceiros, on_delete=models.CASCADE, related_name='destinatario_nfe', null=True)
    data_emissao = models.DateField()
    natureza = models.CharField(max_length=100)
    volume = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    valor_nf = models.CharField(max_length=20)
    
    # Informações de usuário e data/hora
    usuario_cadastro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='notas_fiscais_cadastradas_caio')
    usuario_ultima_atualizacao = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='notas_fiscais_atualizadas_caio')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    def to_dict(self):
        nota_fiscal = {
            'id': self.id,
            'chave_acesso': self.chave_acesso,
            'num_nf': self.num_nf,
            'data_emissao': self.data_emissao.strftime('%Y-%m-%d') if self.data_emissao else None,
            'natureza': self.natureza,
            'volume': self.volume,
            'peso': self.peso,
            'valor_nf': self.valor_nf,
            'usuario_cadastro': self.usuario_cadastro.username if self.usuario_cadastro else None,
            'data_cadastro': self.data_cadastro.strftime('%Y-%m-%d %H:%M:%S') if self.data_cadastro else None,
            'usuario_ultima_atualizacao': self.usuario_ultima_atualizacao.username if self.usuario_ultima_atualizacao else None,
            'data_ultima_atualizacao': self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S') if self.data_ultima_atualizacao else None,
        }
        
        return nota_fiscal