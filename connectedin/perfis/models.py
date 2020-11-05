from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    #email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self', related_name='contatos')
    
    usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)
    
    @property
    def email(self):
        return self.usuario.email
    
    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()


class Convite(models.Model):
    solicitante = models.ForeignKey(
        Perfil, related_name='convites_feitos', on_delete=models.CASCADE)
    convidado = models.ForeignKey(
        Perfil, related_name='convites_recebidos', on_delete=models.CASCADE)

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)       
        self.delete()
        
class Postagem(models.Model):
    texto = models.CharField(max_length=200)
    data = models.TimeField(blank=True, auto_now=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    class Meta:
        ordering = [F('data').desc(nulls_last=True)]
