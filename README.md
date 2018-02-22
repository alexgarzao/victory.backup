# victory
Victory é um complemento do Behave para facilitar o teste de APIs Restful

## Como utilizar
-- Terminal 1 (baixa API de exemplo com seus testes)
cd <DIR>
git clone https://github.com/alexgarzao/victory-api-example.git
cd victory-api-example/api
virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
make run

-- Terminal 2 (baixa victory)
cd <DIR>
git clone https://github.com/alexgarzao/victory.git
cd victory
virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
make FEATURES_PATH=/home/alexgarzao/temp/victory-api-example/bdd/ all

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
