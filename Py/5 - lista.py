"""
EXEMPLOS DE LISTAS EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Criação de listas
- Acesso e fatiamento
- Métodos principais
- Laços
- List comprehension
- Exemplos práticos
"""

# ======================================================
# 1. CRIAÇÃO DE LISTAS
# ======================================================

lista_numeros = [1, 2, 3, 4, 5]
lista_Strings = ['Python', 'SQL', 'Pandas', 'MachineLearn']
lista_mista = [1, 'Dados', True, 3.14]
lista_vazia = []

print(lista_numeros)
print(lista_Strings)
print(lista_mista)
print(lista_vazia)

# ======================================================
# 2. ACESSO A ELEMENTOS
# ======================================================

numero = [10, 20, 30, 40, 50]
print(numero[0])
print(numero[2])
print(numero[-1])

# ======================================================
# 3. FATIAMENTO (SLICING)
# ======================================================

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[2:6])
print(lista[:4])     # [0, 1, 2, 3]
print(lista[5:])     # [5, 6, 7, 8, 9]
print(lista[::2])    # pula de 2 em 2
print(lista[::-1])   # lista invertida

# ======================================================
# 4. ALTERANDO LISTAS
# ======================================================

dados = [1, 2, 3]

dados.append(4) # adiciona no final
dados.insert(0, 99) # adiciona na posição
dados.extend([5, 6, 7]) # insere na lista

print(dados)

# ======================================================
# 5. REMOVENDO ELEMENTOS
# ======================================================

valores = [10, 20, 30, 40, 50]

valores.remove(30) # remove pelo valor
valores.pop() # remove o último
valores.pop(0) #remove pelo índice
#del valores(0)  #remove pelo índice

print(valores)

# ======================================================
# 6. PERCORRENDO LISTAS
# ======================================================

nomes = ['Pedro', 'Arrasca', 'BH']

for nome in nomes: 
    print(nome)

# com índice 
for i, nome in enumerate(nomes):
    print(i, nome)

# ======================================================
# 7. OPERAÇÕES COM LISTAS
# ======================================================

numeros = [5, 2, 9, 1, 7]

print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))

numeros.sort()      # ordena crescente
numeros.reverse()   # inverte ordem

print(numeros)

# ======================================================
# 8. LIST COMPREHENSION
# ======================================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = [n for n in numeros if n % 2 == 0]
quadrados = [n ** 2 for n in numeros]

print(pares)
print(quadrados)

# ======================================================
# 9. LISTA DE LISTAS (MATRIZ)
# ======================================================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(matriz)
print(matriz[3])
print(matriz[1][2]) # acessando elementos

# ======================================================
# 10. EXEMPLO REAL (DADOS)
# ======================================================

precos = [10.5, 20.0, 30.75, 15.25]

media = sum(precos) / len(precos)
print('Média dos preços:', media)