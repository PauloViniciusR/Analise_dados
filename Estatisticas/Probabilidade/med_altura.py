"""Abaixo de 1,70 m	Acima de 1,70 m
Abaixo de 80 kg	30	15
Acima de 80 kg	10	45"""

tabela  = [
    [30, 15],
    [10, 45]
]

total_= sum(sum(linha) for linha in tabela)

acima_170 = tabela[0][1] + tabela[1][1]

prob = acima_170 / total_

print(prob)