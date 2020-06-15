[![N|Solid](https://miro.medium.com/max/425/1*05vDjNRMACek8hWh1pnltA.png)](https://www.codenation.dev/)
# Conteúdos Opcionais
Nesta sessão detalharemos o que foi aprendido durante o AceleraDev em Data Science da Codenation na aba denominada como "Conteúdos Opcionais".

### 1. Princípios de Reprodutibilidade

**Reprodutibilidade**: Capacidade de reproduzir uma análise ou experimento de forma consistente em um momento futuro, dispondo dos mesmos dados e ferramentas.

Isto não significa que o resultado afirmado é correto, apenas que ele é condizente com o experimento realizado. É uma condição **necessária**, mas *não suficiente** para a credibilidade da análise.

### 2. Ambiente de Trabalho em Python

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html): Literalmente um mini conda, possuindo o conda e mais outras bibliotecas interessantes para o desenvolvimento em Python.
- Virtualenv: Criar um ambiente virtual específico para o seu projeto, não sendo necessário manipular sempre as versões das bibliotecas. 
Para criar o ambiente, vá até a pasta do projeto e utilize o comando `virtualenv venv`. Em seguida, com a pasta _venv_ criada, execute o comando **`source venv/bin/activate`**. Para desativar o ambiente virtual, execute o comando `deactivate`. 
A partir do momento que você estiver com o ambiente virtual _venv_ ativado, tudo que for instalado com o comando `pip install` será instalado apenas no ambiente virtual.
Para saber quais as versões das bibliotecas que o projeto está trabalhando, execute o comando `pip freeze`. Para passar estas informações para um arquivo, complemente o comando com `pip freeze > requirements.txt`. Para instalar em outro local as bibliotecas do arquivo _requirements.txt_, utilize o comando `pip install -r requirements.txt`.
- Jupyter: Instale o Jupyter com o _venv_ ativado utilizando o comando `pip install jupyter`. Inicialize o Jupyter com o comando `jupyter notebook`. 

### 3. Git

![](https://miro.medium.com/max/1000/1*zw0bLFWkaAP2QPfhxkoDEA.png)

**Working Directory**: Área acessível ao usuário para trabalhar e realizar modificações (sendbox).
**Staging Directory**: Propostas de modificações salvas no próximo _commit_.
**Repositório Local**: Todo histórico salvo do projeto.

#### Configurando o Usuário
O Git mantém informações sobre todo o histórico, incluindo quem fez o que, para isso, ele vai pedir que você se identifique.
```
$ git config user.name "Meu Nome"
$ git config user.email "meuemail@email.com"
$ git config core.editor vim
```
Todas estas configurações ficam salvas em `~/.gitconfig`.

#### Inicializando um Repositório
Se você estiver iniciando um projeto novo, é possível configurar o diretório do projeto no Git com o comando:
```
$ git init
```
Se o projeto já existir em algum outro repositório, você não precisa inicializá-lo.

#### Clonando um Repositório
Se o projeto já existir em um repositório remoto, você pode clonar todo seu histórico localmente para trabalhar:
```
$ git clone https://github.com/usuario/projeto.git # Usando HTTP
$ git clone git@github.com:usuario/projeto.git # Usando SSH
```
#### Conhecendo o Estado Atual
Uma das tarefas mais básicas e corriqueiras do Git é conhecer o estado atual do projeto local:
```
$ git status
```

#### Marcando Modificações para Serem Salvas
Para consolidar nossas modificações no projeto, devemos fazer o _commit_, mas antes precisamos dizer ao Git o que queremos salvar.
Supondo que quero salvar modificações em 3 arquivos chamados `ExpressaoBinaria.java`, `TestaExpressaoBinaria.java` e `ExpressaoXor.java`, o código seria:
```
$ cd src/expressoes/
$ git add ExpressaoBinaria.java TestaExpressaoBinaria.java ExpressaoXor.java
```
Ou podemos adicionar todo o código do projeto de uma vez com o comando:
```
$ git add .
```
#### Fazendo _Commit_ (_the lazy way_)
Finalmente podemos consolidar nossas modificações no histórico do projeto com o comando:
```
$ git commit -m "Mensagem Título do Commit"
```

#### Fazendo _Commit_ (_the right way_)
Melhor prática é dar uma descrição mais completa do _commit_. Utilize o comando:
```
$ git commit
```
Este comando faz abrir o editor de texto configurado para escrever a mensagem do _commit_ (`git config core.editor vim`).
A primeira linha do arquivo é o Título. Começe com letra maiúscula, tente manter em 50 caracteres e não termine com ponto final. Em seguida, deixe uma linha em branco. A partir da terceira linha, coloque uma descrição detalhada do _commit_, tente manter cada linha com 72 caracteres e explique o porque das modificações feitas, e não o como.

#### Branches 
Branches (ramificações) são uma das _features_ mais especiais do Git. Elas permitem que você trabalhe em uma linha do histórico diferente da linha "principal" do projeto, sem impactar a linha "principal". 

- HEAD é o ponteiro para a referência ao _branch_ atual (onde eu realmente me encontro no projeto, o código que estou mudando).
- master é o _branch_ default criado pelo Git.

![](https://res.cloudinary.com/practicaldev/image/fetch/s--Jc-acrrl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/69payngupg75rqgabwdg.png)

Para criar um novo _branch_, podemos utilizar o código:
```
$ git branch novo-branch
$ git checkout novo-branch # Altera o HEAD para o branch que criei
```
Isso cria um novo _branch_ apontando para o _commit_ que o _branch_ master está apontando e seta HEAD para apontar para ele

#### Trabalhando em _Branches_
Após fazermos algumas modificações no código do novo _branch_, podemos criar um _commit_ nele normalmente. Enquanto isso, a referência do _branch_ master permanece inalterada.
Podemos continuar trabalhando no nosso novo-branch enquanto o _branch_ master pode ser manipulado paralelamente, como apresentado na figura acima.

#### Juntando com o _Branch_ Principal: merge
Em algum ponto do desenvolvimento, iremos querer juntar nosso trabalho no novo-branch com o _branch_ master, que pode ou não ter avançado nesse tempo. Para juntarmos o código, a forma padrão é utilizar o `git merge`.
Primeiro, devemos mover o HEAD para apontar para o master com `git checkout`. Em seguida, juntamos o código do novo-branch com o do master. Isto é feito com os comandos:
```
$ git checkout master
$ git merge novo-branch
```

#### O processo do merge
Problemas com merge podem (e provavelmente vão) acontecer. Alguns conflitos comuns são:
- O seu branch e o branch que será unido ("mergeado") possuem cópias conflitantes do mesmo arquivo.
- Neste caso, o Git pausa o merge, pede para você resolver os conflitos, commitar novamente os arquivos e então finaliza o processo de merge.

Depois de finalizado, o merge produz um novo _commit_, unindo as árvores dos dois _branches_. Depois de finalizado, o _branch_ mergeado pode ser deletado, utilizando o comando:
```
$ git branch -d novo-branch
```

#### Comandos Úteis para Branch
- Para mudar de _branch_ (atualizar o HEAD para outro _branch_): `git checkout outro-branch`
- Para listar _branches_ locais: `git branch -vv`
- Para deletar um _branch_ mergeado: `git branch -d nome_branch`
- Para deletar um _branch_ não mergeado (cuidado): `git branch -D nome_branch`
- Para renomear um _branch_: `git branch -m antigo-nome novo-nome`
- Para mergear branch1 e branch2: `git checkout branch2` e `git merge branch1


#### Configurando Repositórios Remotos
- Repositórios remotos são identificados localmente por um nome. Geralmente, usamos o nome _origin_ para o remoto original.
- Se o projeto já existe em algum remoto, podemos cloná-lo como vimos antes. O Git copiará todo o projeto remoto e identificará esse remoto como _origin_.
- Podemos adicionar remotos para nossos projetos locais com o comando: `git remote add origin https://github.com/usuario/repositorio.git`
- Podemos mudar o endereço de um remoto já configurado com o comando: `git remote set-url origin https://github.com/usuario/novo_repositorio.git`
- Podemos remover remotos com o comando: `git remote remove origin`
- Podemos ter uma visão geral do remoto com o comando: `git remote show origin`
- Podemos listar também todos os remotos configurados com o comando: `git remote -v`

#### Buscando o Estado do Remoto
A primeira tarefa básica é buscar o estado dos remotos com o comando `git fetch -all` ou de um remoto específico `git fetch origin`.
Observação: O comando `git fetch` busca todo o estado do remoto e o guarda localmente, mas __não__ aplica nenhuma modificação.

#### Aplicando Modificações do Remoto
Para aplicar as modificações de um remoto localmente, utilizamos o merge, como no código abaixo:
```
$ git checkout master
$ git fetch --all
$ git merge origin/master 
```
Um outro método de escrever este código é com o pull, como no código abaixo:
```
$ git checkout master
$ git pull origin master
```
Observação: Problemas de conflito podem surgir e precisam ser resolvidos. Sendo assim, é indicado aplicar as modificações com fetch + merge em vez do pull para se ter mais controle do que está acontecendo.

#### Subindo Modificações para o Remoto
O processo contrário do anterior é subir nossas modificações locais para o remoto com `git push`, como no código:
```
$ git push origin master
```
Se o _branch_ local e remoto divergirem, o Git não permitirá o push até que eles estejam sincronizados localmente.

#### Trabalhando com Branch Remoto
_Branches_ remotos são identificados localmente como __<remoto>/<branch>__. Por exemplo, __origin/master__ denota o branch _master_ do repositório remoto _origin_.
- Para listar todos os _branches_ remotos utilize o comando: `git branch -r`
- Podemos criar um branch local diretamente a partir de um branch do remoto com o comando: `git checkout branch-remoto`
- Ou criá-lo com um nome diferente localmente com o comando: `git checkout -b nome-local origin/branch-remoto`
- É possível subir o seu _branch_ local com um nome diferente no remoto com o comando: `git push origin branch-local branch-remoto`
- Por fim, para remover um _branch_ remoto, utilize o comando: `git push origin --delete branch-remoto`.

#### Trackeando um _Branch_ Remoto
- É possível configurar um _branch_ local para "trackear" um _branch_ do remoto com os comandos: `git checkout branch-local` e `git branch -u nome-do-remoto/branch-remoto`.
__Observação__: Se o _branch_ local foi criado diretamente a partir do _branch_ remoto, então ele já está trackeando automaticamente. 
- Existe um atalho para o _branch_ remoto trackeado: @{u}. Com isso, operações ficam mais simples quando o _branch_ remoto é trackeado (`git merge @{u}`). 
- Você também pode verificar quais _branches_ estão sendo trackeados com o comando `git branch -vv`.

#### Links Interessantes para Git

- Documentação oficial: https://git-scm.com/docs/
- Uma das melhores introduções ao Git: https://git-scm.com/book/en/
- Tutoriais da Atlassian: https://www.atlassian.com/git/tutorials/

### 4. Clean Code
- PEP8 Original: https://www.python.org/dev/peps/pep-0008/
- PEP8: Guia de Estilo em Português: https://wiki.python.org.br/GuiaDeEstilo













