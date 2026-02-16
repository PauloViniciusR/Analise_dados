import numpy as np

# ======================================================
# 1. DADOS
# ======================================================

vendas = np.array([120, 140, 230, 420, 560, 680])

print("Vendas:", vendas)

print()

# ======================================================
# 2. INFORMAÇÕES BÁSICAS
# ======================================================

print("\nQuantidade:", np.sum(vendas))

print("Tipo:", vendas.dtype)

print("Dimensão:", vendas.ndim)

print("Shape:", vendas.shape)


# ======================================================
# 3. ESTATÍSTICAS
# ======================================================

print("\nTotal vendido:", np.sum(vendas))

print("Média:", np.mean(vendas))

print("Máximo:", np.max(vendas))

print("Mínimo:", np.min(vendas))

print("Desvio padrão:", np.std(vendas))

print()

# ======================================================
# 4. FILTROS
# ======================================================

filtro = vendas > 150

print("\nFiltro:", filtro)

print("Vendas maiores que 150:", vendas[filtro])


# ======================================================
# 5. OPERAÇÕES
# ======================================================

# aumento de 10%
aumento = vendas * 1.10

print("\nVendas com aumento de 10%:", aumento)


# ======================================================
# 6. INDEXAÇÃO
# ======================================================

print("\nPrimeiro dia:", vendas[0])

print("Último dia:", vendas[-1])


# ======================================================
# 7. MATRIZ (MULTIDIMENSIONAL)
# ======================================================

# vendas por semana (2 semanas)
matriz = np.array([
    [120, 150, 200],
    [130, 170, 210]
])

print("\nMatriz:")
print(matriz)

print("Shape:", matriz.shape)

print("Total matriz:", np.sum(matriz))


# ======================================================
# 8. GERAR DADOS ALEATÓRIOS
# ======================================================

dados = np.random.randint(100, 300, 10)

print("\nDados aleatórios:", dados)

print("Média:", np.mean(dados))


# ======================================================
# 9. RESHAPE
# ======================================================

novo = dados.reshape(5, 2)

print("\nArray reshape:")
print(novo)