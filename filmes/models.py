from django.db import models

# Create your models here.
class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    duracao = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome