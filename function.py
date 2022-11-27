from os import system
import time
from data import *
filename = 'adatok.csv'
ertek = 0

def adatokmentese():
    file = open(filename, 'r', encoding='utf-8')
    filename = mentesek
    mentesek.append(f'5/{ertek}')
    file.close()
    fajlbamentes()

def fajlbamentes():
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{ertek}\n')

def menu():
    global ertek
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('0 - kilépés a játékból.')
    print('1 - játék elindítása.')
    print('2 - statisztikák megnyitása')
    return input('valasztas:')


def eredmenyNezes():
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        mentesek
    file.close()


'''
def loadCars():
    file = open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor = file.readline() # címsor
    for row in file:
        mentesek
    file.close()

def addNewCar():
    system('cls')
    print('Új autó')
    car = input('Autó típusa: ')
    performance = input('Teljesítmánye: ')
    mentesek[car] = performance
    saveCarToFile(car, performance)
    input('Autó felvéve. Tovább (Enter)...')

def saveCarToFile(car, performace):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{car};{performace}\n')
    file.close()

def printAllCar():
    system('cls')
    print('Autók listája')
    for key, value in cars.items():
        print(f'{key} - {value}HP.')
    input('Tovább (Enter)...')

def deleteCar():
    system('cls')
    print('Autó törlése')
    car = input('A törlendő autó típusa: ')
    if car in mentesek:
        mentesek.pop(car)
        saveAllToFile()
        input('Autó törölve. Tovább (Enter)...')
    else:
        input('Nincs ilyen autó. Tovább (Enter)...')

def saveAllToFile():
    file = open(filename, 'w', encoding='utf-8')
    file.write(cimsor)
    for car,performace in cars.items():
        file.write(f'{car};{performace}\n')
    
    file.close()


'''

















'''
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
'''

def jatekKezdete():
    system('cls')
    print('Ruha nélkül egy Várban fekszel.')
    print('1 - Felkelsz.')
    print('2 - Inkább nem.')
    print(mentesek)
    elsoDontes = input('Döntésed:')
    elsoValasztas(elsoDontes)


def elsoValasztas(elsoDontes):
    global masodikDontes
    system('cls')
    if elsoDontes == '1':
        print('Felkeltél')
        print('1 - Körbenézel.')
        print('2 - Inkább nem.')
        masodikDontes = input('Döntésed:')
        masodikValasz(masodikDontes)
    elif elsoDontes == '2':
        input('Enter...')
        Vesztes()



def masodikValasz(masodikDontes):

    system('cls')
    if masodikDontes == '1':
        print('Egy vár tornyában vagy, látsz egy létrát. Körülötted egy romos vár található. (Kb: 20 méter magasan vagy.)')
        print('1 - Lemászol a létrán.')
        print('2 - Leugrassz.')
        harmadikDontes = input('Döntésed:')
        harmadikValasztas(harmadikDontes)
    elif masodikDontes == '2':
        input('Enter...')
        Vesztes()



def harmadikValasztas(harmadikDontes):
    system('cls')
    if harmadikDontes == '1':
        print('lemásztál.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        negyedikDontes = input('Döntésed:')
        negyedikValasz(negyedikDontes)
    elif harmadikDontes == '2':
        print('Beadtad a Water mlg-t.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        negyedikdontes = input('Döntésed:')
        if ertek == 4:
            ertek = 4
        else:
            ertek += 4
        negyedikValasz(negyedikDontes)


def negyedikValasz(negyedikDontes):
    system('cls')
    if negyedikDontes == '1':
        print('Egy öreg omladozó kapun mész keresztül. Bent koponyákat és csontvázakat látsz.(frissnek tűnnek)')
        print('1 - Tovább mész.')
        print('2 - Túlságosan megijesztett a most leírt táj, ezért feladod.')
        otodikdontes = input('Döntésed:')
        otodikvalasz(otodikdontes)
    elif negyedikDontes == '2':
        print('Egy napja mész, de semmit nem találtál(egy erdőben vagy)')
        print('1 - Tovább mész.')
        print('2 - Inkább feladod.')
        otodikdontes2 = input('Döntésed:')
        otodikvalasz2(otodikdontes2)
    
def otodikvalasz(otodikDontes):
    system('cls')
    if otodikDontes == '1':
        print('Tovább mentél, találtál egy kincset grat nyertél.(nincs kedvem tovább írni)')
        time.sleep(5)
        nyertes()
    elif otodikDontes == '2':
        Vesztes()

def otodikvalasz2(otodikDontes2):
    system('cls')
    if otodikDontes2 == '1':
        print('Egy hete mész és elfogyott mindened. Hogyan ölöd meg magad?')
        print('1 - Leszúrod magad egy fadarabbal.')
        print('2 - Leugrassz egy magas fáról(fall damage)')
        print('3 - Belépsz a Jedlik Dök-be.')
        hatodikDontes2 = input('Döntésed:')
        hatodikValasz2(hatodikDontes2)
    elif otodikDontes2 == '2':
        Vesztes()

def hatodikValasz2(hatodikDontes2):
    system('cls')
    if hatodikDontes2 == '1':
        Vesztes()



def Vesztes():
    system('cls')
    print('Vesztettél.')
    input('Enter...')
    adatokmentese()

def nyertes():
    system('cls')
    print('Gratula Nyertél.(nem mintha nehéz lett volna.)')






