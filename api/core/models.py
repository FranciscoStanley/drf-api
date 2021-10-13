from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=150)
    idade = models.IntegerField()

    def __str__(self):
        return self.nomes    