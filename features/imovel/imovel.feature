Funcionalidade: Cadastro de imóveis.

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário quero listar meus imóveis cadastrados.
    Dado que eu quero listar os meus imóveis
    Quando eu busco a lista de imóveis
    Então eu recebo o status que indica requisição válida
    E obtenho uma lista vazia

  Esquema do Cenário: Como usuário quero cadastrar imóveis com dados válidos.
    Dado que eu quero cadastrar um imóvel
    E o campo nome do proprietário é <nome do proprietário>
    E o campo características do imóvel é <características>
    E o campo endereço do imóvel é <endereço>
    E o campo valor do imóvel é <valor>
    E o campo está ocupado é <está ocupado>
    Quando eu tento cadastrar o imóvel
    Então eu recebo o status que indica imóvel criado com sucesso

    Exemplos: Dados válidos para imóveis.
      | nome do proprietário | está ocupado | características | endereço                             | valor  |
      | Proprietário 01      | sim          | A,B,C,D         | Rua A Porto Alegre Rio Grande do Sul | 1000.0 |
      | Proprietário 02      | nao          | <nulo>          | Rua B Porto Alegre Rio Grande do Sul | 2000.0 |

  Cenário: Como usuário quero listar meus imóveis cadastrados.
    Dado que eu quero listar os meus imóveis
    Quando eu busco a lista de imóveis
    Então eu recebo o status que indica requisição válida
    E obtenho a lista de dados abaixo
    | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
    | Proprietário 01      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
    | Proprietário 02      | não          | <nulo>                    | Rua B Porto Alegre Rio Grande do Sul | 2000.0          |


  # Cenário: Como usuário quero listar meus imóveis cadastrados (dados errados).
  #   Dado que eu quero listar os meus imóveis
  #   Quando eu busco a lista de imóveis
  #   Então eu recebo o status que indica requisição válida
  #   E obtenho a lista de dados abaixo
  #   | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
  #   | Proprietário 08      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
  #   | Proprietário 02      | não          | <nulo>                    | Rua C Porto Alegre Rio Grande do Sul | 2000.0          |


    # | nome do proprietário | data de cadastro | está ocupado | características | endereço                             | valor   |
    # | Proprietário 01      | <nao nulo>       | sim          | 1,2,3,4         | Rua A Porto Alegre Rio Grande do Sul | 1000.00 |
    # | Proprietário 02      | <nao nulo>       | nao          | <nulo>          | Rua B Porto Alegre Rio Grande do Sul | 2000.00 |
