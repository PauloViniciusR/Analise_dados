"""
FUNÇÕES EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- O que são funções
- Funções simples
- Parâmetros e retorno
- Funções com strings
- Funções com listas
- Boas práticas
"""

# ======================================================
# 1. FUNÇÃO SIMPLES (SEM PARÂMETROS)
# ======================================================

def saudacao():
    print('Usando funções')

saudacao()


# ======================================================
# 2. FUNÇÃO COM PARÂMETROS
# ======================================================

def saudar_nome(nome):
    print(f"Olá, {nome}!")

saudar_nome("Paulo")


# ======================================================
# 3. FUNÇÃO COM RETORNO
# ======================================================

def soma(a, b):
    return a + b

resultado = soma(10, 20)
print("Resultado da soma:", resultado)


# ======================================================
# 4. FUNÇÃO COM TIPOS DIFERENTES
# ======================================================

def apresentar(nome, idade):
    return f"Nome: {nome} | Idade: {idade}"

print(apresentar("Maria", 30))


# ======================================================
# 5. FUNÇÃO COM CONDICIONAL
# ======================================================

def maior_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(maior_idade(20))
print(maior_idade(15))


# ======================================================
# 6. FUNÇÃO COM STRING
# ======================================================

def analisar_string(texto):
    """
    Retorna:
    - texto em maiúsculo
    - tamanho do texto
    """
    texto_maiusculo = texto.upper()
    tamanho = len(texto)
    return texto_maiusculo, tamanho

resultado = analisar_string("python")
print(resultado)


# ======================================================
# 7. FUNÇÃO COM LISTA
# ======================================================

def soma_lista(numeros):
    return sum(numeros)

print(soma_lista([10, 20, 30]))


# ======================================================
# 8. FUNÇÃO COM LISTA (ESTATÍSTICA BÁSICA)
# ======================================================

def estatisticas(lista):
    """
    Retorna:
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
# 9. FUNÇÃO COM LIST COMPREHENSION
# ======================================================

def filtrar_pares(lista):
    return [n for n in lista if n % 2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))


# ======================================================
# 10. FUNÇÃO COM STRING + LISTA
# ======================================================

def contar_palavras(frase):
    palavras = frase.lower().split()
    return len(palavras)

print(contar_palavras("Python é muito poderoso para dados"))


# ======================================================
# 11. FUNÇÃO COM VALOR PADRÃO
# ======================================================

def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5))
print(potencia(5, 3))


# ======================================================
# 12. BOA PRÁTICA: FUNÇÃO PEQUENA E CLARA
# ======================================================

def eh_par(numero):
    return numero % 2 == 0

print(eh_par(10))
print(eh_par(7))

