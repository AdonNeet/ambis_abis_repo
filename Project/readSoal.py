import generateSoal

# program membaca soal dari soal yang telah di generate di module generateSoal
instances = generateSoal.instances

# it work as well
for instance in instances:
    if(instance.bentuk=='kubus'):
        print(instance.nama, '  ', instance.bentuk, 'sisi =', instance.sisi)
    elif(instance.bentuk=='balok'):
        print(instance.nama, '  ', instance.bentuk, 'panjang =', instance.panjang, 'lebar =', instance.lebar,  'tinggi =', instance.tinggi)
    else:
        print(instance.nama, '  ', instance.bentuk, 'jari2 =', instance.jari, 'lebar =', 'tinggi =', instance.tinggi)