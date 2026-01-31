salario_base = 1600

# Porcentagem
porcentagem_comissao = 0.05
valor_vendas = 500

salario_vendas = valor_vendas * porcentagem_comissao
salario_final = salario_base + salario_vendas
print("Salário final com comissão:", salario_final)

#Incremento
salario_base = salario_base + 200
print("novo salário base:", salario_base)
