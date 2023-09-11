#Leia o nome completo de uma pessoa e mostre o primeiro e o último nome de uma pessoa
nome=str(input('Digite seu nome: ')).strip()
dv=nome.split()
print('O primeiro nome é: {}'.format(dv[0]))
print('O último nome é: {}'.format(dv[(len(dv)-1)]))
