#leia a velocidade de um carro, se ultrapassar 80km/h, notificar multa
#a multa custa 7,00 por cada km acima do limite.
vel=float(input('Qual a velocidade do carro em Km/h? '))
if vel>80:
    print('\033[1;97;41mVocê foi multado!\033[m \n\033[1;31;40mO limite de velocidade é 80km/h\033[m')
    print('\033[1;31;107mVocê deverá pagar R$ {:.2f} de multa.\033[m'.format((vel-80)*7))
else:
    print('\033[1;32;107mParabéns você está dentro do limite de velocidade!\033[m')
