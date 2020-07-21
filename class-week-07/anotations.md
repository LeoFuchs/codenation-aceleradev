# Semana 7 (Teórico)

## Engenharia de Features 

### Variáveis Categóricas

- Não possuem aplicação matemática (simplesmente categorizam as entradas);
- Costumam ser algum tipo de classificador ou agrupador;
- Possui um limite de valores (Exemplo: baixo, médio ou alto)
- Técnicas de Encode: _Label Encode_ e _One Hot Encode_.

![](https://miro.medium.com/max/1200/0*T5jaa2othYfXZX9W.)

Observação: Label Encoding é perigoso pois o modelo pode interpretar os valores das features
como pesos, o que nem sempre é verdade (Apple não é menos relevante que Broccoli)

### Binarização

- Transformar valores escalares em binários;
- Por padrão, tudo que é positivo recebe o valor 1.
- Boa prática é normalizar/padronizar os valores.

### Quantização (_Binning_)

- Separa as amostras em quantis de quantidades iguais;
- _bins_: Quantidade de "separações";
- Permite o agrupamento e a criação de _ranges_.
- Utilizado para gerar categorias dentro de variáveis numéricas (_cut()_)

### Variáveis Numéricas

- StandardScaler
- Z-Score (X - Média / Desvio Padrão)

- MinMaxScaler
- X_scaler = X_std * (Máximo - Minímo) + Mínimo

### Normalização, Escala e Transformação

- Aplicação de técnicas de normalização dos dados, de forma automática.
- Preenchimento de valores faltantes, aplicação de padronização e normalização e transformação de colunas, por valores
ou encode.
- O agrupamento permite a criação de _pipelines_.
- Reaproveitamento dos cálculos, aplicação simultânea.

![](https://miro.medium.com/max/1356/1*87x5Ef-nxSx2Gsp17zxQlg.png)

### Remoção de Outliers

- Procurando por Outliers
- IQR: Menores que o Q1 e Maiores que o Q3 
(Fórmula Abaixo que [Q1 - 1.5 x IQR] e Acima que [Q3 + 1.5 x IQR] onde IQR = Q3 - Q1)

![](https://www.whatissixsigma.net/wp-content/uploads/2015/07/Box-Plot-Diagram-to-identify-Outliers-figure-1.png)

### Features de Texto

- Categóricas por padrão;
- TF-IDF
- TF (Frequência do Termo): O peso de um termo que ocorre em um documento é diretamente proporcional à sua frequência.
- IDF (Inverso da Frequência do Documento): A especificidade de um termo pode ser quantificada por uma função inversa 
ao número de documentos em que ele ocorre.

- Agrupamento de termos, ordenação;
- N-gram: Agrupamento de 2 ou mais palavras, onde a partir deste agrupamento passam a ser tratadas com 1 elemento único.
- Stop-words: Palavras ou composições que não impactam em valor e entendimento.