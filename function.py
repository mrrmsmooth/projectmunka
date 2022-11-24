from os import system
import time

filename = 'adatok.csv'

healthpoint = 100
inventory = ['kés']

elsoDontes = ''
masodikValasz = ''
harmadikValasztas = ''
negyedikValasz = ''
ertek = 0

def menu():
    global ertek
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('0 - kilépés a játékból.')
    print('1 - játék elindítása.')
    print('2 - statisztikák megnyitása')
    return input('valasztas:')

def eszköztár():
    global ertek
    print(f'Az inventory-d tartalma:{inventory}')
    print('1 - inventory bezárása.')
    print('2 - eszköz kidobása')
    inventoryDontes = input('Döntés:')
    if inventoryDontes == '1':
        order()
    elif inventoryDontes == '2':
        system('cls')
        print(f'Az inventory-d tartalma:')
        for i in range(len(inventory)):
            print('\t\t\t',inventory[i])
        inventoryKidobas = int(input('Melyik eszközt szeretnéd kidobni:'))
        inventory.pop(inventoryKidobas-1)
        print('Az eszközt kidobtad')
        time.sleep(3)
        order()

def order():
    if ertek == 0:
        menu()
    elif ertek == 1:
        jatekKezdete()
    elif ertek == 2:
        elsoValasztas(elsoDontes)
    elif ertek == 3:
        masodikValasz(masodikDontes)
    elif ertek == 4:
        harmadikValasztas()
    elif ertek == 5:
        negyedikValasz()
    elif ertek == 6:
        otodikvalasz()
    elif ertek == 7:
        hatodikvalasz()


def jatekKezdete():
    global ertek
    global elsoDontes
    
    system('cls')
    print('Ruha nélkül egy Várban fekszel.')
    print('1 - Felkelsz.')
    print('2 - Inkább nem.')
    print('3 - inventory megnyitása.')
    print(f'Hp:{healthpoint}')
    elsoDontes = input('Döntésed:')
    elsoValasztas(elsoDontes)


def elsoValasztas(elsoDontes):
    global ertek
    global masodikDontes
    system('cls')
    if elsoDontes == '1':
        print('Felkeltél')
        print('1 - Körbenézel.')
        print('2 - Inkább nem.')
        print('3 - Inventory megnyitása.')
        print(f'Hp:{healthpoint}')
        masodikDontes = input('Döntésed:')
        masodikValasz(masodikDontes)
    elif elsoDontes == '2':
        input('Enter...')
        Vesztes()
    elif elsoDontes == '3':
        eszköztár()


def masodikValasz(masodikDontes):
    global ertek
    system('cls')
    if masodikDontes == '1':
        print('Egy vár tornyában vagy, látsz egy létrát. Körülötted egy romos vár található. (Kb: 20 méter magasan vagy.)')
        print('1 - Lemászol a létrán.')
        print('2 - Leugrassz.')
        print('3 - Inventory megnyitása.')
        print(f'Hp:{healthpoint}')
        harmadikDontes = input('Döntésed:')
        harmadikValasztas(harmadikDontes)
    elif masodikDontes == '2':
        input('Enter...')
        Vesztes()
    elif masodikDontes == '3':
        eszköztár()


def harmadikValasztas(harmadikDontes):
    global ertek
    global negyedikdontes
    system('cls')
    if harmadikDontes == '1':
        print('lemásztál.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        print('3 - Inventory megnyitása.')
        negyedikdontes = input('Döntésed:')
    elif harmadikDontes == '2':
        print('Beadtad a Water mlg-t.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        print('3 - Inventory megnyitása.')
        negyedikdontes = input('Döntésed:')
    elif harmadikDontes == '3':
        eszköztár()


def negyedikValasz(negyedikdDontes):
    global ertek
    system('cls')
    if negyedikdDontes == '1':
        print('Egy öreg omladozó kapun mész keresztül. Bent koponyákat és csontvázakat látsz.(frissnek tűnnek)')
        print('1 - ')
        print('2 -')
        print('3 -')
    elif negyedikdDontes == '2':
        pass
    elif negyedikdDontes == '3':
        eszköztár()
    
def otodikvalasz(otodikDontes):
    pass

def hatodikvalasz(hatodikDontes):
    pass


def Vesztes():
    system('cls')
    print('Vesztettél.')
    input('Enter...')






def eredmenyNezes():
    pass
