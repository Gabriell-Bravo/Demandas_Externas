from django.db import models


class AppModel(models.Model):
    ESPECIE_CHOICES = [
        ('Auditoria', 'Auditoria'),
        ('Monitoramento', 'Monitoramento'),
        ('Solicitação', 'Solicitação'),
        ('Representação', 'Representação'),
        ('Outros: Especifica', 'Outros: Especifica'),

    ]
    DIRECIONAMENTO_CHOICES = [
        ('Administração, Receita e Tributação',
         'Administração, Receita e Tributação'),
        ('Agricultura, Abastecimento e Pesca',
         'Agricultura, Abastecimento e Pesca'),
        ('Comunicação Social', 'Comunicação Social'),
        ('Desenvolvimento Social', 'Desenvolvimento Social'),
        ('Direitos dos Animais', 'Direitos dos Animais'),
        ('Educação, Cultura, Inclusão, Ciência e Tecnologia',
         'Educação, Cultura, Inclusão, Ciência e Tecnologia'),
        ('Esporte, Lazer e Turismo', 'Esporte, Lazer e Turismo'),
        ('Finanças', 'Finanças'),
        ('Gabinete', 'Gabinete'),
        ('Gestão, Inovação e Tecnologia', 'Gestão, Inovação e Tecnologia'),
        ('Governança e Sustentabilidade', 'Governança e Sustentabilidade'),
        ('Infraestrutura', 'Infraestrutura'),
        ('Meio Ambiente', 'Meio Ambiente'),
        ('Mulher', 'Mulher'),
        ('Transporte e Serviços Públicos', 'Transporte e Serviços Públicos'),
        ('Obras Públicas', 'Obras Públicas'),
        ('Planejamento', 'Planejamento'),
        ('Relações Institucionais', 'Relações Institucionais'),
        ('Saúde', 'Saúde'),
        ('Segurança e Ordem Pública', 'Segurança e Ordem Pública'),
        ('Transparência e Integridade', 'Transparência e Integridade'),
        ('Urbanismo', 'Urbanismo'),
        # Adicione mais opções se quiser
    ]
    SIM_NAO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    Id_orgao = models.CharField(max_length=50)
    Numero_officio = models.CharField(max_length=50, null=True, blank=True)
    Numero_Processo = models.CharField(max_length=50, null=True, blank=True)
    Especie = models.CharField(
        max_length=50, choices=ESPECIE_CHOICES, null=True, blank=True)
    Objeto = models.TextField(null=True, blank=True)
    Direcionamento = models.CharField(
        max_length=100, choices=DIRECIONAMENTO_CHOICES, null=True, blank=True)
    Anexo = models.FileField(upload_to='anexos/', null=True, blank=True)
    Prazo_Resposta = models.CharField(
        max_length=3, choices=SIM_NAO_CHOICES, null=True, blank=True)
    Data_Prazo = models.DateField(null=True, blank=True)
    Monitoramento = models.CharField(
        max_length=3, choices=SIM_NAO_CHOICES, null=True, blank=True)
    Data_Monitoramento = models.DateField(null=True, blank=True)
    Indexacao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.Id_orgao} - {self.Numero_officio}"
