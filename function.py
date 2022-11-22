from os import system
import time

filename = 'adatok.csv'

healthpoint = 100
inventory = ['kés']
elsoDontes = ''
masodikValasz = ''




def menu():
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('0 - kilépés a játékból.')
    print('1 - játék elindítása.')
    print('2 - statisztikák megnyitása')
    return input('valasztas:')





def jatekKezdete():
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
        system('cls')
        if inventory == []:
            print('Az invetory-d üres.')
            time.sleep(3)
            jatekKezdete()
        else:
            print(f'Az inventory-d tartalma:{inventory}')
            print('1 - inventory bezárása.')
            print('2 - eszköz kidobása')
            inventoryDontes = input('Döntés:')
            if inventoryDontes == '1':
                jatekKezdete()
            elif inventoryDontes == '2':
                system('cls')
                print(f'Az inventory-d tartalma:')
                for i in range(len(inventory)):
                    print('\t\t\t',inventory[i])
                inventoryKidobas = int(input('Melyik eszközt szeretnéd kidobni:'))
                inventory.pop(inventoryKidobas-1)
                print('Az eszközt kidobtad')
                time.sleep(3)
                jatekKezdete()




            
def masodikValasz(masodikDontes):
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
        system('cls')
        if inventory == []:
            print('Az invetory-d üres.')
            time.sleep(3)
            elsoValasztas(elsoDontes)
        else:
            print(f'Az inventory-d tartalma:{inventory}')
            print('1 - inventory bezárása.')
            print('2 - eszköz kidobása')
            inventoryDontes = input('Döntés:')
            if inventoryDontes == '1':
                elsoValasztas(elsoDontes)
            elif inventoryDontes == '2':
                system('cls')
                print(f'Az inventory-d tartalma:')
                for i in range(len(inventory)):
                    print('\t\t\t',inventory[i])
                inventoryKidobas = int(input('Melyik eszközt szeretnéd kidobni:'))
                inventory.pop(inventoryKidobas-1)
                print('Az eszközt kidobtad')
                time.sleep(3)
                elsoValasztas(elsoDontes)

def harmadikValasztas(harmadikDontes):
    system('cls')
    if harmadikDontes == '1':
        print('lemásztál.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        print('3 - Inventory megnyitása.')
    if harmadikDontes == '2':
        print('Beadtad a Water mlg-t.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        print('3 - Inventory megnyitása.')
    elif harmadikDontes == '3':
        system('cls')
        if inventory == []:
            print('Az invetory-d üres.')
            time.sleep(3)
            elsoValasztas(elsoDontes)
        else:
            print(f'Az inventory-d tartalma:{inventory}')
            print('1 - inventory bezárása.')
            print('2 - eszköz kidobása')
            inventoryDontes = input('Döntés:')
            if inventoryDontes == '1':
                elsoValasztas(elsoDontes)
            elif inventoryDontes == '2':
                system('cls')
                print(f'Az inventory-d tartalma:')
                for i in range(len(inventory)):
                    print('\t\t\t',inventory[i])
                inventoryKidobas = int(input('Melyik eszközt szeretnéd kidobni:'))
                inventory.pop(inventoryKidobas-1)
                print('Az eszközt kidobtad')
                time.sleep(3)
                elsoValasztas(elsoDontes)

def negyedikValasz():
    pass    
    


def Vesztes():
    system('cls')
    print('Vesztettél.')
    input('Enter...')






def eredmenyNezes():
    pass
