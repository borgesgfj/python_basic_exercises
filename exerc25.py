#Digite o nome de uma pessoa e diga se existe Silva no nome.
nom=str(input('Digite seu nome completo: ')).strip()
print('\033[1;43;97Tem "Silva" em seu nome? \033[m')
print('R: {}{}{}'.format('\033[1;31m', 'silva' in nom.lower(), '\033[m'))
print('\033[4;1;30;107mSe a resposta for True existe Silva no nome, caso seja False não existe\033[m')