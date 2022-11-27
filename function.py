from os import system
import time
from data import *
filename = 'adatok.csv'
ertek = ''


def ujErtek():
    global ertek
    mentesek.append(ertek)
    saveToFile(ertek)


def saveToFile(ertek):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{ertek}' + '\n')
    file.close()


def menu():
    global ertek
    system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('0 - kilépés a játékból.')
    print('1 - játék elindítása.')
    print('2 - statisztikák megnyitása')
    return input('valasztas:')


def eredmenyNezes():
    system('cls')
    file = open(filename, 'r', encoding='utf-8')
    print('Eredmények')
    for a in mentesek:
        print(f'\t{a}')
    input('Enter...')
    file.close()

def jatekKezdete():
    global ertek
    system('cls')
    ertek = '6/0'
    print('Ruha nélkül egy Várban fekszel.')
    print('1 - Felkelsz.')
    print('2 - Inkább nem.')
    elsoDontes = input('Döntésed:')
    elsoValasztas(elsoDontes)


def elsoValasztas(elsoDontes):
    system('cls')
    global ertek
    if elsoDontes == '1':
        print('Felkeltél')
        print('1 - Körbenézel.')
        print('2 - Inkább nem.')
        masodikDontes = input('Döntésed:')
        ertek = '6/1'
        masodikValasz(masodikDontes)
    elif elsoDontes == '2':
        input('Enter...')
        Vesztes()
        ertek = '6/1'



def masodikValasz(masodikDontes):

    system('cls')
    global ertek
    if masodikDontes == '1':
        print('Egy vár tornyában vagy, látsz egy létrát. Körülötted egy romos vár található. (Kb: 20 méter magasan vagy.)')
        print('1 - Lemászol a létrán.')
        print('2 - Leugrassz.')
        print('3 - Megpróbálod feldolgozni, hogy hogyan lehet ennyire rossza a dök.')
        harmadikDontes = input('Döntésed:')
        ertek = '6/2'
        harmadikValasztas(harmadikDontes)
    elif masodikDontes == '2':
        input('Enter...')
        Vesztes()
        ertek = '6/2'
    



def harmadikValasztas(harmadikDontes):
    system('cls')
    global ertek
    if harmadikDontes == '1':
        print('lemásztál.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        negyedikDontes = input('Döntésed:')
        ertek = '6/3'
        negyedikValasz(negyedikDontes)
    elif harmadikDontes == '2':
        print('Beadtad a Water mlg-t.')
        print('1 - A várba mész.')
        print('2 - Elingdulsz a másik irányba.')
        negyedikDontes = input('Döntésed:')
        ertek = '6/3'
        negyedikValasz(negyedikDontes)
    elif harmadikDontes == '3':
        ertek = '6/3'
        Vesztes()


def negyedikValasz(negyedikDontes):
    system('cls')
    global ertek
    if negyedikDontes == '1':
        print('Egy öreg omladozó kapun mész keresztül. Bent koponyákat és csontvázakat látsz.(frissnek tűnnek)')
        print('1 - Tovább mész.')
        print('2 - Túlságosan megijesztett a most leírt táj, ezért feladod.')
        otodikdontes = input('Döntésed:')
        ertek = '6/4'
        otodikvalasz(otodikdontes)
    elif negyedikDontes == '2':
        print('Egy napja mész, de semmit nem találtál(egy erdőben vagy)')
        print('1 - Tovább mész.')
        print('2 - Inkább feladod.')
        otodikdontes2 = input('Döntésed:')
        ertek = '6/4'
        otodikvalasz2(otodikdontes2)
    
def otodikvalasz(otodikDontes):
    system('cls')
    global ertek
    if otodikDontes == '1':
        print('Tovább mentél, találtál egy kincset grat nyertél.(nincs kedvem tovább írni)')
        ertek = '6/4'
        time.sleep(5)
        nyertes()
    elif otodikDontes == '2':
        ertek = '6/4'
        Vesztes()

def otodikvalasz2(otodikDontes2):
    system('cls')
    global ertek
    if otodikDontes2 == '1':
        print('Egy hete mész és elfogyott mindened. Hogyan ölöd meg magad?')
        print('1 - Leszúrod magad egy fadarabbal.')
        print('2 - Leugrassz egy magas fáról(fall damage)')
        print('3 - Belépsz a Jedlik Dök-be.')
        hatodikDontes2 = input('Döntésed:')
        ertek = '6/5'
        hatodikValasz2(hatodikDontes2)
    elif otodikDontes2 == '2':
        ertek = '6/5'
        Vesztes()

def hatodikValasz2(hatodikDontes2):
    system('cls')
    global ertek
    if hatodikDontes2 == '1':
        ertek = '6/5'
        Vesztes()
    if hatodikDontes2 == '2':
        ertek = '6/5'
        Vesztes()
    if hatodikDontes2 == '3':
        ertek = '6/5'
        Vesztes()



def Vesztes():
    system('cls')
    print('Vesztettél.')
    input('Enter...')
    ujErtek()

def nyertes():
    global ertek
    system('cls')
    ertek = '6/6'
    print('Gratula Nyertél.(nem mintha nehéz lett volna.)')
    ujErtek()
