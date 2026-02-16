"""
NUMPY + TIME
Autor: Paulo Vinícius

Medindo performance do NumPy
"""

import numpy as np
import time


# ======================================================
# 1. MEDIR TEMPO DE EXECUÇÃO SIMPLES
# ======================================================

inicio = time.time()

array = np.arange(0, 1000000)

soma = np.sum(array)

fim = time.time()

print("Soma:", soma)

print("Tempo de execução:", fim - inicio, "segundos")


# ======================================================
# 2. COMPARAÇÃO: LISTA VS NUMPY
# ======================================================

# Lista Python
inicio = time.time()

lista = list(range(1000000))

soma_lista = sum(lista)

fim = time.time()

tempo_lista = fim - inicio

print("\nTempo lista:", tempo_lista)


# NumPy
inicio = time.time()

array = np.arange(1000000)

soma_array = np.sum(array)

fim = time.time()

tempo_numpy = fim - inicio

print("Tempo NumPy:", tempo_numpy)


# ======================================================
# 3. MOSTRAR QUAL É MAIS RÁPIDO
# ======================================================

if tempo_numpy < tempo_lista:

    print("\nNumPy é mais rápido 🚀")

else:

    print("\nLista é mais rápida")


# ======================================================
# 4. GERAR DADOS E MEDIR
# ======================================================

inicio = time.time()

dados = np.random.rand(1000000)

media = np.mean(dados)

fim = time.time()

print("\nMédia:", media)

print("Tempo:", fim - inicio)
