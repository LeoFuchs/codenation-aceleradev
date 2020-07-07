# Semana 5 (Prática)

### Pesquisa Científica

- Pesquisa: Procedimento racional e sistemático que tem por objetivo proporcionar respostas aos problemas que são 
propostos. A pesquisa é desenvolvida mediante o concurso dos conhecimentos disponíveis e a utilização cuidadosa de 
métodos, técnicas e outros procedimentos científicos.

- Problema Científico: Questão não resolvida e que é objeto de discussão, em qualquer domínio do conhecimento.

- Características do Problema Científico: Formulado como pergunta, claro e preciso, empírico, suscetível de solução e
deve ser delimitado a uma dimensão viável.

### Hipóteses

A pesquisa científica se inicia com a colocação de um problema solucionável. O passo seguinte consiste em oferecer uma
solução possível, mediante uma proposição, ou seja, uma expressão verbal suscetível de ser declarada verdadeira ou
falsa. A essa proposição dá-se o nome de *hipótese*. Assim, a hipótese é a proposição verificável que pode vir a ser
a solução do problema.

Com frequência, pesquisadores elaboram extensa relação de hipóteses e depois de detida análise descartam a maior parte
delas. Além disso, nem todas as hipóteses são testáveis ou verificáveis. Para que uma hipótese possa ser considerada
logicamente aceitável, ela deve apresentar algumas características: deve ser conceitualmente clara, tendo referências
empíricas, parcimoniosas, estar relacionada com as técnicas disponíveis e deve estar relacionada com uma teoria.

### Teorema do Limite Central

O Teorema do Limite Central aponta que a distribuição das médias retiradas de uma amostra cuja população tenha qualquer
distribuição terão uma distribuição normal. [Video Explicando](https://www.youtube.com/watch?v=YAlJCEDH2uY)


### Teste Estatístico (Teste de Hipótese)

Permite a tomada de decisão entre duas ou mais hipóteses. Define-se a hipótese nula (H0) e uma ou mais hipóteses
alternativas (H1, H2, ..., HN). H0 é então assumida como verdadeira, o que se quer realmente testar. Enquanto HN é
considerada quando H0 é falso (não possui relevância estatística).

![](https://www.simplypsychology.org/type-1-and-2-errors.jpg)

### P-Valor

- Probabilidade de obter uma estatística de teste *igual ou superior* que a observada em uma amostra para H0.
- Quanto menor o P-valor, maior a chance de se rejeitar a hipótese nula (H0).
- Define-se o alfa (nivel de significância) antes do experimento. O comum é utilizar o alfa de 0.05 (5%).

![](http://www.portalaction.com.br/sites/default/files/inferencia/figuras/introducao/pvalor_bilateral_exem.png)

### Tipos de Testes de Hipótese

1. *T-test (Student T-test)*: Baseia-se na distribuição t de Student, uma distribuição simétrica, semelhante à curva normal
mas com um grau de liberdade.

    A ideia então para comparar dois grupos é utilizar a média entre os valores, o desvio padrão e a variância.

2. *Shapiro-Wilk*: Trata-se de um teste de normalidade. Utiliza uma amostra da população para validar se a mesma está
distribuida normalmente. Calcula-se utilizando variância, média e desvio padrão. 

    H0: Amostra provém de uma normal;
    H1: Amostra não provém de uma normal.
    
    Observação: Não funciona muito bem para amostras maiores que 5000.

3. *Jarque-Bera*: Trata-se de outro teste de normalidade. Neste caso, ele valida se existe desvio padrão. Utiliza 
curtose e assimetria.

    H0: Amostra provém de uma normal;
    H1: Amostra não provém de uma normal.

4. *Gráfico Q-Q (QQ-Plot)*: Conhecido também como gráfico de Quantil-Quantil (Quartil-Quartil). Compara a distribuição
de duas probabilidades entre variáveis ou entre uma variável e "quartis teóricos". Este teste ajuda a validar se uma
distribuição é normal.

![](https://marcoarmello.files.wordpress.com/2012/05/teste-estatistico-marco-mello.001.png)