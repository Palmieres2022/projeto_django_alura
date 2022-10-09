from django.contrib import admin
from.models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_de_preparo') 
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)  #possibilita a pesquisa pelo nome da receita
    list_filter = ('categoria',) #adiciona filtro por categoria das receitas
    list_per_page = 4 #Cria a paginação do admin-django              


admin.site.register(Receita, ListandoReceitas)
