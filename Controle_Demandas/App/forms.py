from django import forms
from .models import AppModel

MONITORAMENTO_CHOICES = (
    ('Mensal', 'Mensal'),
    ('Trimestral', 'Trimestral'),
    ('Semestral', 'Semestral'),
    ('Anual', 'Anual'),
    ('Não monitorado', 'Não monitorado'),
)

class Appform(forms.ModelForm):
    Monitoramento = forms.ChoiceField(
        choices=MONITORAMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = AppModel
        fields = '__all__'
        widgets = {
            'Id_orgao': forms.TextInput(attrs={'class': 'form-control'}),
            'Numero_officio': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Numero_Processo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Especie': forms.Select(attrs={'class': 'form-control'}),
            'Objeto': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'OBSERVAÇÃO': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            # TAREFAS foi removido daqui
            'Direcionamento': forms.Select(attrs={'class': 'form-control'}),
            'Prazo_Resposta': forms.Select(attrs={'class': 'form-control'}),
            'Data_Prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Data_Monitoramento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Indexacao': forms.TextInput(attrs={'class': 'form-control'}),
        }