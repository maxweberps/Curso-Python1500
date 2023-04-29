"""
1 - Crie um sistema de cadastro e login de um site, utilizando um username e
senha informados pelo usuário.
"""
login = False
print('Bem-vindo\n\n'
      '--Cadastro--')

usuario1 = input('Usuário: ')
senha1 = input('Senha: ')

print('\nCadastro realizado com sucesso!\n')

print('--Login--')
usuario2 = input('Digite seu usuário: ')
senha2 = input('Digite sua senha: ')

if usuario1 == usuario2 and senha1 == senha2:
      login = True
else:
      login = False

if login:
      print('\nUsuário logado com sucesso!')
else:
      print('\nUsuário ou senha incorreto!')


