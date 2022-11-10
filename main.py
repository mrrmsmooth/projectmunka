from os import system
from function import system


system('cls')
print('Üdvözlet a crypts and monsters-ben!')
print('A 0-ás gombbal kiléphetsz a játékból.')
print('Az 1-es számmal elindíthatod a játékot.')
print('A 2-es számmal megnézheted a statisztikáidat')


choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        jatekKezdete
    elif choice == '2':
        pass