"""
    Author  : Bara Donta Perdana
    Date    : D7-M12-Y2022
    Note    : run in python terminal or vsc/vscodium (coderunner ext)
"""

# procedure section
def menu():
    print('Berikut adalah beberapa perintah yang dapat digunakan:')
    print('K Kubus')
    print('B Balok')
    print('T Tabung')
    print('P Prisma')
    print('b Bola')
    print('S Limas segitiga')
    print('p Limas segiempat')
    print('L Kerucut')
    print('- ---')
    print('- ---')
    print('- ---')
    print('M Menu')
    print('x Keluar')

def cube():
        """
        Mencari volume kubus       
        """
        s = int(input('Masukkan panjang sisi kubus: '))
        print('Volume kubus tersebut adalah', s**3, '\n')
        
def cuboid():
        """
        Mencari volume balok       
        """
        p = int(input('Masukkan panjang balok: '))
        l = int(input('Masukkan lebar balok: '))
        t = int(input('Masukkan tinggi balok: '))
        print('Volume balok tersebut adalah', p*l*t, '\n')

def cylinder():
        """
        Mencari volume tabung      
        """
        r = int(input('Masukkan jari-jari lingkaran: '))
        t = int(input('Masukkan tinggi tabung: '))
        print('Volume balok tersebut adalah', round((22/7)*(r**2)*t, 2), '\n')
        
def prism():
        """
        Mencari volume prisma       
        """
        a = int(input('Masukkan alas segitiga: '))
        t = int(input('Masukkan tinggi segitiga: '))
        T = int(input('Masukkan tinggi prisma: '))
        print('Volume balok tersebut adalah', round(0.5*a*t*T, 2), '\n')

def sphere():
        """
        Mencari volume bola       
        """
        r = int(input('Masukkan jari-jari bola: '))
        print('Volume balok tersebut adalah', round((4/3)*(22/7)*(r**3), 2), '\n')

def tetrahedron():
        """
        Mencari volume limas segitiga       
        """
        a = int(input('Masukkan alas segitiga: '))
        t = int(input('Masukkan tinggi segitiga: '))
        T = int(input('Masukkan tinggi limas: '))
        print('Volume balok tersebut adalah', round((1/3)*(0.5*a*t)*T, 2), '\n')

def sqrPyramid():
        """
        Mencari volume limas segiempat     
        """
        p = int(input('Masukkan panjang alas: '))
        l = int(input('Masukkan lebar alas: '))
        T = int(input('Masukkan tinggi limas: '))
        print('Volume balok tersebut adalah', round((1/3)*(p*l)*T, 2), '\n')

def cone():
        """
        Mencari volume kerucut      
        """
        r = int(input('Masukkan jari-jari lingkaran: '))
        T = int(input('Masukkan tinggi kerucut: '))
        print('Volume balok tersebut adalah', round((3/3)*((22/7)*(r**2))*T, 2), '\n')


# init at start
menu()

# main iteration
while True:
    ans = input('Masukkan perintah yang ingin digunakan: ')
    if(ans=="x"):
        print('terima kasih')
        exit()
    elif(ans=='M'):
        menu()
    elif(ans=='K'):
        cube()
    elif(ans=='B'):
        cuboid()
    elif(ans=='T'):
        cylinder()
    elif(ans=='P'):
        prism()
    elif(ans=='b'):
        sphere()
    elif(ans=='S'):
        tetrahedron()
    elif(ans=='p'):
        sqrPyramid()
    elif(ans=='L'):
        cone()
    else:
        print('Perintah yang anda masukkan salah, silahkan ulangi lagi\n')