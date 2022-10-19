from django.urls import path

from . import views

urlpatterns = [
    path('<int:receita_id>', views.receita, name='receita'),
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar')
]
