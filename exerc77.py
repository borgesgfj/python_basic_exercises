# Uma tupla com várias palavras não usar acento, depois mostrar cada palavra quais são as vogais
lista_palavras = ('Vasco', 'Futebol', 'Arte', 'Vitoria', 'Amor', 'casa', 'gigante', 'colina',
                  'margem', 'esperança', 'futuro', 'ciencia', 'brasil', 'mercado', 'bola', 'jogador')
for palavras in lista_palavras:
    print(f'\nNa palavra \033[4;31m{palavras.upper()}\033[m tem as seguintes vogais:',end=' ')
    for letra in palavras:
        if letra in 'AaEeIiOoUu':
            print(f'\033[1;32m{letra}\033[m', end=' ')



