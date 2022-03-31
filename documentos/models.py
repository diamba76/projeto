from django.db import models

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=200, blank=True)
    documento = models.FileField(upload_to='documents/')

