from django.db import models
# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    cpf = models.CharField(max_length=11)


class PessoaLogin(models.Model):
    Pessoa_link = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    login = models.CharField(max_length=200, unique=True)
    senha = models.CharField(max_length=200)
