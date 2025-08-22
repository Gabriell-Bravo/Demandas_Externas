from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.login_view, name='exibir_login'),
    path('Cadastro_Demandas/', views.Exibir_Cadastro_Demandas, name='Exibir_Cadastro_demandas'),
    path('Painel/', views.Exibir_Painel, name='Exibir_Painel'),
]
