import itertools

# espaço amostral de dois dados
S = list(itertools.product(range(1,7), range(1,7)))

A1 = [x for x in S if sum(x) <= 6]
A2 = [x for x in S if 7 <= sum(x) <= 9]
A3 = [x for x in S if sum(x) >= 10]

print('Tamanhos:')
print('A1:', len(A1))
print('A2:', len(A2))
print('A3:', len(A3))

print('\nSoma das probabilidades:')
print(len(A1)/36 + len(A2)/36 + len(A3)/36)
