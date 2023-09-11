# Digitar indefinidos valores e parar se o usuário digitar 999.
# mostrar a soma e quantos valores foram digitados
c = s = 0 # contador
while True:
    n = int(input('\033[31mDigite um valor (999 para parar): \033[m'))
    if n == 999: # se colocar o break no final ele lê 999 adiciona 1 no contador e 999 na soma
        break
    c += 1
    s += n
print(f'\033[1;32mA soma dos {c} valores é {s}\033[m')