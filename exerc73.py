# Tabela do Brasileirão. Mostrar a lista de times pela colocação
# mostrar os 5 primeiros; os quatro últimos, times em ordem alfabetica, posição do Vasco
classificação = ('Náutico', 'Brusque', 'Botafogo', 'CRB', 'Goiás', 'Guarani', 'Sampaio Correia', 'Vila Nova', 'Coritiba', 'Operário', 'Vasco', 'Remo', 'Confiança', 'Vitória', 'Londina', 'CSA', 'Ponte Preta', 'Brasil de Pelotas', 'Cruzeiro', 'Avaí')
print('\033[1;32m=-=\033[m'*38)
print('\033[1;97;40m {: ^115}\033[m'.format(' Brasileirão Série B '))
print('\033[1;32m=-=\033[m'*38)
print(f'\033[1;33mOs 5 primeiros colocados são: {classificação[0:5]} \033[m')
print('\033[1;32m_-_\033[m'*38)
print(f'\033[1;31mOs 4 últimos são {classificação[-4:]}\033[m')
print('\033[1;32m_-_\033[m'*38)
print(f'\033[1;34mOs times participantes por ordem alfabética são:\n{sorted(classificação)}\033[m')
print('\033[1;32m_-_\033[m'*38)
print(f'\033[1;97;40m O Vasco está na {classificação.index("Vasco")}ª posição \033[m')
print('\033[1;32m_=_\033[m'*38)