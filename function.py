from os import system

filename = 'adatok.csv'




def menu():
    #system('cls')
    print('Üdvözlet a crypts and monsters-ben!')
    print('A 0-ás gombbal kiléphetsz a játékból.')
    print('Az 1-es számmal elindíthatod a játékot.')
    print('A 2-es számmal megnézheted a statisztikáidat')
    return input('valasztas:')

def jatekKezdete():
    #system('cls')
    print('Ruha nélkül egy Várban fekszel.')
    print('1 - Felkelsz.')
    print('2 - Inkább nem.')
    elsoDontes = input('Döntésed:')
    elsoValasztas(elsoDontes)
    
    
def elsoValasztas(elsoDontes):
    if elsoDontes == '1':
        print('Felkeltél')
        print('1 - Körbenézel.')
        print('2 - Megnézed mi van nálad.')
        masodikDontes = input('Döntésed:')
        masodikValasz(masodikDontes)
    elif elsoDontes == '2':
        input('Enter...')
        Vesztes()


            
def masodikValasz(masodikDontes):
    if masodikDontes == '1':
        print('youuu')
    elif masodikDontes == '2':
        print('youuu2')


def Vesztes():
    system('cls')
    print('Vesztettél.')



def eredmenyNezes():
    pass
