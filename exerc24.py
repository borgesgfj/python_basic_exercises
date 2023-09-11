# Leia o nome de uma cidade e indique se ela começa ou não com o nome "Santo"
print('\033[1;31;40mA cidade informada inicia com o nome "Santo"?\033[m')
cid=str(input('Digite o nome de uma cidade: ')).strip()
sep=cid.split()
print('R: {}{}{}'.format('\033[1;33m','santo' in sep[0].lower(),'\033[m'))
print('\033[4;1;30mTrue = Começa, False = Não começa')
