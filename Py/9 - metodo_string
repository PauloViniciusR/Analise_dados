"""
MÉTODOS DE STRING EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Transformação de texto
- Busca
- Substituição
- Divisão
- Junção
- Validações
- Limpeza
"""

# ======================================================
# 1. TRANSFORMAÇÃO DE TEXTO
# ======================================================

texto = "python para dados"

print(texto.upper())       # Tudo maiúsculo
print(texto.lower())       # Tudo minúsculo
print(texto.capitalize())  # Primeira letra maiúscula
print(texto.title())       # Primeira letra de cada palavra maiúscula
print(texto.swapcase())    # Inverte maiúsculo/minúsculo


# ======================================================
# 2. BUSCA EM STRINGS
# ======================================================

frase = "Python é muito poderoso"

print(frase.find("muito"))      # Retorna posição
print(frase.index("Python"))    # Igual find, mas dá erro se não achar
print(frase.count("o"))         # Conta quantas vezes aparece


# ======================================================
# 3. SUBSTITUIÇÃO
# ======================================================

nova_frase = frase.replace("poderoso", "incrível")
print(nova_frase)


# ======================================================
# 4. DIVISÃO (SPLIT)
# ======================================================

dados = "Paulo,25,Analista"
lista_dados = dados.split(",")
print(lista_dados)


# ======================================================
# 5. JUNÇÃO (JOIN)
# ======================================================

palavras = ["Python", "para", "Dados"]
frase_final = " ".join(palavras)
print(frase_final)


# ======================================================
# 6. REMOVER ESPAÇOS
# ======================================================

texto_espaco = "   Olá Mundo   "

print(texto_espaco.strip())     # Remove dos dois lados
print(texto_espaco.lstrip())    # Remove da esquerda
print(texto_espaco.rstrip())    # Remove da direita


# ======================================================
# 7. VALIDAÇÕES
# ======================================================

numero = "12345"
letras = "Python"

print(numero.isdigit())   # Só números?
print(letras.isalpha())   # Só letras?
print(letras.isalnum())   # Letras e números?
print(letras.islower())   # Está minúsculo?
print(letras.isupper())   # Está maiúsculo?


# ======================================================
# 8. COMEÇA OU TERMINA COM
# ======================================================

arquivo = "relatorio.xlsx"

print(arquivo.startswith("relatorio"))
print(arquivo.endswith(".xlsx"))


# ======================================================
# 9. TAMANHO DA STRING
# ======================================================

print(len(texto))


# ======================================================
# 10. FATIAMENTO (SLICE)
# ======================================================

palavra = "Python"

print(palavra[0])      # Primeiro caractere
print(palavra[-1])     # Último caractere
print(palavra[0:3])    # Do índice 0 até 2
print(palavra[::-1])   # Inverte a string

