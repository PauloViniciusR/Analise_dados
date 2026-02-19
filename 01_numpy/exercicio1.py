"""
Loja de segunda a sabado, independentemente de feriadoas. NOs ultimos 30 dias teve o menor volume de vendas 
sendo 20 e o maior 200. 
Criar simulação das vendas desses ultimos 30 dias, separando por semana. Calcule

- Total de vendas por semana
- a média de vendas por semana
- a media de vendas por dia da semana"""

import numpy as np

rng = np.random.default_rng(seed=42)
vendas_semanais = rng.integers(low=20, high=200, size=(5, 6), endpoint=True)
print(vendas_semanais)
print()

total_vendas_semana = vendas_semanais.sum(axis=1)
print(total_vendas_semana)
print()

media_vendas_semana = vendas_semanais.mean(axis=1)
print(media_vendas_semana)
print()

media_vendas_dia = vendas_semanais.mean(axis=0)
print(media_vendas_dia)
print()
    
    
