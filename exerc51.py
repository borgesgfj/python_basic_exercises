#Programa que leia o primeiro termo e a razão de uma PA (progressão artimetica)
#Programa geral para números decimais (float)
# ####CABEÇALHO (ESTÉTICA, NÃO NECESSÁRIO)
print('\033[1;36m{:*^50}\033[m'.format(' Calculadora de P.A '))
# ###################################################################
a1 = float(input('Digite o primeiro termo da P.A: ')) # Primeiro termo da P.A, para aceitar números decimais.
razão = float(input('Qual a razão da P.A? ')) # Razão da P.A, pode ser número decimal
calc_termo = a1 # Inicializa uma variável para calcular os termos da P.A, começando com a1
print('\033[1;35mOs 10 primeiros termos desta P.A são: \033[m') # print estético
for c in range(1, 11): # começa a iterar sobre os 10 termos para calculá-los
    if c == 1: # como calc_termo inicializa com a1, então para c == 1 basta "printar" a1.
        print(a1, end='; ') # imprime a1 e acrescenta um ";" seguido de espaço após ele ( end é por questão estética)
    else: # depois da primeira iteração para calcular o 2º termo (por exemplo) basta somar a razão ao termo a1, que é o valor de calc_termo
        # para c==1.
        calc_termo += razão # aqui faz uma soma acumulativa para c == n soma a razão ao valor calc_termo alocado pela interação n-1
        # Esse if é opcional, usadao apenas para imprimir um ponto após o último elemento.
        if c < 10:
            print('{:.2f}'.format(calc_termo), end=';  ')
        else:
            print('{:.2f}'.format(calc_termo), end='.')




