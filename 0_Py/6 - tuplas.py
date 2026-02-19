"""
TUPLAS EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- O que são tuplas
- Criação de tuplas
- Acesso a elementos
- Operações com tuplas
- Desempacotamento
- Tuplas com listas
- Exemplos práticos
"""

# ======================================================
# 1. O QUE É UMA TUPLA
# ======================================================
# Tupla é uma coleção:
# - ordenada
# - imutável (não pode ser alterada)
# - permite valores duplicados

tupla_vazia = ()
tupla_simples = (1, 2, 3)
tupla_strings = ("Python", "SQL", "Power BI")

print(tupla_vazia)
print(tupla_simples)
print(tupla_strings)

# ======================================================
# 2. TUPLA COM UM ÚNICO ELEMENTO
# ======================================================
# precisa da vírgula

tupla_um_elemento = (10,)
print(type(tupla_um_elemento))

# ======================================================
# 4. FATIAMENTO (SLICING)
# ======================================================

numeros = (0, 1, 2, 3, 4, 5)

print(numeros[1:4])
print(numeros[:3])
print(numeros[3:])
print(numeros[::-1])

# ======================================================
# 6. OPERAÇÕES COM TUPLAS
# ======================================================

numeros = (1, 2, 3, 4)

print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))

# ======================================================
# 7. TUPLAS COM LOOP
# ======================================================

frutas = ("maçã", "banana", "uva")

for fruta in frutas:
    print(fruta)

# ======================================================
# 8. DESEMPACOTAMENTO DE TUPLAS
# ======================================================

pessoa = ("Maria", 30, "Engenheira")

nome, idade, profissao = pessoa

print(nome)
print(idade)
print(profissao)

# ======================================================
# 9. USANDO * NO DESEMPACOTAMENTO
# ======================================================

numeros = (10, 20, 30, 40, 50)

a, b, *resto = numeros

print(a)
print(b)
print(resto)

# ======================================================
# 10. TUPLAS DENTRO DE LISTAS (MUITO COMUM EM DADOS)
# ======================================================

dados = [
    ('Produto A', 10, 2.5),
    ("Produto B", 5, 4.0),
    ("Produto C", 8, 3.2)
]

for produto, quantidade, preco in dados:
    total = quantidade * preco 
    print(produto, total)

# ======================================================
# 11. CONVERSÃO LISTA <-> TUPLA
# ======================================================

lista = [1, 2, 3]
tupla = tuple(lista)

print(tupla)

lista_nova = list(tupla)
print(lista_nova)


# ======================================================
# 12. QUANDO USAR TUPLA?
# ======================================================
# - dados que não devem mudar
# - coordenadas (x, y)
# - retorno de múltiplos valores
# - performance levemente melhor que listas
