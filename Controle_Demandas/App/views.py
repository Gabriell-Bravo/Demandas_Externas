from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DemandaForm  # Assumindo que você tem um forms.py com DemandaForm

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

@login_required
def Exibir_Cadastro_Demandas(request):
    # Se você tiver um formulário, descomente as linhas abaixo
    # if request.method == 'POST':
    #     form = DemandaForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Exibir_Painel')
    # else:
    #     form = DemandaForm()
    # return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': None})

@login_required
def Exibir_Painel(request):
    # Dados de exemplo para demonstração
    demandas_exemplo = [
        {
            'Id_orgao': 'Secretaria de Educação',
            'Numero_officio': '123/2024',
            'Numero_Processo': 'PROC-001',
            'Especie': 'Solicitação',
            'Objeto': 'Sistema em modo de demonstração no Vercel',
            'Direcionamento': 'Departamento de TI',
            'Anexo': None,
            'Prazo_Resposta': '30 dias',
            'Data_Prazo': '2024-02-15',
            'Monitoramento': 'Em análise',
            'Data_Monitoramento': '2024-01-20',
            'Indexacao': 'Demonstração'
        }
    ]
    return render(request, 'Painel.html', {'demandas': demandas_exemplo})

def logout_view(request):
    logout(request)
    return redirect('exibir_login')