import solveSoal
print('ini dari readAnswer')
# program membaca soal dari soal yang telah di generate di module generateSoal
quest = solveSoal.quest
ans = solveSoal.ans

# it to read the question
for instance in quest:
    if(instance.bentuk=='kubus'):
        print(instance.nama , instance.bentuk, 'sisi =', instance.sisi)
    elif(instance.bentuk=='balok'):
        print(instance.nama, instance.bentuk, 'panjang =', instance.panjang, 'lebar =', instance.lebar,  'tinggi =', instance.tinggi)
    else:
        print(instance.nama, instance.bentuk, 'jari2 =', instance.jari, 'lebar =', 'tinggi =', instance.tinggi)

# it to read the answer
for instance in quest:
    print(instance.nama, instance.bentuk, ans[instance.nama])
