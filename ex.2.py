'''Receba um endereço de e-mail, e faça um sistema que receba os dados do usuário.'''

email = (input('digite se email:')).strip()
nome = email.strip()

print('seu usuario é : {}'.format(nome[0:14]))
print('seu servidor é :{}'.format(nome[15:20]))

'''so funcina com o email 'marianapaulina@gmail.com' pois contei as letras so aprendi como separar nome com sobrenos  com aspaços fazendo uma lista não sei como separar um email todo junto ;-;'''
