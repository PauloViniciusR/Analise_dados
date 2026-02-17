""""Identificar quaisquer tempos de ciclo que estão dois desvios padrão 
acima ou abaixo da média."""


import numpy as np 

tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.7, 7.2, 4.8])
media = np.mean(tempos_ciclo)
print(media)

desvio_padrao = np.std(tempos_ciclo)
print(desvio_padrao)

condicao = tempos_ciclo > 5
print(np.where(condicao))

condicao = (tempos_ciclo > media + 2 * desvio_padrao) | (tempos_ciclo < media - 2 * desvio_padrao)
anomalias = np.where(condicao)
print(anomalias)

print(tempos_ciclo[anomalias])

print(f"Os tempos que estão na condição pedida são {tempos_ciclo[condicao]}")


print("----------------------------------------------------------")

#Dentro do intervalo

contrario_condicao = ((tempos_ciclo <= media + 2 * desvio_padrao) & (tempos_ciclo >= media - 2 * desvio_padrao))
print(np.where(contrario_condicao))

print(np.where(~condicao))

print()

print("----------------------------------------------------------")

rng = np.random.default_rng(seed=0)
tempos_gerados = rng.normal(loc=media, scale=desvio_padrao, size=100)
print(tempos_gerados)


print(media)
print(tempos_gerados.mean())
print()

print(desvio_padrao)
print(tempos_gerados.std())
print()

condicao = ((tempos_gerados > tempos_gerados.mean() + 2 * tempos_gerados.std())) | (tempos_gerados < tempos_gerados.mean() - 2 * tempos_gerados)
print(np.where(condicao))
print(tempos_gerados[condicao])   