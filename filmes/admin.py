from django.contrib import admin

# Register your models here.
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'ano_lancamento', 'duracao')
    search_fields = ('nome', 'descricao')