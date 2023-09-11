#Informe de alistamento militar. Calcula a idade, e diz se ele vai ter que se alistar; já passou
#da hora ou ainda vai se alistar.
from datetime import date
nascimento = int(input('Informe seu ano de nascimento. '))
idade = date.today().year - nascimento
sexo = str(input('Qual seu sexo? (masculino/feminino) ')).strip()
print('\033[1;34mSua idade atual é {} anos.\033[m'.format(idade))
if sexo.lower() == 'feminino':
    print('\033[1;30mO serviço militar não é obrigatório para mulheres. Tenha um ótimo dia.')
elif sexo.lower() == 'masculino':
    if idade < 18:
        print('\033[1;32mVocê deverá se alistar daqui a {} anos. Seu alistamento será em {}\033[m'.format(18 - idade, nascimento + 18))
    elif idade==18:
        print('\033[1;94mJá está na hora de você se alistar!Vai na fé!\033[m')
    elif idade > 18:
        print('\033[1;31mJá passou o tempo de você se alistar. Você deviria ter se alistado há {} anos, em {}.\033[m'.format(idade - 18,nascimento +18))
        print('\033[1;31mCaso não o tenha se alistado procure a junta militar mais próxima de você.\033[m')
print('Obrigado!')

