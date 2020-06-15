# Semana 1 (Teórica)

### Ementa Geral
- Semana 1: Introdução a Ciência de Dados
- Semana 2: Pré-processamento de Dados em Python
- Semana 3: Análise de Dados Exploratória
- Semana 4: Continuação da Análise de Dados Exploratória
- Semana 5: Pensamento Estatístico em Python
- Semana 6: Continuação do Pensamento Estatístico em Python
- Semana 7: Engenharia de Features
- Semana 8: Regressão
- Semana 9: Classificação

### Ciência de Dados
1. A profissão mais sexy do século XXI
2. Resolver problemas interdisciplinares
3. Foco no resultado (do negócio)
4. Utilizar métodos e metodologias científicas

### Big Data
Temos por definição os 5V's do Big Data que caracterizam do que se trata Big Data:
1. __Volume__: Big Data é uma grande quantidade de dados gerada a cada segundo. A tecnologia do Big Data serve para lidar com o grande volume de dados, guardando-os em diferentes localidades e juntando-os através de software.
2. __Velocidade__: Se refere à velocidade com que os dados são criados ou manipulados. O Big Data serve para analisar os dados no instante em que são criados, sem ter de armazená-los em bancos de dados.
3. __Variedade__: No passado, a maior parte dos dados era estruturada e podia ser colocada em tabelas e relações. Hoje, 80% dos dados do mundo não se comportam dessa forma. Com o Big Data, mensagens, fotos, vídeos e sons, que são dados não-estruturados, podem ser administrados juntamente com dados tradicionais.
4. __Veracidade__: Um dos pontos mais importantes de qualquer informação é que ela seja verdadeira. Com o Big Data não é possível controlar cada hashtag do Twitter ou notícia falsa na internet, mas com análises e estatísticas de grandes volumes de dados é possível compensar as informações incorretas.
5. __Valor__: O último V é o que torna Big Data relevante: tudo bem ter acesso a uma quantidade massiva de informação a cada segundo, mas isso não adianta nada se não puder gerar valor. É importante que empresas entrem no negócio do Big Data, mas é sempre importante lembrar dos custos e benefícios e tentar agregar valor ao que se está fazendo.

### Governança de Dados (José Carlos Barbieri)
- Para onde vou (em termos de negócios), como vou e quando vou?
- Que dados serão necessários nesse caminho?
- Como obtê-los e mantê-los?
- Que áreas serão prioritárias no tratamento dos dados, baseando nas estratégias de negócios?

### Tipos de Análises
1 - __Análises Descritivas__: A análise exploratória ou descritiva é um dos primeiros níveis de tratamento de informações. Como o nome indica, ela procura compreender qual é o cenário da empresa ou da situação analisada, por meio de algumas ferramentas. É o método mais simples de conhecer o que está por trás das informações. É possível verificar o volume de vendas do negócio em cada área coberta, por exemplo.
Resumindo: Olha apenas para o __passado/atual__ (_"O que aconteceu?"_).

2 - __Análises Diagnósticas__: Quando uma pessoa vai a um médico, ele analisa os sintomas, pede exames e, a partir dos resultados, identifica se existe algum problema de saúde. Com a análise diagnóstica acontece de forma parecida. Por se tratar do segundo nível de avaliação das informações, exige que a abordagem descritiva tenha ocorrido previamente. Com o uso dos dados, o objetivo não é apenas compreender como está o cenário, mas o porquê de ele se configurar de tal maneira. Ao entender os motivos e as explicações, fica mais fácil obter insights sobre como é possível melhorar. 
Resumindo: Olha apenas para o __passado/atual__ (_"Porque isso aconteceu?"_).

3 - __Análises Preditivas__: As análises descritivas e diagnósticas ajudam a ter uma visão sobre o presente e o passado. Dá para compreender o comportamento em relação ao que já aconteceu e descobrir quais são os impactos do momento. A partir das análises preditivas, o período começa a ser outro. A intenção é verificar o que possivelmente acontecerá, de modo a antever e se preparar para o futuro. O principal mecanismo nesse sentido é a identificação e a análise de tendências. Não é porque o faturamento foi ampliado nos últimos anos que ele, necessariamente, continuará a aumentar. No entanto, se a indústria fez mudanças no target, é possível que a base de clientes continue a atrair pessoas com características distintas.
Resumindo: Utiliza o __passado__ para prever/predizer o __futuro__ (_"O que vai acontecer?"_").

4 - __Análise Prescritivas__: De volta à situação em que alguém vai a um médico, o diagnóstico é a fase inicial. Uma vez que o problema seja detectado, o especialista recomenda o tratamento, certo? Trata-se de uma analogia às análises prescritivas.
A partir do reconhecimento da situação com as análises descritivas e dos insights trazidos pelas diagnósticas e preditivas, é possível definir um plano de ação. Pense em uma indústria que tem uma marca mal posicionada entre os distribuidores. Eles não sabem como os produtos podem atingir seus respectivos públicos e por que deveriam recorrer a essa possibilidade. Para alavancar as vendas, a análise prescritiva pode prever a realização de ações de apresentação da atuação. Como resultado, a empresa pode reconhecer o que fazer para reverter o cenário desfavorável.
Resumindo: Utilizando uma predição/previsão do __futuro__ para recomendar uma ação (_"O que vou fazer?"_").

### Tipos de Problemas
1 - __Classificação Binária__: Preveem um resultado binário (uma de duas classes possíveis). Comumente utiliza-se regressão logística.

Exemplos: "Este e-mail é spam ou não?" / "O cliente comprará o produto?" / "Este produto foi feito por um humano ou um robô?"

2 - __Classificação Multiclasse__: Permitem gerar previsões para várias classes (prever entre mais de dois resultados). Comumente utiliza-se regressão logística multinominal.

Exemplos: "Este produto é um livro, um filme ou uma roupa?" / "Este filme é uma comédia, um documentário ou um romance?"

3 - __Regressão__: Preveem um valor numérico. Comumente utiliza-se regressão linear.

Exemplos: "Qual será a temperatura em São Paulo amanhã?" / "Quantas unidades deste produto serão vendidas?"

4 - __Clusterização/Agrupamento__: Modelo que consegue aprender grupos/divisões nos dados. Comumente utiliza-se o algoritmo KMeans.

Exemplos: "Quantos perfis de cliente minha empresa tem?" / "Quantos grupos de alunos possuem a minha classe?"

5 - __Sistemas de Recomendação__: Modelo sugere/recomenda algo ao usuário. Comumente utiliza-se _Collaborative Filtering/Content Based_.

Exemplos: "Qual filme recomendar à um usuário baseado em seu gosto?" / "Qual imóvel recomendar ao usuário comprar?"

### Tipos de Aprendizado

1 - __Aprendizado Supervisionado__: São apresentadas ao computador exemplos de entradas e saídas desejadas, fornecidas por um "professor". O objetivo é aprender uma regra geral que mapeia as entradas para as saídas.
Exemplo: Figuras do Tom e Jerry onde um conjunto de teste é passado já com rotulos informando quais das figuras são o Tom e quais são o Jerry. Assim, novas figuras sem o rótulo podem ser dadas como entrada para que se descubra se é o Tom ou o Jerry.

2 - __Aprendizado Não Supervisionado__: Nenhum tipo de etiqueta é informado. Encontrar estruturas nas estradas fornecidas sozinho. Pode ser um objetivo em si (descobrir novos padrões nos dados) ou um meio para atingir um fim.
Exemplo: Figuras do Tom e Jerry onde o conjunto de entrada não possui nenhuma rotulação e a saída são clusters de imagens semelhantes, para o Tom e para o Jerry.

### O Processo de Ciência de Dados

![](https://secureservercdn.net/160.153.137.170/uh6.338.myftpupload.com/wp-content/uploads/2019/05/modelling_evaluation.png?time=1591380037)

1: _Understand Business Problem_ (Entender o Problema do Negócio)
- Faça quantas perguntas forem necessário;
- Faça uma imersão no problema antes de pensar em uma solução.

2: _Define Analytical Problem_ (Defina o Problema Analiticamente) 
- Traduza a necessidade do negócio em uma solução de dados e planeje como entregá-la;
- Defina KPI's de negócio para avaliar o sucesso do modelo.

3: _Define Tech Architecture_ (Defina a Arquitetura Tecnologica)
- Defina quais tecnologias serão utilizadas para resolver o problema do negócio;
- Esclareça ao cliente o que vamos fazer.

4: _Data Understanding_ (Compreensão dos Dados)
- Explore as correlações entre as variáveis;
- Faça testes de hipóteses. 

5: _Data Processing_ (Processamento dos Dados)
- Seleção de _features_
- _Feature Engineering_

6: _Data Modelling_ (Modelagem dos Dados)
- Configure diferentes experiências e as melhores métricas;
- Encontre o modelo mais adequado para as necessidades do negócio.

7: _Evaluation_ (Avaliação)
- Realize a explicabilidade do modelo e a comunicação de resultados;
- Verifique a _performance_ em diferentes cenários.

8: _Deployment_ (Implantação)
- Implante o modelo na arquitetura do projeto;
- Assegure-se da qualidade da solução apresentada.

9: _Feedback_
- Faça testes A/B com o mundo real;
- Monitore métricas do modelo e KPI's do negócio.