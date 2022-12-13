def header():
    print(f"{'MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG':^50}")

def user():
    '''input user'''
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    return panjang, lebar

def luas_p(panjang, lebar):
    '''menghitung luas'''
    luas = panjang*lebar
    return luas

def keliling_p(panjang , lebar):
    '''menghitung keliling'''
    return 2*(panjang+lebar)

while True:
    header()
    p,l = user()
    opsi = input("masukkan K untuk keliling dan L untuk luas: ")
    if opsi == 'L':
        print(luas_p(p,l))
        break
    elif opsi == 'K':
        print(keliling_p(p,l))
        break
    else:
        print('masukkan anda salah, K untuk keliling dan L untuk luas')