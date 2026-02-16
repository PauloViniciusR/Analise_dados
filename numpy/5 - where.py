"""
NUMPY - WHERE
Autor: Paulo Vinícius

Função where para condições e filtros
"""

import numpy as np


# ======================================================
# 1. ARRAY BASE
# ======================================================

array = np.array([5, 12, 8, 20, 3, 15])

print("Array:", array)


# ======================================================
# 2. ENCONTRAR ÍNDICES
# ======================================================

# retorna os índices onde a condição é verdadeira
indices = np.where(array > 10)

print("\nÍndices onde valor > 10:", indices)


# ======================================================
# 3. SUBSTITUIR VALORES
# ======================================================

# se maior que 10 → 1, senão → 0
resultado = np.where(array < 10, 1, 0)

print("\nMaior que 10 vira 1:", resultado)

# ======================================================
# 4. SUBSTITUIR VALORES NEGATIVOS
# ======================================================

valores = np.array([-5, 10, -2, 7, -1])

corrigido = np.where(valores < 0, 0, valores)

print("\nNegativos substituidos por 0", corrigido)

# ======================================================
# 5. USANDO STRINGS
# ======================================================

notas = np.array([4, 7, 5, 8, 10])

status = np.where(notas >= 6, "Aprovado", "REprovado")

print("\nStatus", status)

# ======================================================
# 6. CONDIÇÕES MÚLTIPLAS
# ======================================================

# entre 10 e 20
condicao = np.where((array >= 10) & (array <= 20), "OK", "FORA")

print("\nEntre 10 e 20:", condicao)

# ======================================================
# 7. USO PRÁTICO EM DATA SCIENCE
# ======================================================

salarios = np.array([1500, 2500, 4000, 1200, 3000])

categoria = np.where(salarios >= 3000, "Alto", "Baixo")

print("\nCategoria salarial:", categoria)