# ======================================================
# 1. RANDOM
# ======================================================

import numpy as np

rng = np.random.default_rng()
print(rng)

numero_Aleatorio = rng.random() * 10
print(numero_Aleatorio)

print()

# ======================================================
# 2. ANALISE
# ======================================================

"""
Gerar dados falsos para 30 dias 
VAmos supor que as vendas de um produto podem variar de 50 a 200 por dia
Pode definir uma seed para garantir que os resultados sejam foram reproduziveis
"""

rng = np.random.default_rng(seed=42) #estatizar os numeros gerados aleatorio
dados_vendas = rng.integers(low=50, high=200, size=30)
print(dados_vendas)

print("---------------------------------------------------------------------------")

print("Maior venda:",np.max(dados_vendas))

print("Qual dia da maior venda:", np.argmax(dados_vendas) + 1)

print("Menor venda:", np.min(dados_vendas))

print("Qual dia da menor venda:", np.argmin(dados_vendas) + 1)

media = np.mean(dados_vendas)
print(f"A média de vendas é de {media} vendas por dia")

print(np.median(dados_vendas)) #Mediana

print(np.percentile(dados_vendas, 50))

print(np.std(dados_vendas)) #Desvio padrão

print(np.var(dados_vendas)) #Variancia
