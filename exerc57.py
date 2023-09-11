#programa que leia o sexo de uma pessoa, só aceite m ou f caso esteja errado peça a digitação novamente
sexo = ''
while sexo != 'M' and sexo != 'F' and sexo != 'NB':
    sexo = str(input('Digite o seu sexo [Maculino (M)/Feminino (F)/Não-binário[NB]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F' and sexo != 'NB':
        print('Opção inválida! Digite novamente.')
    else:
        print('Sexo Validado.')
