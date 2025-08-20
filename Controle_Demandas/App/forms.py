from django import forms
from .models import AppModel


class Appform(forms.ModelForm):
    class Meta:
        model = AppModel
        fields = [
            'Id_orgao',
            'Numero_officio',
            'Numero_Processo',
            'Especie',
            'Objeto',
            'Direcionamento',
            'Anexo',
            'Prazo_Resposta',
            'Data_Prazo',
            'Monitoramento',
            'Data_Monitoramento',
            'Indexacao'
        ]
        widgets = {
            'Id_orgao': forms.TextInput(attrs={'class': 'form-control'}),
            'Numero_officio': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Numero_Processo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Especie': forms.Select(attrs={'class': 'form-control'}),
            'Objeto': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Direcionamento': forms.Select(attrs={'class': 'form-control'}),
            'Anexo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Prazo_Resposta': forms.Select(attrs={'class': 'form-control'}),
            'Data_Prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Monitoramento': forms.Select(attrs={'class': 'form-control'}),
            'Data_Monitoramento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Indexacao': forms.TextInput(attrs={'class': 'form-control'}),
        }
