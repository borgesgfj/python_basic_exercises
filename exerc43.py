#Programa para calcular o Indice de Massa corporea (IMC) e indicar o status da pessoa:
#abaixo do peso (imc<18.5); peso ideal (18.5<= imc <25); sobrepeso (25<=imc <=30); obesidade (30<=imc<=40)
#obesidade morbida imc > 40
#Imc é calculado dividindo o peso da pessoa em Kg dividido pela altura ao quadrado em metros
print('\033[1;97;40mCálculo do índice de massa corporal (IMC)\033[m')
print('')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? (valor em metros) '))
imc = peso/(altura**2)
if imc < 18.5:
    status = '\033[1;4;33mABAIXO DO PESO\033[m.'
elif 18.5 <= imc <25:
    status = 'no seu \033[1;4;32mPESO IDEAL\033[m.'
elif 25 <= imc < 30:
    status = 'em \033[1;4;91mSOBREPESO\033[m.'
elif 30 <= imc < 40:
    status = 'em \033[1;4;91mOBESIDADE\033[m.'
elif imc >= 40:
    status = 'em \033[1;4;31mOBESIDADE MÓRBIDA\033[m.'
print('O seu IMC é {}{:.1f}{}.'.format('\033[34m', imc, '\033[m'))
print('Você está {}'.format(status))
