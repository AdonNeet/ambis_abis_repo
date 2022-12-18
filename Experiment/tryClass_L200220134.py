class balok_liter(object):
    liter = 100
    pi = 3.14
    def __init__(self, panjang, lebar, tinggi):
        self.p = panjang
        self.l = lebar
        self.t = tinggi
    def literbalok(self):
        vb =  (self.p * self.l * self.t) * self.liter
        return vb
class tabung_liter(balok_liter):
    def __init__(self, diameter, tinggi):
        self.d = diameter
        self.t = tinggi
    def litertabung(self):
        vt = self.pi * self.d * self.t * self.liter
        return vt

while True:
    print('Pilih bangunan yang ingin di hitung berapa maksimal liter air\n','1. Balok\n','2. Tabung\n','3. Keluar\n','Catatan : Tolong saat memasukan Nilai itu berbentuk Meter\n')
    user = str(input('Pilih No: '))
    if user == '1':
        i1 = float(input('Panjang Balok : '))
        i2 = float(input('Lebar Balok: '))
        i3 = float(input('Tinggi Balok: '))
        i = balok_liter(i1,i2,i3)
        print('Maksimal yang bisa di tampung oleh balok sebanyak ',i.literbalok(),' Liter')
    elif user == '2':
        u1 = float(input('Diameter alas Tabung : '))
        u2 = float(input('Tinggi tabung : '))
        u = tabung_liter(u1,u2)
        print('Maksimal yang bisa di tampung oleh tabung sebanyak',u.litertabung(),'Liter')
    elif user == '3':
        print('Program selesai')
        break
    else:
        print('Tidak ada Pilihan ,dicoba lagi')



