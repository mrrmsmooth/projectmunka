from os import system




def jatekKezdete():
    pass

print(f'Egy elhagyatott házban ébredsz egy szál Rick and Morty-s alsógatyában.')


def menu():
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('A 0-ás gombbal kiléphetsz a játékból.')
    print('Az 1-es számmal elindíthatod a játékot.')
    print('A 2-es számmal megnézheted a statisztikáidat')
    return input('valasztas:')