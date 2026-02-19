"""
FUNÇÕES EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Criar funções
- Parâmetros
- Retorno
- Múltiplos parâmetros
- Parâmetros padrão
- Funções com listas
- Funções com loops
- Funções com try/except
- Funções lambda
"""

# ======================================================
# 1. FUNÇÃO SIMPLES
# ======================================================

def saudacao():
    """Função que imprime uma saudação"""

    print(f"Hello WOrld")

saudacao()


# ======================================================
# 2. FUNÇÃO COM PARÂMETRO
# ======================================================

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("MOlodoy")

# ======================================================
# 3. FUNÇÃO COM RETORNO
# ======================================================

def somar(a, b):
    resultado = a + b
    return resultado 

resultado = somar(10, 5)
print("Resultado:", resultado)

# ======================================================
# 4. FUNÇÃO COM MÚLTIPLOS PARÂMETROS
# ======================================================

def dados_usuarios(nome, idade, cidade):
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)

dados_usuarios("Paulo", 25, "São Paulo")


# ======================================================
# 5. PARÂMETRO PADRÃO
# ======================================================

def saudacao_personalizada(nome="Usuário"):
    print(f"Ola, {nome}")

saudacao_personalizada()
saudacao_personalizada("Fallen")


# ======================================================
# 6. FUNÇÃO COM RETORNO MÚLTIPLO
# ======================================================

def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

soma, sub = operacoes(10, 5)

print("Soma:", soma)
print("Subtração:", sub)

print()

# ======================================================
# 7. FUNÇÃO COM LISTA
# ======================================================

def somar_lista(lista):
    total = 0 

    for numero in lista:
        total+= numero

    return total

numeros = [10, 20, 40]

resultado = somar_lista(numeros)

print("Samar lista:", resultado)

print()

# ======================================================
# 8. FUNÇÃO COM LOOP
# ======================================================

def mostrar_lista(lista):
    for item in lista:
        print("Lista:", item)

mostrar_lista(["Python", "Dados"])

print()

# ======================================================
# 8. FUNÇÃO COM LOOP
# ======================================================

def converter_para_int(valor):
    try:
        numero = int(valor)
        return numero 
    
    except ValueError:

        print("Erro: valor inválido")
        return None

print(converter_para_int("10"))
print(converter_para_int("Py"))

print()

# ======================================================
# 10. FUNÇÃO QUE VERIFICA PAR OU ÍMPAR
# ======================================================

def verificar_par(numero):

    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(verificar_par(10))
print(verificar_par(7))

print()

# ======================================================
# 11. FUNÇÃO LAMBDA
# ======================================================

# função simples
dobro = lambda x: x * 2

print("Dobro:", dobro(5))

# lambda com dois parâmetros
somar = lambda a, b: a + b

print("Soma:", somar(3, 4))

print()

# ======================================================
# 12. FUNÇÃO APLICADA A DADOS
# ======================================================

def calcular_media(lista):
    soma = 0

    for numero in lista:
        soma += numero

    media = soma / len(lista)

    return media

notas = [7, 8, 9, 10]

media = calcular_media(notas)

print("Média", media)