"""
STRINGS COM .format() EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Uso básico do .format()
- Múltiplas variáveis
- Índices
- Nomeação de parâmetros
- Formatação numérica
- Formatação de casas decimais
- Alinhamento
- Exemplos práticos
"""

# ======================================================
# 1. USO BÁSICO
# ======================================================

nome = "Paulo"
idade = 25

frase = "Meu nome é {} e tenho {} anos.".format(nome, idade)
print(frase)


# ======================================================
# 2. USANDO ÍNDICES
# ======================================================

print("Meu nome é {0} e tenho {1} anos.".format(nome, idade))
print("Tenho {1} anos e me chamo {0}.".format(nome, idade))

# ======================================================
# 3. NOMEANDO PARÂMETROS
# ======================================================

print("NOme: {nome} | Idade: {idade}".format(nome="MAria", idade=30))

# ======================================================
# 4. FORMATANDO NÚMEROS
# ======================================================

valor = 1234.56789

# 2 casas decimais
print("Valor formatado: {:.2f}".format(valor))

# Separador de milhar
print("Valor com milhar: {:,.2f}".format(valor))

# ======================================================
# 5. PORCENTAGEM
# ======================================================

taxa = 0.8567

print("Taxa: {:.2%}".format(taxa))

# ======================================================
# 6. ALINHAMENTO
# ======================================================

texto = "Python"

# Alinhado à direita
print("{:>10}".format(texto))

# Alinhado à esquerda
print("{:<10}".format(texto))

# Centralizado
print("{:^10}".format(texto))

# ======================================================
# 7. PREENCHIMENTO
# ======================================================

print("{:*^20}".format("Dados"))


# ======================================================
# 8. EXEMPLO REAL (DADOS)
# ======================================================

produto = "Notebook"
preco = 3500.5
estoque = 8

mensagem = "Produto: {} | Preço: R${:.2f} | Estoque: {}".format(produto, preco, estoque)

print(mensagem)


# ======================================================
# 9. USANDO .format() COM DICIONÁRIO
# ======================================================

pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo"
}

print("Nome: {nome}, Idade: {idade}, Cidade: {cidade}".format(**pessoa))


# ======================================================
# 10. EXEMPLO COM LISTA
# ======================================================

notas = [7.5, 8.0, 9.2]
media = sum(notas) / len(notas)

print("Notas: {} | Média: {:.2f}".format(notas, media))