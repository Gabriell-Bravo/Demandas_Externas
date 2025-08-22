#!/bin/bash

# Instalar dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar diretórios necessários
mkdir -p staticfiles
mkdir -p media