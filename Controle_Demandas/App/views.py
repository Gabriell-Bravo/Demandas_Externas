from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Appform
from .models import AppModel


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Login')
        password = request.POST.get('Senha')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Exibir_Cadastro_demandas')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')


def Exibir_Cadastro_Demandas(request):
    if request.method == 'POST':
        form = Appform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Exibir_Painel')
    else:
        form = Appform()
    return render(request, 'index.html', {'form': form})


def Exibir_Painel(request):

    demandas = AppModel.objects.all()
    return render(request, 'Painel.html', {'demandas': demandas})
