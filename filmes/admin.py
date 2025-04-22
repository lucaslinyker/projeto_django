from django.contrib import admin
from .models import Filme, Genero

# Register your models here.
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'ano_lancamento', 'duracao')
    search_fields = ('nome', 'descricao')
admin.site.register(Filme, FilmeAdmin)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
admin.site.register(Genero, GeneroAdmin)