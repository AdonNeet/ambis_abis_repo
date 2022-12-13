"""
    Author  : Bara Donta Perdana
    Date    : D13-M12-Y2022
    Note    : run in python terminal or vsc/vscodium (coderunner ext)
"""

# import weakref # module for garbage collector, gak jadi dipakai karena sering error (Note : perlu diperdalam lagi)

# bagian class
class Dog:
    def __init__(self, nama, berat, entry):
        self.nama = nama
        self.berat = berat
        self.entry = entry


# bagian main
count = int(0)
instances = []
print('Selamat datang di program mendata "Anjing", silahkan isi data yang berkaitan.....\nuntuk keluar dari program ketik angka 0 pada input nama')
while True:
    temp1 = input('Masukkan nama anjing : ')
    if(temp1=='0'):
        break
    count+=1
    temp2 = input('Masukkan berat anjing tersebut : ')
    temp1 = Dog(temp1, temp2, count)
    instances += [temp1]

# bagian menampilkan semua data yang telah di input  
print('\n\n==========================================')
print('berikut adalah anjing yang telah terdata\nNo     Nama     Berat')
'    '
for instance in instances:
    print(instance.entry, '    ',instance.nama, '    '+str(instance.berat))
print('Jumlah anjing yang terdata sebanyak', count)
print('==========================================')