"""
LOOPS E TRATAMENTO DE ERROS EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- for
- for com range
- while
- break e continue
- try e except
- try, except, else e finally
"""

# ======================================================
# 1. LOOP FOR COM LISTA
# ======================================================

print("\n--- FOR COM LISTA ---")

nomes = ["KS", "Molodoy", "Fallen"]

for nome in nomes:
    print("Nome:", nome)


# ======================================================
# 2. LOOP FOR COM STRING
# ======================================================

print("\n--- FOR COM STRING ---")

texto = "Python"

for letra in texto:
    print(letra)


# ======================================================
# 3. LOOP FOR COM RANGE
# ======================================================

print("\n--- FOR COM RANGE ---")

# range(inicio, fim, passo)

for i in range(5):
    print("Número", i)

print("\nRange com início e fim:")

for i in range(1, 6):
    print("Número", i)

print("\nRange com passo:")

for i in range(0,10,2):
    print("Número", i)


# ======================================================
# 4. FOR COM ÍNDICE (enumerate)
# ======================================================

print("\n--- FOR COM ÍNDICE ---")

frutas = ["Maçã", "Laranja", "Acerola"]

for indice, frutas in enumerate(frutas):
    print("Índice", indice, "| Fruta:", frutas)


# ======================================================
# 5. LOOP WHILE
# ======================================================

print("\n--- WHILE COM CONDIÇÃO ---")

numero = 1

while numero <= 10:
    print("Número:", numero)
    numero += 1


# ======================================================
# 7. BREAK
# ======================================================

print("\n--- BREAK ---")

for i in range(10):

    if i == 5:
        print("Parando o loop")
        break

    print(i)


# ======================================================
# 8. CONTINUE
# ======================================================

print("\n--- CONTINUE ---")

for i in range(5):

    if i == 2:
        continue

    print(i)


# ======================================================
# 9. TRY EXCEPT
# ======================================================

print("\n--- TRY EXCEPT ---")

try:

    numero = int("abc")

except ValueError:

    print("Erro: conversão inválida")


# ======================================================
# 10. TRY EXCEPT COM DIVISÃO
# ======================================================

print("\n--- TRY EXCEPT DIVISÃO ---")

try:

    resultado = 10 / 0

except ZeroDivisionError:

    print("Erro: divisão por zero")


# ======================================================
# 11. TRY EXCEPT ELSE
# ======================================================

print("\n--- TRY EXCEPT ELSE ---")

try:

    numero = int("10")

except ValueError:

    print("Erro")

else:

    print("Conversão bem sucedida:", numero)


# ======================================================
# 12. TRY EXCEPT FINALLY
# ======================================================

print("\n--- TRY EXCEPT FINALLY ---")

try:

    numero = int("20")
    print(numero)

except ValueError:

    print("Erro")

finally:

    print("Executa sempre")


# ======================================================
# 13. EXEMPLO PRÁTICO (DADOS)
# ======================================================

print("\n--- EXEMPLO PRÁTICO ---")

valores = ["10", "20", "abc", "30"]

for valor in valores:

    try:

        numero = int(valor)
        print("Número convertido:", numero)

    except ValueError:

        print("Valor inválido:", valor)