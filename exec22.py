# Um programa que leia o nome completo de uma pessoa e mostre:
#nome com todas as letras maiusculas, todas as letras minusculas, quantas letras tem, e quantas
#letras no primeiro nome
nome=str(input('Digite seu nome completo: ')).strip()
dividido=nome.split()
print('O nome com todas as letras maísculas: {}'.format(nome.upper()))
print('O nome com todas as letras minusculas: {}'.format(nome.lower()))
print('Ao todo o nome possuí {} letras'.format(len(nome)- nome.count(' ')))
print('O primeiro nome possuí {} letras'.format(len(dividido[0])))

