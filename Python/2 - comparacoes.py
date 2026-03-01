"""
COMPARAÇÕES EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Operadores de comparação
- Operadores lógicos
- Condicionais (if / elif / else)
- Comparações com strings
- Comparações com listas
- Exemplos práticos
"""

# ======================================================
# 1. OPERADORES DE COMPARAÇÃO
# ======================================================

a = 10
b = 5

print(a == b)   # igual
print(a != b)   # diferente
print(a > b)    # maior
print(a < b)    # menor
print(a >= b)   # maior ou igual
print(a <= b)   # menor ou igual


# ======================================================
# 2. OPERADORES LÓGICOS
# ======================================================

idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira)   # AND
print(idade < 18 or tem_carteira)     # OR
print(not tem_carteira)               # NOT


# ======================================================
# 3. IF / ELSE
# ======================================================

idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ======================================================
# 4. IF / ELIF / ELSE
# ======================================================

nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


# ======================================================
# 5. COMPARAÇÕES COM STRINGS
# ======================================================

senha = "1234"

if senha == "1234":
    print("Acesso permitido")
else:
    print("Senha incorreta")


# Case-sensitive
print("Python" == "python")


# ======================================================
# 6. COMPARANDO STRINGS (BOA PRÁTICA)
# ======================================================

usuario = "Admin"

if usuario.lower() == "admin":
    print("Usuário administrador")


# ======================================================
# 7. COMPARAÇÕES NUMÉRICAS EM FUNÇÃO
# ======================================================

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

print(maior_numero(10, 20))


# ======================================================
# 8. COMPARAÇÕES COM LISTAS
# ======================================================

numeros = [10, 20, 30]

print(20 in numeros)
print(40 not in numeros)


# ======================================================
# 9. COMPARANDO TAMANHO DE LISTAS
# ======================================================

lista_a = [1, 2, 3]
lista_b = [1, 2, 3, 4, 5]

if len(lista_a) > len(lista_b):
    print("Lista A é maior")
else:
    print("Lista B é maior")


# ======================================================
# 10. COMPARAÇÕES MÚLTIPLAS
# ======================================================

valor = 15

if 10 <= valor <= 20:
    print("Valor dentro do intervalo")


# ======================================================
# 11. COMPARAÇÃO COM BOOLEAN
# ======================================================

ativo = False

if ativo:
    print("Usuário ativo")
else:
    print("Usuário inativo")


# ======================================================
# 12. EXEMPLO REAL (DADOS)
# ======================================================

preco = 120
desconto = 15

if desconto >= 10 and preco > 100:
    preco_final = preco - desconto
else:
    preco_final = preco

print("Preço final:", preco_final)

