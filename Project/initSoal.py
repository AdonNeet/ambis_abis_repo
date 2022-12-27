import random
print('ini dari initSoal')
# init data awal untuk gacha
data = ('kubus', 'balok', 'tabung', 'bejana')
quest = None

# init dict, tidak digunakan
# instances = []

# bagian class
class soal:
    # membuat soal berdasarkan bentuk
    def kubus(self):
        self.sisi = random.randint(1, 50)
    def balok(self):
        self.panjang = random.randint(1, 50)
        self.lebar = random.randint(1, 50)
        self.tinggi = random.randint(1, 50)
    def tabung(self):
        self.jari = random.randint(1, 50)
        self.tinggi = random.randint(1, 50)
    def bejana(self):
        """
        Soal tentang hidrostatis

        rumus hidrostatis bejana berhubungan
        rho1 h1 = rho2 h2
        rho = massa jenis
        h = tinggi permukaan zat cair

        disini kita akan menggunakan air dan alkohol
        rho air = 1000kg/m^3
        rho alkohol = 800kg/m^3
        """
        dat = ('air', 'alkohol')
        self.mAir = int(1000)
        self.mAlkohol = int(800)
        tmp = random.choice(dat)
        if(tmp=='air'):
            self.hAir=random.randint(1, 50)
            self.hAlkohol = None
        else:
            self.hAlkohol=random.randint(1, 50)
            self.hAir= None


    # bagian input argument
    def __init__(self, nama, bentuk):
        self.nama = nama
        self.bentuk = bentuk
        if(bentuk=='kubus'):
            self.kubus()
        elif(bentuk=='balok'):
            self.balok()
        elif(bentuk=='tabung'):
            self.tabung()
        else:
            self.bejana()

quest = None
# membuat satu soal ketika dipanggil
def buatSoal():
    global quest
    bentuk = random.choice(data)
    quest = soal('soal', bentuk)
    """ # untuk check soal yang terbentuk
    if(quest.bentuk=='kubus'):  # it works
        print(quest.nama, '  ', quest.bentuk, 'sisi =', quest.sisi)
    elif(quest.bentuk=='balok'):
        print(quest.nama, '  ', quest.bentuk, 'panjang =', quest.panjang, 'lebar =', quest.lebar,  'tinggi =', quest.tinggi)
    else:
        print(quest.nama, '  ', quest.bentuk, 'jari2 =', quest.jari, 'lebar =', 'tinggi =', quest.tinggi)
    """

# otomatis menjalankan function diatas ketika initSoal di import
# buatSoal()

"""
# bagian membuat soal secara otomatis
for i in range(1, 6):
    temp1 = 'soal '+str(i)
    bentuk = random.choice(data)
    temp1 = soal(temp1, bentuk)
    # instances.add(temp1, bentuk)
    instances += [temp1]
"""

"""
# bagian menampikan soal yang sudah dibuat
for instance in instances:
    if(instance.bentuk=='kubus'):
        print(instance.nama, '  ', instance.bentuk, 'sisi =', instance.sisi)
    elif(instance.bentuk=='balok'):
        print(instance.nama, '  ', instance.bentuk, 'panjang =', instance.panjang, 'lebar =', instance.lebar,  'tinggi =', instance.tinggi)
    else:
        print(instance.nama, '  ', instance.bentuk, 'jari2 =', instance.jari, 'lebar =', 'tinggi =', instance.tinggi)
print('\n')
"""