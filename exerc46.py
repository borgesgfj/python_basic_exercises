#contagem regressiva fogos de artifício
from time import sleep
import emoji
print('\033[1;33mContagem regressiva\033[m')
for c in range(10, -1, -1):
    print('\033[1;31m', c, '\033[m')
    sleep(1)
print(emoji.emojize(':fireworks:'*20))