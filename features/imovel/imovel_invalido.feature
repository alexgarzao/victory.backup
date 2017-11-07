Funcionalidade: Cadastro de imóveis com dados inválidos.

  Esquema do Cenário: Como usuário tento cadastrar imóveis com dados inválidos.
    Dado que eu quero cadastrar um imóvel
    E o campo nome do proprietário é <nome>
    E o campo caracteristíscas do imóvel é <caracteristicas>
    E o campo endereço do imóvel é <endereco>
    E o campo valor do imóvel é <valor>
    E o campo está ocupado é <está ocupado>
    Quando eu tento cadastrar o imóvel
    Então eu recebo o código que indica requisição inválida
    Exemplos: Dados inválidos para imóveis.
      | nome   | está ocupado | caracteristicas | endereco | valor  |
      | <nulo> | <nulo>       | <nulo>          | <nulo>   | <nulo> |
