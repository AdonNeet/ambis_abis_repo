nama = []
nim = []
alamat = []

def showdata():
    if len(nama) <= 0:
        print('Nama : (Belum ada data nama)')
    if len(nama) <= 1:
        for indeks in range(len(nama)):
            print('Nama:',nama[0])
    if len(nim) <= 0:
        print('Nim : (Belum ada data nim)')
    if len(nim) <= 1:
        for indeks in range(len(nim)):
            print('Nim:',nim[0])
    if len(alamat) <= 0:
        print('Alamat : (Belum ada data alamat)')
    if len(alamat) <= 1:        
        for indeks in range(len(alamat)):
            print('Alamat:',alamat[0])
    
def insertdata():
    print(' nama\n','nim\n','alamat\n')
    user = str(input("Apa yang ingin isi data : "))
    if user == 'nama':
        nama_baru = (input("Nama anda: "))
        nama.append(nama_baru)
    elif user == 'nim':
        nim_baru = (input("Nim anda :"))
        nim.append(nim_baru)
    elif user == 'alamat':
        alamat_baru = (input("Alamat anda :"))
        alamat.append(alamat_baru)
    else:
        print('Tidak ada pilihan coba lagi')
        insertdata()
        
def showmenu():
    print('--------- Menu ---------\n','1.Menampilakan data\n','2.Memasukan data\n','3.Keluar\n')
while True:
    showmenu()
    menu = input('Pilih menu no: ')
    if menu == '1':
        showdata()
    elif menu == '2':
        insertdata()
    elif menu == '3':
        print('Anda telah keluar')
        break
    else:
        print('TIdak ada dipilihan anda, Cobalagi')
