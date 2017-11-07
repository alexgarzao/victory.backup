@setup
Funcionalidade: Setup do teste.

  Cenário: Definindo a URL base da API.
    Dado que eu quero definir a URL base da API
    Quando eu tento definir a URL base como http://localhost:5000/
    Então nenhuma falha ocorre

  Esquema do Cenário: Mapeando os campos do JSON.
    Dado que eu quero mapear os campos do JSON
    E o campo <nome> é do tipo <tipo> e corresponde ao <campo json> no JSON
    Quando eu tento mapear os campos
    Então nenhuma falha ocorre

    Exemplos: Campos do método de login.
      | nome          | tipo    | campo json |
      | id do usuário | integer | id_usuario |
      | usuário       | string  | usuario    |
      | email         | string  | email      |
      | senha         | string  | senha      |

    Exemplos: Campos do método de imóveis.
      | nome                      | tipo        | campo json      |
      | id do imóvel              | integer     | id_imovel       |
      | id do usuário             | integer     | id_usuario      |
      | endereço do imóvel        | string      | endereco        |
      | características do imóvel | string_list | caracteristicas |
      | nome do proprietário      | string      | proprietario    |
      | valor do imóvel           | number      | valor           |
      | está ocupado              | bool        | esta_ocupado    |
      | data de cadastro          | date        | data_cadastro   |

  Esquema do Cenário: Mapeando os códigos de retorno do HTTP.
    Dado que eu quero mapear os códigos de retorno do HTTP
    E o código <código> indica <status>
    Quando eu tento mapear os códigos de retorno
    Então nenhuma falha ocorre

    Exemplos: Códigos mapeados.
      | código | status                    |
      | 201    | elemento criado           |
      | 204    | elemento excluído         |
      | 200    | elemento atualizado       |
      | 200    | elemento obtido           |
      | 404    | elemento não encontrado   |
      | 404    | login inválido            |
      | 200    | login válido              |
      | 400    | requisição inválida       |
      | 200    | requisição válida         |
      | 200    | requisição ok             |
      | 201    | imóvel criado com sucesso |
