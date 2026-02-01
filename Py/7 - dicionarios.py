"""
DICIONÁRIOS EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- O que são dicionários
- Criação
- Acesso a valores
- Alterações
- Métodos principais
- Loop em dicionários
- Dicionários com listas e tuplas
- Exemplos práticos
"""

# ======================================================
# 1. O QUE É UM DICIONÁRIO
# ======================================================
# Dicionário:
# - pares chave:valor
# - não permite chaves duplicadas
# - valores podem ser alterados
# - muito usado para dados estruturados

dicionario_vazio = {}
pessoa = {
    'nome': 'Paulo',
    'idade': 25,
    'profissão': 'Analista de Dados'
}

print(dicionario_vazio)
print(pessoa)

# ======================================================
# 2. ACESSANDO VALORES
# ======================================================

print(pessoa['nome'])
print(pessoa.get('idade'))
print(pessoa.get('salário', 0))

# ======================================================
# 3. ADICIONANDO E ALTERANDO VALORES
# ======================================================

pessoa['cidade'] = 'São Paulo'
pessoa['idade'] = 26

print(pessoa)

# ======================================================
# 4. REMOVENDO ITENS
# ======================================================

pessoa.pop("cidade")

print(pessoa)

# ======================================================
# 5. MÉTODOS IMPORTANTES
# ======================================================

print(pessoa.keys()) # retorna todas as chaves do dicionario
print(pessoa.values()) # retorna todos os valores do dicionario
print(pessoa.items()) # retorna pares

# ======================================================
# 6. LOOP EM DICIONÁRIOS
# ======================================================

for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():
    print(chave, '=>', valor)

# ======================================================
# 7. VERIFICANDO EXISTÊNCIA DE CHAVE
# ======================================================

print("nome" in pessoa)
print("salario" in pessoa)

# ======================================================
# 8. DICIONÁRIO COM LISTAS
# ======================================================

aluno = {
    "nome": "Maria",
    "notas": [7, 8, 9]
}

media = sum(aluno["notas"]) / len(aluno["notas"])
print("Média:", media)

# ======================================================
# 9. LISTA DE DICIONÁRIOS (MUITO COMUM EM DADOS)
# ======================================================

produtos = [
    {"nome": "Produto A", "preco": 10.5, "estoque": 5},
    {"nome": "Produto B", "preco": 20.0, "estoque": 3},
    {"nome": "Produto C", "preco": 7.8, "estoque": 10}
]

for produto in produtos:
    total = produto["preco"] * produto["estoque"]
    print(produto["nome"], total)


# ======================================================
# 10. DICIONÁRIO COM TUPLAS
# ======================================================

coordenadas = {
    "ponto1": (10, 20),
    "ponto2": (30, 40)
}

print(coordenadas["ponto1"])


# ======================================================
# 11. ATUALIZANDO DICIONÁRIO
# ======================================================

pessoa.update({
    "idade": 27,
    "cidade": "Rio de Janeiro"
})

print(pessoa)


# ======================================================
# 12. EXEMPLO REAL (DADOS)
# ======================================================

vendas = {
    "janeiro": 1200,
    "fevereiro": 980,
    "marco": 1430
}

maior_mes = max(vendas, key=vendas.get)
print("Melhor mês:", maior_mes, vendas[maior_mes])
