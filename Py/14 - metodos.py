"""
MÓDULOS NATIVOS DO PYTHON
Autor: Paulo Vinícius

Conteúdo:
- datetime
- random
- os
- sys
- math
- time
"""

# ======================================================
# 1. DATETIME
# ======================================================

import datetime

agora = datetime.datetime.now()

print("Data e hora atual:", agora)

print("Ano:", agora.year)
print("Mês:", agora.month)
print("Dia:", agora.day)

# criando data específica
data_especifica = datetime.datetime(2025, 2, 15)

print(f"Data criada: {data_especifica.strftime('%d/%m/%Y')}")

print()


# ======================================================
# 2. RANDOM
# ======================================================

import random

numero_aleatorio = random.randint(1, 1000)
print(f"Número aleatório entre 1 e 10: {numero_aleatorio}")

lista = ["Amarelo", "Verde", "Vermelho", "Preto", "Branco", "Roxo"]

print("Escolha aleatória:", random.choice(lista))

random.shuffle(lista)

print("Lista embaralhada:", lista)

print()


# ======================================================
# 3. OS (SISTEMA OPERACIONAL)
# ======================================================

import os

print("Diretório atual:", os.getcwd())

print("Arquivos da pasta:", os.listdir())

# criar pasta (se não existir)
""""if not os.path.exists("nova_pasta"):
    os.mkdir("nova_pasta")
    print("Pasta criada!")"""


# ======================================================
# 4. SYS
# ======================================================

import sys

print("Versão do Py:", sys.version)

print("Caminho do executável:", sys.executable)

print()


# ======================================================
# 5. MATH
# ======================================================

import math

print("Raiz quadrada de 25:", math.sqrt(25))

print("Potência 2^3:", math.pow(2, 3))

print("Valor de PI:", math.pi)

print("Arredondamento para cima:", math.ceil(4.3))

print("Arredondamento para baixo:", math.floor(4.8))

print()

# ======================================================
# 6. TIME
# ======================================================

import time

print("Timestamp atual:", time.time())

print("Esperando 3 segundos...")
time.sleep(2)
print("Continuando execução...")
