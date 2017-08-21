# victory
Victory é um complemento do Behave para facilitar o teste de APIs Restful

Recursos previstos:
* Classe que abstrai chamadas a API
* Suporte a variáveis
* Steps genéricos para envio de dados, recepção, listas, ...
* Poder manter dados entre diferentes cenários
* Estrutura de diretório e arquivos pronta para ser clonada

Dúvidas:
* Qual API usar como exemplo?
  * GitHub? https://developer.github.com/v3/

Futuramente:
* Integração pymix

Ideias
* Nos testes, poderíamos ter uma tabela única de dados, que poderia ser definida no início do feature e utilizada por todo ele. Esta tabela teria os dados a serem utilizados na inserção de dados. Cada cenário poderia alterar/excluir dados e a tabela poderia ser utilizada em gets, lists, ... Poderíamos ter filtros nas listagens para ignorar excluídos, etc e tal. Enfim, a ideia de usar esta tabela seria para evitar aquelas listagens repetitivas.
