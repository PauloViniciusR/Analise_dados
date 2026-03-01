"""
FUNDAMENTOS DE PYTHON
Autor: Paulo Vinícius
Conteúdo:
- Variáveis e tipos
- Strings
- Comparações
- Funções
- Listas
- Exercícios resolvidos

"""

# ======================================================
# 1. VARIÁVEIS E TIPOS DE DADOS
# ======================================================

nome = "Paulo"
idade = 25
altura = 1.75
estudante = True

print(f"Meu nome é {nome}, tenho {idade} anos, altura {altura} e estudante = {estudante}")

# Tipos
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))


# Exercício 2
x = "10"
y = 5

print(type(x))
print(type(y))

x = int(x)
soma = x + y
print("Soma:", soma)


# ======================================================
# 2. STRINGS
# ======================================================

frase = "Python é incrível"

# Palavra Python
print(frase[0:6])

# Maiúsculo
print(frase.upper())

# Substituição
print(frase.replace("incrível", "poderoso"))


# Exercício 4
nome_usuario = "Paulo Vinícius"

print("Quantidade de letras:", len(nome_usuario))
print("Nome invertido:", nome_usuario[::-1])


# ======================================================
# 3. COMPARAÇÕES E OPERADORES LÓGICOS
# ======================================================

a = 10
b = 5

print(a > b)
print(a == b)
print(a != b)


idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ======================================================
# 4. FUNÇÕES
# ======================================================

def soma(num1, num2):
    """
    Recebe dois números e retorna a soma
    """
    return num1 + num2

resultado = soma(10, 20)
print("Resultado da soma:", resultado)


def analisar_string(texto):
    """
    Recebe uma string e retorna:
    - string em maiúsculo
    - tamanho da string
    """
    return texto.upper(), len(texto)

texto_maiusculo, tamanho = analisar_string("python")
print(texto_maiusculo, tamanho)


# ======================================================
# 5. LISTAS
# ======================================================

numeros = [10, 20, 30, 40, 50]

print("Primeiro:", numeros[0])
print("Último:", numeros[-1])
print("Tamanho da lista:", len(numeros))


numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = [n for n in numeros2 if n % 2 == 0]
quadrados = [n ** 2 for n in numeros2]

print("Pares:", pares)
print("Quadrados:", quadrados)


# ======================================================
# 6. FUNÇÃO COM LISTA (NÍVEL DADOS)
# ======================================================

def estatisticas(lista):
    """
    Recebe uma lista de números e retorna:
    - média
    - maior valor
    - menor valor
    """
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)

    return media, maior, menor


dados = [10, 20, 30, 40, 50]
media, maior, menor = estatisticas(dados)

print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)


# ======================================================
# 7. STRINGS + LISTAS
# ======================================================

frase_usuario = "Python para dados"

frase_usuario = frase_usuario.lower()
palavras = frase_usuario.split()

print("Lista de palavras:", palavras)
print("Quantidade de palavras:", len(palavras))


# ======================================================
# FIM DO ARQUIVO
# ======================================================

print("Arquivo de fundamentos finalizado com sucesso")
