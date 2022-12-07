def penjumlahan(x):
    return x

ans = 0

print('Jika angka 0 dimasukkan, maka perulangan input akan berhenti')
while True:
    num = int(input('Masukkan angka yang ingin ditambahkan: '))
    if(num != 0):
       ans += penjumlahan(int(num))
    else:
        break

print('Hasil penjumlahannya yaitu', ans)