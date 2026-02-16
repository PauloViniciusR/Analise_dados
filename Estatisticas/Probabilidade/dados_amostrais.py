from itertools import product 

espaco_amostral = list(product(range(1,7), repeat=2))

print("Espaço amostral total:", len(espaco_amostral))
print()

# ---------------------------------------------------
# QUESTÃO 1: soma maior que 10
# ---------------------------------------------------

soma_maior_10 = [par for par in espaco_amostral if sum(par) > 10]

print("Q1 - Soma maior qeu 10")
print("Pares:", soma_maior_10)
print("Quantidade:", len(soma_maior_10))

prob = len(soma_maior_10) / len(espaco_amostral)
print(f"Probabilidade: {prob:.2%}")

print()

# ---------------------------------------------------
# QUESTÃO 2: primeiro par e segundo ímpar
# ---------------------------------------------------

par_impar = [par for par in espaco_amostral if par[0] % 2 == 0 and par[1] % 2 != 0] 

print("Q2 - Primeiro par e segundo ímpar" )
print("Quantidade:", len(par_impar))

prob = len(par_impar) / len(espaco_amostral)
print(f"Probabilidade: {prob:.2%}")

print()

# ---------------------------------------------------
# QUESTÃO 3: diferença diferente de 2
# ---------------------------------------------------

dif_que_2 = [par for par in espaco_amostral if abs(par[0] - par[1]) != 2]

print("Q3 - Diferença diferente de 2")
print("QUantidade:", len(dif_que_2))

prob = len(dif_que_2) / len(espaco_amostral)
print(f"Probabilidade:{prob:.2%}")

print()

# ---------------------------------------------------
# QUESTÃO 4: pelo menos um dado é 6
# ---------------------------------------------------

pelo_menos_um_6 = [par for par in espaco_amostral if 6 in par]

print("Q4 - Pelo menos um dado é 6")
print("Quantidade:", len(pelo_menos_um_6))

prob = len(pelo_menos_um_6) / len(espaco_amostral)
print(f"Probabilidade: {prob:.2%}")
