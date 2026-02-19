"""
NUMPY - ARRAYS
Autor: Paulo Vinícius

Criação e manipulação de arrays
"""

import numpy as np


# ======================================================
# 1. CRIAR ARRAY A PARTIR DE LISTA
# ======================================================

array = np.array([10, 20, 30, 40, 50])

print("Array:", array)


# ======================================================
# 2. INFORMAÇÕES DO ARRAY
# ======================================================

print("\nTipo:", type(array))

print("Tipo dos dados:", array.dtype)

print("Shape:", array.shape)

print("Dimensão:", array.ndim)

print("Tamanho:", array.size)


# ======================================================
# 3. INDEXAÇÃO
# ======================================================

print("\nPrimeiro elemento:", array[0])

print("Último elemento:", array[-1])


# ======================================================
# 4. SLICING
# ======================================================

print("\nDo índice 1 ao 3:", array[1:4])

print("Primeiros 3:", array[:3])

print("Últimos 2:", array[-2:])


# ======================================================
# 5. ARRAY AUTOMÁTICO
# ======================================================

array_range = np.arange(0, 10)

print("\nArray range:", array_range)


# ======================================================
# 6. ARRAY DE ZEROS
# ======================================================

zeros = np.zeros(5)

print("\nZeros:", zeros)


# ======================================================
# 7. ARRAY DE UNS
# ======================================================

uns = np.ones(5)

print("\nUns:", uns)


# ======================================================
# 8. ARRAY ALEATÓRIO
# ======================================================

aleatorio = np.random.randint(1, 100, 5)

print("\nArray aleatório:", aleatorio)


# ======================================================
# 9. MATRIZ
# ======================================================

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatriz:")
print(matriz)

print("Shape matriz:", matriz.shape)
