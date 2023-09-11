# Programa que leia uma frase e mostre: Quantas vezes aparece a letra 'a', a posição
#que aparece primeiro e a posição que aparece por último.
frase=str(input('Digite uma frase: ')).strip()
print('Você digitou a seguinte frase:\n {}'.format(frase))
print("Nesta frase a letra 'a' aparece {} vezes".format(frase.lower().count('a')))
print("A letra 'a' aparece primeiro na posição {}".format((frase.lower().find('a'))+1))
print("A letra 'a' aparece pela última vez na posição {}".format((frase.lower().rfind('a')+1)))