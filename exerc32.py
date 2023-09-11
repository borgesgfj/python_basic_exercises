# Determinar se um ano é bissexto
ano = int(input('Digite um ano: '))
if (ano%4)==0:
    if (ano%100)>0:
        print('O ano de {} É BISSEXTO'.format(ano))
    else:
        if (ano%400)==0:
            print('O ano de {} É \033[1;32mBISSEXTO\033[m'.format(ano))
        else:
            print('O ano de {} NÃO É BISSEXTO.'.format(ano))
else:
    print('O ano de {} \033[1;31mNÃO É BISSEXTO\033[m'.format(ano))
