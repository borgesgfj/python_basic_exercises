#soma dos números ímpares múltilos de 3 entre 1 e 500
print('\033[1;33mSoma dos números ímpares múltiplos de 3 entre 0 e 500\033[m')
s = 0
cont = 0 # Prosposto na solução para saber quantos valores foram solicitados
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('\033[1;34m\nA soma dos {} números ímpares entre 1 e 500 que são múltiplos de 3 é {}'.format(cont ,s))


