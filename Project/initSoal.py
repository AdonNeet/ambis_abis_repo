import random
print('ini dari initSoal')
# init data awal untuk gacha
data = ('kubus', 'balok', 'tabung')

# init dict
instances = []

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

    # bagian input argument
    def __init__(self, nama, bentuk):
        self.nama = nama
        self.bentuk = bentuk
        if(bentuk=='kubus'):
            self.kubus()
        elif(bentuk=='balok'):
            self.balok()
        else:
            self.tabung()

# bagian membuat soal secara otomatis
for i in range(1, 6):
    temp1 = 'soal '+str(i)
    bentuk = random.choice(data)
    temp1 = soal(temp1, bentuk)
    # instances.add(temp1, bentuk)
    instances += [temp1]

# bagian menampikan soal yang sudah dibuat
for instance in instances:
    if(instance.bentuk=='kubus'):
        print(instance.nama, '  ', instance.bentuk, 'sisi =', instance.sisi)
    elif(instance.bentuk=='balok'):
        print(instance.nama, '  ', instance.bentuk, 'panjang =', instance.panjang, 'lebar =', instance.lebar,  'tinggi =', instance.tinggi)
    else:
        print(instance.nama, '  ', instance.bentuk, 'jari2 =', instance.jari, 'lebar =', 'tinggi =', instance.tinggi)
print('\n')