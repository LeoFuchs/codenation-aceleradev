# Semana 8 (Teórico)

## Regressão

### Trade-off Bias x Variance

__Viés (Bias)__: Se deve à escolha do modelo, que pode ter sido muito simples para um problema em mãos.
É relacionado ao underfitting do modelo.

__Variância__: Está relacionada a complexidade do modelo. Qualquer dado externo do conjunto de treino é considerado 
ruído. É relacionado ao overfitting do modelo.

_Overfitting_: Utiliza-se de um modelo complexo para reduzir o erro a praticamente 0 no treinamento. Possui um viés 
baixo e uma alta variância. O modelo tende a funcionar apenas com os dados de treino.

_Underfitting_: Utiliza-se um modelo genérico ou desajustado. Possui um erro alto, um viés alto com baixa variância. 
O modelo tende a não funcionar bem nem no treino nem no teste.

Problema de Alta Variedade/Variância (_Overfitting_): Existem duas soluções: Obter mais exemplos de treinamento, porque 
quanto maior o conjunto de dados, maior a probabilidade de obter previsões mais assertivas. Ou experimentar conjuntos 
menores de features (porque o modelo está ajustado demais).

Problema de Alto Viés (_Underfitting_): Existem duas soluções: Tente obter recursos adicionais, você está generalizando
os conjuntos de dados. Ou tente adicionar recursos polinomiais, torne o modelo mais complexo.

![](https://miro.medium.com/proxy/1*k_D4-U7c3Tf8hJRpaOZoBQ.png)