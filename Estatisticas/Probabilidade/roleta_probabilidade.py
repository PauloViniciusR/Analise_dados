import random

roleta = ["vermelho"] * 18 + ["preto"] * 18 + ["verde"] * 2

resultado = random.choice(roleta)

print("Resultado:", resultado)

# -------------------------------------------------------
# QUESTÃO 1: Probabilidade de cair nas casas vermelhas
# -------------------------------------------------------

vermelhas = 18 
total = 38 

prob = vermelhas / total

print("Probabilidades (fracão):", vermelhas, '/', total)
print("Decial:", prob)
print(f"Porcentagem: {prob:.2%}")   

print()

# -------------------------------------------------------
# QUESTÃO 2: Probabilidade de cair na coluna 1 ou 1st 12
# -------------------------------------------------------

coluna1 = 12 
primeira_duzia = 12 
intersecao = 4 
total = 38

favoraveis = coluna1 + primeira_duzia - intersecao 

prob = favoraveis / total 

print("Casos favoráveis", favoraveis)
print("Probabilidade (fração):", favoraveis, "/", total)
print(f"Probabilidade (%): {prob:.2%}")

print()