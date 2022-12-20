import random

# init data awal
data = ('kubus', 'balok', 'tabung')

"""         # tidak digunakan
# bagian dict
class dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
# init dict
instances = dictionary()
"""

instances = []

# bagian class
class soal:
    def kubus(self):
        self.sisi = random.randint(1, 50)
    def balok(self):
        self.panjang = random.randint(1, 50)
        self.lebar = random.randint(1, 50)
        self.tinggi = random.randint(1, 50)
    def tabung(self):
        self.jari = random.randint(1, 50)
        self.tinggi = random.randint(1, 50)
    def __init__(self, nama, bentuk):
        self.nama = nama
        self.bentuk = bentuk
        if(bentuk=='kubus'):
            self.kubus()
        elif(bentuk=='balok'):
            self.balok()
        else:
            self.tabung()
    """ # tidak digunakan
    def __str__(self):
        if(self.bentuk=='kubus'):
            return f"{self.bentuk}, Sisi={self.sisi}"
        elif(self.bentuk=='balok'):
            return f"{self.bentuk}, panjang={self.panjang}, lebar={self.lebar}, panjang={self.panjang}"
        else:
            return f"{self.bentuk}, jari={self.jari}, panjang={self.tinggi}"
    """

# bagian membuat soal secara otomatis
for i in range(1, 6):
    temp1 = 'soal '+str(i)
    bentuk = random.choice(data)
    temp1 = soal(temp1, bentuk)
    # instances.add(temp1, bentuk)
    instances += [temp1]

# bagian menampilan masing-masing data
for instance in instances:
    if(instance.bentuk=='kubus'):
        print(instance.nama, '  ', instance.bentuk, 'sisi =', instance.sisi)
    elif(instance.bentuk=='balok'):
        print(instance.nama, '  ', instance.bentuk, 'panjang =', instance.panjang, 'lebar =', instance.lebar,  'tinggi =', instance.tinggi)
    else:
        print(instance.nama, '  ', instance.bentuk, 'jari2 =', instance.jari, 'lebar =', 'tinggi =', instance.tinggi)