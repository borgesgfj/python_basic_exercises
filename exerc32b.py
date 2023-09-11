# Usando uma sintaxe mais curta ( que dá o mesmo resultado) igual a que foi mostrada pelo
#Guanabara em Curso em video
from datetime import date
ano=int(input('Que ano você quer analisar? (Digite 0 para o ano atual): '))
if ano==0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano de {} É BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))
