import random

# init data awal
data = ('kubus', 'balok', 'tabung')
soal1 = ""; soal2 = ""; soal3 = ""; soal4 = ""; soal5 = "";

# bagian dict
class dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
 
# init dict
object = dictionary()
 

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
    def __init__(self, bentuk):
        self.bentuk = bentuk
        if(bentuk=='kubus'):
            self.kubus()
        elif(bentuk=='balok'):
            self.balok()
        else:
            self.tabung()
    def __str__(self):
        if(self.bentuk=='kubus'):
            return f"{self.bentuk}, Sisi={self.sisi}"
        elif(self.bentuk=='balok'):
            return f"{self.bentuk}, panjang={self.panjang}, lebar={self.lebar}, panjang={self.panjang}"
        else:
            return f"{self.bentuk}, jari={self.jari}, panjang={self.tinggi}"

# bagian membuat soal secara manual dan menampilkannya
soal1 = soal(random.choice(data))
soal2 = soal(random.choice(data))
soal3 = soal(random.choice(data))
soal4 = soal(random.choice(data))
soal5 = soal(random.choice(data))

print(soal1)
print(soal2)
print(soal3)
print(soal4)
print(soal5)