import solveSoal

# init var soal dan jawaban
soal = None
ans = None

# untuk mengakses properti masing-masing bentuk, gunakan if statement
class inspect:
    def __init__(self, soal):
        if(soal.bentuk=='kubus'):
            self.bentuk = soal.bentuk
            self.sisi = soal.sisi
        elif(soal.bentuk=='balok'):
            self.bentuk = soal.bentuk
            self.panjang = soal.panjang
            self.lebar = soal.lebar
            self.tinggi = soal.tinggi
        elif(soal.bentuk=='tabung'):
            self.bentuk = soal.bentuk
            self.jari = soal.jari
            self.tinggi = soal.jari
        else:
            self.bentuk = soal.bentuk
            self.diketahui = soal.know
            if(self.diketahui=='air'):
                self.hCair = soal.hAir
            else:
                self.hCair = soal.hAlkohol


# untuk menampilkan info tentang properti soal tersebut dapat menggunakan if statement
def show(info):     # rubah print ini ke bentuk label jika di tkinter
    if(soal.bentuk=='kubus'):
        print('bentuk =', info.bentuk)
        print('sisi =', info.sisi)
    elif(soal.bentuk=='balok'):
        print('bentuk =', info.bentuk)
        print('panjang =', info.panjang)
        print('lebar =', info.lebar)
        print('tingg =', info.tinggi)
    elif(soal.bentuk=='tabung'):
        print('bentuk =', info.bentuk)
        print('jari2 =', info.jari)
        print('tingg =', info.tinggi)
    else:
        print('bentuk =', info.bentuk)
        print('diketahui =', info.diketahui)
        print('tinggi cairan =', info.hCair)

# ketika menekan button akan menjalankan fungsi soalBaru pada solveSoal.py 
soal = solveSoal.soalBaru() # kemudian mencari jawabannya
ans = solveSoal.jawab(soal) 
# untuk mengetahui properti tentang soal maka dapat di lakukan dengan menggunakan class inspect
info = inspect(soal)
# untuk menampilkan info dapat menggunakan if statement padaa fungsi show
show(info)



