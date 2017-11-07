Funcionalidade: Login.

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário tento me logar com uma senha inválida.
    Dado que eu quero executar o login
    E o campo usuário é usuario@usuario.com
    E o campo senha é 'senha invalida'
    Quando eu tento executar o login
    Então eu recebo o status que indica login inválido
