from django.db import models

# Create your models here.

class Licitacao(models.Model):
    objeto = models.CharField(max_length=4000)
    modalidade = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    comprador = models.CharField(max_length=255)
    descrição = models.CharField(max_length=4000)
    unidade = models.FloatField()
    quantidade = models.IntegerField()
    valor = models.FloatField()
