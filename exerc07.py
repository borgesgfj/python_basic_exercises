# Programa que calcule as duas notas de um aluno e calcule sua média
nome= input('Qual o nome do(a) aluno(a)? ')
n1 = float(input('Digite a nota da primeira prova '))
n2 = float(input('Digite a nota da segunda prova '))
m = (n1 + n2) / 2  # média nas duas provas
print('A pontuação média de {} é {}'.format(nome, m))

