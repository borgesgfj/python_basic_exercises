#calcualr o preço de uma passagem de ônibus, R$0.50 por km até 200km e 0.45 para mais longas
dis=float(input('\033[1;97;40mQual a distância total da viagem em Km?\033[m '))
if dis<=200:
    print('\033[1;30;44mA passagem custará R$ {:.2f}.\033[m \n \033[1;31;107mBoa viagem!\033[m'.format(dis*0.50))
else:
    print('\033[1;30;44mA passagem custará R$ {:.2f}.\033[m \n \033[1;31;107mBoa viagem!\033[m'.format(dis*0.45))
