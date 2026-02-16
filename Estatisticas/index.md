FUNDAMENTOS DE PROBABILIDADE

1. Experimento Aleatório

Um experimento aleatório é um procedimento que, quando realizado sob condições semelhantes, pode produzir diferentes resultados, e cujo resultado específico não pode ser previsto com certeza absoluta antes de sua realização.

Exemplos incluem o lançamento de uma moeda, o lançamento de um dado ou a seleção aleatória de um indivíduo em uma população.

2. Espaço Amostral

O espaço amostral, denotado por Ω (ômega), é o conjunto de todos os resultados possíveis de um experimento aleatório.

Exemplo:

No lançamento de um dado de seis faces:

Ω = {1, 2, 3, 4, 5, 6}

O número total de elementos do espaço amostral é representado por:

n(Ω)

3. Evento

Um evento é qualquer subconjunto do espaço amostral.

Se A é um evento, então:

A ⊆ Ω

O número de elementos do evento A é representado por:

n(A)

Exemplo:

Evento A: obter um número par no lançamento de um dado

A = {2, 4, 6}

4. Definição Clássica de Probabilidade

Se todos os resultados do espaço amostral são igualmente prováveis, a probabilidade de ocorrência de um evento A é definida como:

P(A) = n(A) / n(Ω)

Onde:

P(A) = probabilidade do evento A ocorrer
n(A) = número de resultados favoráveis ao evento
n(Ω) = número total de resultados possíveis

A probabilidade é um número real tal que:

0 ≤ P(A) ≤ 1

5. Propriedades Fundamentais da Probabilidade

Para qualquer evento A, valem as seguintes propriedades:

Não negatividade:

P(A) ≥ 0

Normalização:

P(Ω) = 1

Probabilidade do evento impossível:

P(∅) = 0

Onde ∅ representa o conjunto vazio.

6. Evento Complementar

O complemento de um evento A, denotado por Aᶜ, é o conjunto de todos os resultados do espaço amostral que não pertencem a A.

A probabilidade do evento complementar é dada por:

P(Aᶜ) = 1 − P(A)

7. União de Eventos

A união de dois eventos A e B, denotada por A ∪ B, representa o evento em que A ocorre, ou B ocorre, ou ambos ocorrem.

A probabilidade da união é dada por:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

Onde A ∩ B representa a interseção dos eventos A e B.

8. Interseção de Eventos

A interseção de dois eventos A e B, denotada por A ∩ B, representa o evento em que ambos ocorrem simultaneamente.

Se A e B são eventos independentes, então:

P(A ∩ B) = P(A) × P(B)

9. Eventos Independentes

Dois eventos A e B são independentes quando a ocorrência de um não influencia a ocorrência do outro.

Formalmente, A e B são independentes se:

P(A ∩ B) = P(A) × P(B)

10. Probabilidade Condicional

A probabilidade condicional de um evento A dado que o evento B ocorreu é definida por:

P(A | B) = P(A ∩ B) / P(B), com P(B) > 0

Esta medida representa a probabilidade de A ocorrer sob a condição de que B já tenha ocorrido.

11. Variável Aleatória

Uma variável aleatória é uma função que associa um número real a cada resultado de um experimento aleatório.

Pode ser classificada como:

Variável aleatória discreta: assume valores isolados e enumeráveis.
Exemplo: número de caras em lançamentos de moeda.

Variável aleatória contínua: assume valores em intervalos reais.
Exemplo: altura, peso, tempo.

12. Interpretação da Probabilidade

A probabilidade é uma medida numérica que quantifica a incerteza associada à ocorrência de um evento.

Se:

P(A) = 0 → evento impossível
P(A) = 1 → evento certo
0 < P(A) < 1 → evento possível, mas incerto