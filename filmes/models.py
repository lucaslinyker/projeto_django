from django.db import models

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# Create your models here.
class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    duracao = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.nome