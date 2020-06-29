# Semana 3 (Prática)

### Conceitos de Amostragem

- __Amostragem__: Processo de obtenção de amostras, que são uma pequena parte da população.

- __População__: Todos os membros de um grupo o qual queremos estudar.

- __Amostra__: Um pequeno grupo de membros pertencentes a uma população.

### Problemas Relacionados à Amostragem

- _Undercoverage Bias_: Este problema acontece quando se analisa poucas observações ou quando se omite segmentos
inteiros de uma população.

Exemplo: Conduzir uma pesquisa de satisfação de funcionários de um hospital durante o dia. Com isso, funcionários do 
turno noturno não foram contemplados na pesquisa.

- _Self-selection Bias_: Acontece quando as pessoas que se dispuseram a entrar na análise diferem muito da real 
população de estudo. 

Exemplo: Fazer uma pesquisa online sobre um time de futebol. Somente pessoas que já torcem para o time em questão 
responderam a esta pesquisa.

- _Health-users Bias_: Acontece quando retiramos uma amostra somente da parte mais sadia da população.

Exemplo: Realizar uma pesquisa sobre hábitos saudáveis em uma academia. Pessoas que frequentam academia provavelmente 
possuem hábitos mais saudáveis que a maioria da população.

- _Survivor Bias_: Consiste no erro lógico de nos concentrarmos em pessoas que sobreviveram a algum processo enquanto 
ignoramos aqueles que foram eliminados, devido a sua falta de visibilidade.

Exemplo: Ao realizar uma análise dos aviões que retornavam da guerra, ao invés de reforçar os locais mais atingidos,
o correto deveria ser reforçar os locais que menos receberam dano, uma vez que possivelmente quem recebeu dano nestes
locais não conseguiram voltar com vida.

### Tipos de Amostragem

- __Aleatória__: Retirar elementos aleatórios da população para formar a amostra.

- __Não Aleatória__: Retirar elementos não aleatórios da população para formar a amostra.

- __Estratificada Proporcional__: A amostra deverá obter camadas que possuam as mesmas proporções observadas na 
população.

Exemplo: Considere um conjunto com 1000 elementos, sendo 500 do estrato 1, 120 do estrato 2, 280 do estrato 3 e 
100 do estrato 4. Em uma amostragem estratificada proporcional, uma amostra com 100 elementos deve conter 50 elementos 
do estrato 1, 12 do estrato 2, 28 do estrato 3 e 10 do estrato 4 (proporcionalmente distribuida).

- __Estratificada Uniforme__: Atribuir o mesmo tamanho de amostra para todos as camadas, independentemente do peso 
dos estratos da população. 

Exemplo: Considere um conjunto com 1000 elementos, sendo 500 do estrato 1, 120 do estrato 2, 280 do estrato 3 e 
100 do estrato 4. Em uma amostragem estratificada uniforme, uma amostra com 100 elementos deve conter 25 elementos do 
estrato 1, 25 elementos do estrato 2, 25 elementos do estrato 3 e 25 elementos do estrato 4 (uniformemente distribuida).

### Probabilidades

- Variam de 0 (impossível de acontecer) à 1 (certo de acontecer);
- A soma de todas as probabilidades devem resultar em 1;
- A distribuição relaciona x com a probabilidade p(x);
- Podem ser funções discretas ou contínuas.

Exemplo: Qual a probabilidade de obter cara jogando uma moeda (justa) para cima? (Discreta)
Exemplo: Qual a probabilidade de uma pessoa tirar uma nota acima da média no Enem (Contínua)

### Distribuição Normal (Gausiana)

- A área sob esta curva determina a probabilidade de ocorrer o evento por ela correlacionado;
- A soma da área sob a curva de densidade é igual a 1;
- É uma curva simétrica em torno do seu ponto médio, apresentando assim seu famoso formato de sino;
- A média, mediana e moda dos seus dados possuem o mesmo valor;
- É uma distribuição de variáveis contínuas.

![](http://www.portalaction.com.br/sites/default/files/EstatisticaBasica/figuras/distribuicaoNormal/normal3.PNG)

### Distribuição Binomial

- Espaço amostral finito;
- Apenas dois resultados possíveis (sucesso e fracasso, 0 e 1);
- Todos os elementos devem possuir possibilidades iguais de ocorrência;
- É uma distribuição de variáveis discretas (inteiros e contáveis).

Exemplo: Jogar uma moeda/dado.

![](https://mathbitsnotebook.com/Geometry/Probability/BD3x.jpg)

### Função Densidade de Probabilidade (PDF)

- Descreve a probabilidade __relativa__ de uma variável aleatória tomar um __valor dado__;
- É sempre não negativa;
- Sua integral sobre o espaço é igual a 1;
- Informa a probabilidade de uma variável x assumir um valor naquele intervalo.

### Função de Distribuição Acumulada (CDF)

- Descreve a probabilidade __acumulada__ de uma variável aleatória tomar um __conjunto de valores dado__;
- É sempre não negativa;
- Sua integral sobre o espaço é igual a 1;
- Informa a probabilidade de uma variável x assumir um valor naquele intervalo.

![](https://i.pinimg.com/originals/50/ee/86/50ee86d23bbac398871545435fc5b690.jpg)

### Função Distribuição Acumulada Empírica (ECDF)

- Um estimador da função de distribuição acumulada;
- Modelo EMPÍRICO;
- Funciona com suas observações.