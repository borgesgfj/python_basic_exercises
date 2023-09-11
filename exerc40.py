#Leia a média de duas notas e mostre se o está aprovado (med>7.0), de recuperação (5<méd<6.9),
#ou reprovado (med<5)
print('\033[1;97;40m**\033[m'*16)
print('\033[1;30;107mCálculo da situação de estudante\033[m')
print('\033[1;97;40m**\033[m'*16)

n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
media = (n1+n2)/2
print('\033[1;33mA sua média foi {:.1f}\033[m'.format(media))
if media >= 7.0:
    print('\033[1;32mVocê foi APROVADO! Parabéns!\033[m')
elif media < 5.0:
    print('\033[1;31mVocê foi REPROVADO.\033[m')
elif 5.0 <= media < 7:
    print('\033[1;34mVocê ficou de RECUPERAÇÃO. Estude mais e boa sorte!')


