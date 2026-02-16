"""
NUMPY - FUNÇÕES
Autor: Paulo Vinícius

Funções matemáticas e estatísticas
"""

import numpy as np


# ======================================================
# 1. ARRAY BASE
# ======================================================

array = np.array([10, 20, 30, 40, 50])

print("Array:", array)


# ======================================================
# 2. FUNÇÕES MATEMÁTICAS
# ======================================================

print("\nSoma:", np.sum(array))

print("Média:", np.mean(array))

print("Máximo:", np.max(array))

print("Mínimo:", np.min(array))

print("Desvio padrão:", np.std(array))


# ======================================================
# 3. FUNÇÕES DE POSIÇÃO
# ======================================================

print("\nÍndice do maior valor:", np.argmax(array))

print("Índice do menor valor:", np.argmin(array))


# ======================================================
# 4. RAIZ E POTÊNCIA
# ======================================================

print("\nRaiz quadrada:", np.sqrt(array))

print("Potência ao quadrado:", np.power(array, 2))


# ======================================================
# 5. ARREDONDAMENTO
# ======================================================

decimais = np.array([1.2, 2.5, 3.7])

print("\nArredondado:", np.round(decimais))


# ======================================================
# 6. FUNÇÕES LÓGICAS
# ======================================================

print("\nMaior que 25:", np.where(array > 25))


# ======================================================
# 7. FUNÇÕES DE ARRAY
# ======================================================

print("\nOrdenado:", np.sort(array))

print("Array invertido:", np.flip(array))

print()

# ======================================================
# 8. FUNÇÕES DE DOT
# ======================================================

a = np.array([1, 1, 1])
b = np.array([1, 1, 1])

resultado = np.dot(a, b)

print(resultado)
