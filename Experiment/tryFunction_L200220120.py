#Fungsi Operator
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4

    var_total = var_harian + var_uts + var_uas
    return var_total

#Fungsi Percabangan
def fungsi_percabangan (var_nilai) :
    var_huruf = ""
    if (var_nilai >= 0 and var_nilai < 20) :
        var_huruf = "E"
    elif (var_nilai >= 20 and var_nilai < 40) :
        var_huruf = "D"
    elif (var_nilai >= 40 and var_nilai < 60) :
        var_huruf = "C"
    elif (var_nilai >= 60 and var_nilai < 80) :
        var_huruf = "B"
    elif (var_nilai >= 80 and var_nilai < 100) :
        var_huruf = "A"
    return var_huruf

#Fungsi Perulangan
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,3):
        print("--------Nilai Ke ",i,"--------")
        var_harian = input("Nilai Harian : ")
        var_uts = input("Nilai UTS : ")
        var_uas = input("Nilai UAS : ")

        #Pemanggilan fungsi Penjumlahan
        var_hasil_perulangan +=(int(fungsi_total_nilai(var_harian, var_uts, var_uas)))

    return var_hasil_perulangan /i


#Pemanggilan fungsi perulangan
var_total = fungsi_perulangan()

print("--------Total Nilai --------")
print("Total nilai yang didapat : ",var_total)

#Pemanggilan Fungsi Percabangan
print("Total Nilai Dalam Huruf : ", fungsi_percabangan(var_total))