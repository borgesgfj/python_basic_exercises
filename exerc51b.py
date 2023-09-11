#calcular 10 termos de uma PA apartir do termo 1 + razão
# Aqui ao contrário da última vez vou fazer sem calcular termo a termo, usando o range!
# solução proposta pelo Guanabara-curso em vídeo
#só funciona para inteiros!!!
print('\033[1;36m{:*^50}\033[m'.format(' Calculadora de P.A '))
a1 = int(input('Digite o primeiro termo da P.A: ')) # primeiro termo
razão = int(input('Qual a razão da P.A? '))
a10 = a1 + (10-1)*razão # Termo geral da PA an= a1 + (n-1)*razão
for c in range(a1, a10 + razão, razão):
    if c < a10:
        print('{}'.format(c), end = '; ')
    else:
        print('{}'.format(c), end = '.')
