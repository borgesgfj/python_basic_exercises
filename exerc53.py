# verificador de palindromo.
print('\033[1;34m=-\033[m'*30)
print('{:^65}'.format('\033[1;97;44m Analisador de palíndromo \033[m'))
print('\033[1;34m=-\033[m'*30)

frase = str(input('Digite uma frase (ignore os acentos): ')).strip()
frase_limpa = frase.replace(' ', '').lower() # elimina espaços internos. Poderia fazer com split() na frase e depois
# join na frase splitada!
inverso = ''  # aloca uma string que receberá a frase ao contrário
# a frase inversa poderia ser obtida sem o for, com fatiamento da seguinte forma:
# inverso = frase_limpa[::-1] Vai pegar os carcteres do final até o começo (indicado pelo passo - 1)

for i in range(len(frase_limpa) - 1, -1, -1):
    inverso += frase_limpa[i]  # concatena os caracteres da "frase" começando do último
print('A frase: \033[1;33m{}\033[m'.format(frase))
print('{status}'.format(status=
                        '\033[1;4;32mÉ UM PALÍNDROMO\033[m' if frase_limpa == inverso else '\033[1;4;31mNÃO É UM PALÍNDROMO\033[m'))
