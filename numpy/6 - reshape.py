import numpy as np 

# Vendas diarias por 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])
# Reorganizar os dados em uma matriz 2x7

vendas_reshape = np.reshape(vendas, (2, 7))
print(vendas_reshape)
print()

print(vendas_reshape.ndim)
print()

print(vendas_reshape.shape)
print()

print(vendas_reshape[0])
print()

print(vendas_reshape[0][0])
print()

print(vendas_reshape[0][1])
print()

print(vendas_reshape.sum())
print()

print("--------------------------------------------------")
#Axis (Eixo)

print(vendas_reshape.sum(axis=0)) # somar no eixo 0 (em colunas)
print()

print(vendas_reshape.sum(axis=1)) # a soma da primeira linha toda e soma da segunda linha toda