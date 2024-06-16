"""
1 - Crie um sistema de cadastro e login de um site, utilizando um username e
senha informados pelo usuário.
"""
login = False
print('Bem-vindo\n\n'
      '--Cadastro--')

usuario = input('Usuário: ')
senha = input('Senha: ')

print('\nCadastro realizado com sucesso!\n')

print('--Login--')

if input('Usuário: ') == usuario and input('Senha: ') == senha:
    login = True
else:
    login = False

if login:
    print('\nUsuário logado com sucesso!')
else:
    print('\nUsuário ou senha incorreto!')
