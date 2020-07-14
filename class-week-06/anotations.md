# Semana 6 (Teórico)

### Machine Learning Canvas

![](https://miro.medium.com/max/2594/1*17k48Dwk5xAP2L0KX8FKyw.jpeg)

### Mapas Mentais (Prototipação)

https://www.mindmeister.com/pt/

### CRISP-DM

![](https://www.datocms-assets.com/6503/1546015659-crispen.png)

### Dimensionalidade

- Maldição da Dimensionalidade: Também conhecido como *curse of dimensionality* é um fator muito relevante para decidir
qual a dimensionalidade ideal a ser adotada em um problema de reconhecimento de padrões.

- Redução da Dimensionalidade: Processo de conversão de um conjunto de dados que possui vastas dimensões em dados com
dimensões menores. Assegurando que o conjunto reduzido transmita informações semelhantes de forma concisa.

### Seleção de Features

- O processo de seleção de um subconjunto de recursos relevantes (variáveis, preditores) para uso na construção do
modelo. 

- Simplificação de modelos para facilitar a interpretação.

- Tempo de treinamento mais curto.

- Evitar problemas de dimensionalidade.

- Generalização aprimorada pode reduzir o *overfitting* (funciona apenas para o treino/teste inicial)

![](https://miro.medium.com/max/694/0*gz5XuPZfN0wAi66I)

### Extração de Features

- Diminuir o número de *features* para explicar melhor os dados.

- Interpretar o comportamento de cada *feature*.

- Parte do processo de redução de dimensionalidade.

### Análise de Componentes Principais (*Principal Component Analysis* - PCA)

- Ferramenta matemática para reduzir a dimensionalidade dos dados.

- Bastante útil quando tratamos problemas com altas dimensões.

- Identifica a relação entre as características extraídas dos dados.

- Exemplo: Escolhe-se um número de variáveis que se deseja reduzir ou escolhe-se o 'quão fidedigno' estes novos dados 
devem ser com relação aos dados completos (variância explicada).

### Seleção de Variáveis (*Features*)

- A seleção pode ocorrer por correlação (as variáveis selecionadas devem possuir correlação forte com a variável que se 
deseja prever), completude (as variáveis selecionadas devem possuir poucos valores faltantes) e variância.

- *Recursive Feature Elimination* (RFE): Dado um estimador externo que atribui pesos aos recursos (*features*), o 
objetivo da eliminação recursiva de recursos (RFE) é selecionar recursos considerando recursivamente conjuntos 
de recursos cada vez menores. Primeiro, o estimador é treinado no conjunto inicial de recursos e a importância 
de cada recurso é obtida através de um atributo atributo `feature_importances`. Em seguida, os recursos menos 
importantes são removidos do conjunto atual de recursos. Esse procedimento é repetido recursivamente no conjunto
podado até que o número desejado de recursos a serem selecionados seja finalmente alcançado.

![](https://www.scikit-yb.org/en/latest/_images/rfecv_credit.png)

- Algoritmo de *Minimum Redundancy Maximum Relevance* (mRMR)


