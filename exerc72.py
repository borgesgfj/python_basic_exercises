# usando tupla criar um programa para ler um número entre 0 e 20 e escrever ele por extenso
numerais = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezessies', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('\033[31mOpção inválida!\033[m')
    else:
        break
print(f'\033[1;32mO número digitado foi\033[m \033[4;31m{numerais[num]}\033[m')