# outra maneira de fazer. usando not in ''
sexo = str(input('Digite seu sexo [Masculino(M)/ Feminino(F)/ Não binário(NB)] ')).strip().upper()
while sexo not in 'MFNB':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: [Masculino(M)/ Feminino(F)/ Não binário(NB)] ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))

