# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Appform
from .models import AppModel, Anexo, Tarefa 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

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
        form = Appform(request.POST, request.FILES)
        if form.is_valid():
            demanda = form.save()
            
            # --- CORREÇÃO: Lógica para salvar as tarefas ---
            tarefas_list = request.POST.getlist('tarefas[]')
            for tarefa_descricao in tarefas_list:
                if tarefa_descricao: # Garante que a descrição não está vazia
                    Tarefa.objects.create(
                        demanda=demanda,
                        descricao=tarefa_descricao
                    )
            
            # Handle multiple file uploads
            files = request.FILES.getlist('anexos') # 'anexos' is the name of your file input
            for f in files:
                Anexo.objects.create(demanda=demanda, arquivo=f, nome=f.name)
            
            return redirect('Exibir_Painel')
    else:
        form = Appform()
    return render(request, 'index.html', {'form': form})

def Exibir_Painel(request):
    # --- CORREÇÃO: Uso de prefetch_related para carregar tarefas eficientemente ---
    demandas = AppModel.objects.all().prefetch_related('tarefas')
    return render(request, 'Painel.html', {'demandas': demandas})

def editar_demanda(request, id):
    demanda = get_object_or_404(AppModel, id=id)
    if request.method == 'POST':
        form = Appform(request.POST, request.FILES, instance=demanda)
        if form.is_valid():
            form.save()
            
            # Handle new file uploads during edit
            files = request.FILES.getlist('anexos')
            for f in files:
                Anexo.objects.create(demanda=demanda, arquivo=f, nome=f.name)
                
            return redirect('Exibir_Painel')
    else:
        form = Appform(instance=demanda)
    
    # Pass existing annexes and tasks to the template for display
    anexos = demanda.anexos.all()
    tarefas = demanda.tarefas.all()
    return render(request, 'editar_demanda.html', {'form': form, 'demanda': demanda, 'anexos': anexos, 'tarefas': tarefas})

def excluir_demanda(request, id):
    demanda = get_object_or_404(AppModel, id=id)
    if request.method == 'POST':
        demanda.delete()
        return redirect('Exibir_Painel')
    return render(request, 'confirmar_exclusao.html', {'demanda': demanda})

@require_POST
def atualizar_status_tarefa(request, tarefa_id):
    """
    Atualiza o status de conclusão de uma tarefa.
    """
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        data = json.loads(request.body)
        tarefa.concluida = data.get('concluida', False)
        tarefa.save()
        return JsonResponse({'success': True})
    except Tarefa.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Tarefa não encontrada'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)