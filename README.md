# victory
Victory é um complemento do Behave para facilitar o teste de APIs Restful.

## Como utilizar
Para poder testar o "Hello world" do Victory, existe um projeto de exemplo.
No exemplo abaixo são necessários 2 terminais para executar o teste: o terminal 1, onde será executada a API de exemplo, e o terminal 2, onde serão executados os testes com o Victory.

Vamos assumir que `<DIR>` contém o diretório onde o exemplo e o Victory serão baixados.
 
```
# Terminal 1
cd <DIR>
git clone https://github.com/alexgarzao/victory-api-example.git
cd victory-api-example/api
virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
make run

# Terminal 2
cd <DIR>
git clone https://github.com/alexgarzao/victory.git
cd victory
virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
make FEATURES_PATH=<DIR>/victory-api-example/bdd/ all
```

Victory assume que, no PATH indicado (FEATURES_PATH) vai existir:
- um arquivo chamado 'sequence.featureset', contendo a ordem de execução dos testes
- um diretório, com o nome 'custom_steps', contendo os steps específicos da API a ser testada

Em relação a localização das funcionalidades a serem validadas (arquivos .feature), o Victory no assume nomes ou localizações específicas. Mas, como sugestão, tente organizar os arquivos em pastas, onde cada pasta contém os testes relativos a uma funcionalidade.

## Recursos previstos
* Classe que abstrai chamadas a API
* Suporte a variáveis
* Steps genéricos para
  * enviar dados
  * validar dados
  * listas
  * ...
* Poder manter dados entre diferentes cenários
* Estrutura de diretório e arquivos pronta para ser clonada

## Dúvidas
* Qual API usar como exemplo?
  * GitHub? https://developer.github.com/v3/

## Futuramente
* Integração pymix

## Ideias
* Nos testes, poderíamos ter uma tabela única de dados, que poderia ser definida no início do feature e utilizada por todo ele. Esta tabela teria os dados a serem utilizados na inserção de dados. Cada cenário poderia alterar/excluir dados e a tabela poderia ser utilizada em gets, lists, ... Poderíamos ter filtros nas listagens para ignorar excluídos, etc e tal. Enfim, a ideia de usar esta tabela seria para evitar aquelas listagens repetitivas.
