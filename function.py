from os import system

filename = 'adatok.csv'

healthpoint = 100
inventory = []




def menu():
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('0 - kilépés a játékból.')
    print('1 - játék elindítása.')
    print('2 - statisztikák megnyitása')
    return input('valasztas:')

def jatekKezdete():
    system('cls')
    print('Ruha nélkül egy Várban fekszel.')
    print('1 - Felkelsz.')
    print('2 - Inkább nem.')
    print('3 - inventory megnyitása')
    print(f'Hp:{healthpoint}')
    elsoDontes = input('Döntésed:')
    elsoValasztas(elsoDontes)
    
    
def elsoValasztas(elsoDontes):
    system('cls')
    if elsoDontes == '1':
        print('Felkeltél')
        print('1 - Körbenézel.')
        print('2 - Megnézed mi van nálad.')
        print('3 - inventory megnyitása')
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
            
        else:
            print(f'Az inventory-d tartalma:{inventory}')
            print('1 - inventory bezárása.')
            print('2 - eszköz kidobása')
            inventoryDontes = input('Döntés:')
            if inventoryDontes == '1':
                elsoValasztas
            elif inventoryDontes == '2':
                system('cls')
                print(f'Az inventory-d tartalma:')
                for i in range(len(inventory)):
                    print('\t\t\t',inventory[i])
                inventoryKidobas = int(input('Melyik eszközt szeretnéd kidobni:'))    
                inventory.pop(inventoryKidobas-1)


            
def masodikValasz(masodikDontes):
    system('cls')
    if masodikDontes == '1':
        print('youuu')
    elif masodikDontes == '2':
        print('youuu2')


def Vesztes():
    system('cls')
    print('Vesztettél.')
    input('Enter...')



def eredmenyNezes():
    pass
