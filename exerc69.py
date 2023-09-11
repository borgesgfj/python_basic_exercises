# cadastrar pessoas: ler idade, sexo. A cada pessoa cadastrada o programa pergunta se quer continuar.
# No final mostrar a) quantas pessoas tem mais de 18 anos; b) quantos homens; c) quantas mulheres < 20 anos.
print('\033[1;31m=-\033[m'*30)
print('{: ^70}'.format('\033[1;30;107m Cadastro de pessoas \033[m'))
print('\033[1;31m=-\033[m'*30)
c_h = c_m = c_maior = 0
while True:
    print('\033[35m--\033[m'*30)
    print('{: ^50}'.format('\033[1;34mCadastre uma pessoa\033[m'))
    print('\033[35m--\033[m' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        c_maior += 1
    if sexo in 'Mm':
        c_h +=1
    if sexo == 'F' and idade < 20:
        c_m += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^100}'.format('\033[1;32m FIM DO CADASTRAMENTO \033[m'))
print(f'\033[34mTotal de pessoas com mais de 18 anos: {c_maior}\033[m')
print(f'\033[32mAo todo temos {c_h} homens cadastrados\033[m')
print(f'\033[33mE temos {c_m} mulheres com menos de 20 anos\033[m')
