# Semana 3 (Prática)

### Análise de Exploratória Exploratório (EDA)

- Definição: "Procedimentos para analisar dados, técnicas para interpretar os resultados de 
tais procedimentos, formas de planejar a reunião dos dados para tornar sua análise mais fácil, mais precisa ou mais
exata e toda a maquinaria e os resultados da estatística (matemática) que se aplicam a análise de dados." John W. Tukey

- Sugerir __hipóteses__ sobre as causas dos fenômenos observados;
- Avaliar __pressupostos__ sobre os quais a inferência estatística se baseará;
- Apoiar a seleção de ferramentas e técnicas estatísticas apropriadas;
- Oferecer uma base para coleta posterior de dados por meio de pesquisas e experimentos.

### Estatística Descritiva Univariada 

Em outras palavras, é o conceito de se analisar uma variável separadamente.

- __Média__ _(Mean/Average)_: Ponto central de um conjunto de informações definido pela somatória das informações de um
conjunto dividido pela quantidade de informações. 

Fórmula: __Média = SUM(valores) / COUNT(valores)__

Exemplo: [10, 20, 20, 12, 13, 20, 21, 25] - Média = 17.62

- __Mediana__ _(Median)_: Valor que separa a metade das informações em __2 conjuntos de mesma quantidade__. Para
conjuntos de quantidade par, a média dos dois valores centrais.

Exemplo: [1, 3, 3, 6, 7, 8, 9] - Mediana = 6

- __Quartis__: Divide os dados em 4 conjuntos de dados, com 25% em cada conjunto.
- __Percentis__: Divide os dados em 100 partes do todo, com 1% acumulado em cada segmento.

![](https://aprendendogestao.com.br/wp-content/uploads/2016/07/QE-Figura-1.png)

- __Amplitude Interquartil__ _(Interquartile Range) (IQR)_: O 50% central dos valores quando ordenados do menor para o
maior. Em outras palavras, encontra-se a mediana da menor e da maior metade dos dados. Estes valores são o Quartil 1 
(Q1) e o Quartil 3 (Q3). A Amplitude Interquartil é então a diferença entre Q3 e Q1.

![](https://i2.wp.com/makemeanalyst.com/wp-content/uploads/2017/05/IQR-1.png?resize=431%2C460)

Exemplo: Dado os valores [62, 63, 64, 70, 72, 76, 77, 81, 81], determine qual é a Amplitude Interquartil?

![](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_summarizingdata/Interquartile-Odd.png)

- __Desvio Padrão__ _(Standard Deviation (STD))_: Medida que expressa o grau de dispersão de um conjunto de dados.
Em outras palavras, indica o quanto um conjunto de dados é uniforme. Ou seja, quanto mais próximo de zero for o desvio
padrão, mais homogêneo são os dados.

![](https://images.educamaisbrasil.com.br/content/banco_de_imagens/guia-de-estudo/D/desvio-padrao-matematica.jpg)

Exemplo: Dado os valores [1.55, 1.70, 1.80], determine qual é o Desvio Padrão?

Primeiro, notamos que a média deste conjunto é 1.68 e que o numero de elementos é 3. Com isso, temos que: 

![](https://static.todamateria.com.br/upload/de/sv/desviopadraoexemplo1.jpg)

- __Assimetria__ _(Skewness)_: Grau de distorção da curva simétrica a distribuição normal. Em outras palavras, mede a
falta de simetria na distribuição dos dados. Uma distribuição simétrica teria então um _skewness_ de 0.

![](https://miro.medium.com/max/1200/1*nj-Ch3AUFmkd0JUSOW_bTQ.jpeg)

- __Curtose__ _(Kurtosis)_: Medida de dispersão que caracteriza o "achatamento" da curva em função da distribuição.
Existem alguns tipos de Curtose:

1. Mesócurtica _(Mesokurtic)_ [curtose = 0]: Achatamento como o da distribuição normal.

2. Leptocúrtica _(Leptokurtic)_ [curtose > 0]: Possui uma curva mais afunilada, com um pico mais alto que a 
distribuição normal e caudas pesadas.

3. Platicúrtica _(Platykurtic)_ [curtose < 0]: Mais achatado do que a distribuição normal.

![](http://www.portalaction.com.br/sites/default/files/resize/EstatisticaBasica/figuras/curtose1-700x304.png)

- __Normalização__ _(Normalization)_: A normalização tem como objetivo colocar todas as variáveis dentro do intervalo 
0 e 1, ou no intervalo -1 e 1, caso haja valores negativos. 

- __Padronização__ _(Standardization)_: A padronização por sua vez possui o objetivo de padronizar as variáveis, 
resultando em uma média igual a 0 e um desvio padrão igual a 1.

### Estatística Descritiva Bivariada/Multivariada

Em outras palavras, são amostras que possuem mais de uma variável e que se busca entender o relacionamento entre os 
pares ou o conjunto de variáveis. Este relacionamento pode ser notado através de: Tabulações cruzadas e tabelas de 
contingência, representações gráficas através de gráficos de dispersão, medidas quantitativas de dependência e 
descrições de distribuições condicionais. 

- __Correlação__ _(Correlation)_: Medida padronizada da relação entre duas variáveis. Em outras palavras, indica a 
força (forte ou fraca) e a direção do relacionamento (positiva ou negativa) entre duas variáveis. A correlação oscila
entre -1 e 1. Se o valor estiver próximo de 0, as variáveis não possuem correlação. Em uma correlação positiva, as
variáveis se movem juntas, ficando mais forte quando se aproxima de 1, enquanto na correlação negativa, as variáveis
se movem em direções opostas, ficando mais forte quando se aproxima de -1. Duas variáveis são perfeitamente 
correlacionadas quando possuem a correlação de 1 (perfeitamente positiva) ou -1 (perfeitamente negativa).  

__Observação__: Correlação não significa Causalidade!

- __Correlação de Spearman__: Avalia a relação __monotônica__ entre duas variáveis contínuas ou ordinais. 
Em uma relação monotônica (quando a correlação é crescente ou decrescente, ou estritamente crescente ou estritamente 
decrescente ou constante), as variáveis tendem a mudar juntas mas não necessariamente a uma taxa constante. O 
coeficiente de correlação de Spearman baseia-se nos valores classificados de cada variável, em vez dos dados brutos.
A correlação de Spearman é muito usada para avaliar relações envolvendo variáveis ordinais (que possuem ordem). Por 
exemplo, utilizar a correlação de Spearman para avaliar se a ordem na qual os funcionários executam um teste 
está relacionada ao número de meses de emprego.

__Observação__: Correlação de Spearman é menos sensível a _outliers_.

- __Correlação de Pearson__: Avalia a relação __linear__ entre duas variáveis contínuas. Uma relação é linear quando a 
mudança em uma variável é associada a uma mudança __proporcional__ na outra variável. Por exemplo, utilizar a 
correlação de Pearson para avaliar se aumentos na temperatura da instalação de produção estão associados a uma 
redução da espessura da cobertura de chocolate.

### Visualização dos Dados

- __Histograma__ _(Histogram)_: Possui a distribuição de frequências, com a representação gráfica feita em barras
verticais ou horizontais. Pode ser dividido em classes uniformes ou não uniformes, onde a base de cada retângulo 
representa uma classe específica e a sua altura representa a quantidade, a frequência absoluta ou a densidade da
frequência para classes não uniformes.

![](https://chartio.com/assets/27a327/tutorials/charts/histograms/bd0509cd76e528096e481e0a7078d9ddb4a8da50022f947fee4c461d0b40a1fb/histogram-example-1.png)

- __Diagrama de Caixas__ _(Box Plot)_: Ferramenta gráfica para representar a variação de dados observados de uma 
variável numérica por meio de quartis. A reta (_whisker_ ou fio de bigode) que se estende verticalmente ou 
horizontalmente a partir da caixa indica a variabilidade fora do quartil superior e inferior. Além disso, _outlires_
são tratados como pontos individuais após a reta.

![](https://www.gradusct.com.br/wp-content/uploads/2018/07/Boxplot-04.png)

- __Dispersão__ _(Scatter Plot)_: Representa duas (tipicamente) ou mais variáveis, utilizando coordenadas cartesianas
para exibir valores de um conjunto de dados. São exibidos como uma coleção de pontos, cada um com o valor de uma
variável.

![](https://www.r-graph-gallery.com/img/graph/13-scatter-plot2.png)

- __Matriz de Correlação__ _(Correlation Matrix)_: Uma tabela que apresenta a correlação entre valores de um conjunto
de dados.

![](https://vizerybusiness.files.wordpress.com/2019/01/cm1.png) 