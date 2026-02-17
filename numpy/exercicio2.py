""""VOce pediu aos clientes para classifiar seu nivel de satisfação em uma escala de 0 a 10. 
Coletamos respostas de 30 clientes por dia durante 7 dias, resultando no total dde 210 respostas    

No entanto, os dados que voce recebeu estão em um array 1D de 210 elementos.Reorganize os dados de forma a ter
as respostas por dia e faça uma analise descritiva basica, calculando a media geral de satisfação e a média diaria."""

import numpy as np 

# COnsidere os dados aleatorios
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
print(respostas)

respostas_reshape = np.reshape(respostas,(7, 30))
print(respostas_reshape)

media_geral = np.mean(respostas_reshape)
print(media_geral)

media_diaria = np.mean(respostas_reshape, axis=1)
print(media_diaria)