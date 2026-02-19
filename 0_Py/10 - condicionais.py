"""
CONDICIONAIS EM PYTHON (IF, ELIF, ELSE)
Autor: Paulo Vinícius

Conteúdo:
- if simples
- if e else
- if, elif e else
- Operadores de comparação
- Operadores lógicos
- Condições com strings
- Exemplos práticos
"""

# ======================================================
# 1. IF SIMPLES
# ======================================================

idade = 20

if idade >= 18:
    print("Maior de idade")


# ======================================================
# 2. IF E ELSE
# ======================================================

numero = 5

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")


# ======================================================
# 3. IF, ELIF E ELSE
# ======================================================

nota = 7.5

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")


# ======================================================
# 4. OPERADORES DE COMPARAÇÃO
# ======================================================

a = 10
b = 20

if a == b:
    print("São iguais")

if a != b:
    print("São diferentes")

if a < b:
    print("a é menor que b")

if a > b:
    print("a é maior que b")

if a <= b:
    print("a é menor ou igual a b")

if a >= b:
    print("a é maior ou igual a b")


# ======================================================
# 5. OPERADORES LÓGICOS
# ======================================================

idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

if idade < 18 or not tem_carteira:
    print("Não pode dirigir")


# ======================================================
# 6. CONDIÇÕES COM STRING
# ======================================================

nome = "Paulo"

if nome == "Paulo":
    print("Nome correto")

texto = "python para dados"

if "python" in texto:
    print("Contém a palavra python")

if texto.startswith("python"):
    print("Começa com python")

if texto.endswith("dados"):
    print("Termina com dados")


# ======================================================
# 7. EXEMPLO PRÁTICO (DADOS)
# ======================================================

salario = 3500

if salario > 5000:
    print("Salário alto")
elif salario >= 3000:
    print("Salário médio")
else:
    print("Salário baixo")


# ======================================================
# 8. CONDICIONAL TERNÁRIO
# ======================================================

idade = 17
resultado = "Maior de idade" if idade >= 18 else "Menor de idade"
print(resultado)


