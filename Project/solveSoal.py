import initSoal
print('ini dari solveSoal')
"""
# bagian dict
class dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
# init var jawaban saat ini
ans = dictionary()
"""


def soalBaru():
    soal = initSoal.buatSoal()
    return soal

def kubus(s):
    """
    Mencari volume kubus       
    """
    print('Volume kubus tersebut adalah', s**3)

def balok(p, l, t):
    """
    Mencari volume balok       
    """
    print('Volume balok tersebut adalah', p*l*t)
    return (p*l*t)

def tabung(r, t):
    """
    Mencari volume tabung      
    """
    print('Volume tabung tersebut adalah', round((22/7)*(r**2)*t, 2))
    return (round((22/7)*(r**2)*t, 2))

def bejana(r1, r2, h1=None, h2=None):
    """
    Mencari tinggi salahh satu cairan
    """
    if(h1==None):
        print('Tinggi permukaan air tersebut adalah', round((r2*h2)/r1, 2))
        return(round((r2*h2)/r1, 2))
    else:
        print('Tinggi permukaan alkohol tersebut adalah', round((r1*h1)/r2, 2))
        return(round((r1*h1)/r2, 2))

# method untuk menjawab soal
def jawab(soal):
    if(soal.bentuk=='kubus'):
        return(soal.bentuk, kubus(soal.sisi))
    elif(soal.bentuk=='balok'):
        return(soal.bentuk, balok(soal.panjang, soal.lebar, soal.tinggi))
    elif(soal.bentuk=='tabung'):
        return(soal.bentuk, tabung(soal.jari, soal.tinggi))
    else:
        return(soal.bentuk, soal.know, bejana(soal.mAir, soal.mAlkohol, soal.hAir, soal.hAlkohol))


"""
# init var soal
soal = None

# membuat soal pada var soal
soalBaru()  #untuk membuat soal baru, tinggal panggil fungsi ini aja lalu pangil var soal untuk mendapatkan data tentang soal
jawaban = jawab(soal)
print(jawaban)
"""


"""
# langsung solve tanpa harus buat temporary var
for soal in quest:
    if(soal.bentuk=='kubus'):
        ans.add(soal.nama, kubus(soal.sisi))
    elif(soal.bentuk=='balok'):
        ans.add(soal.nama, balok(soal.panjang, soal.lebar, soal.tinggi))
    else:
        ans.add(soal.nama, tabung(soal.jari, soal.tinggi))
"""
# print('\n')

""" # for check the output        
for soal in initSoal.instances:
    print(soal.nama, soal.bentuk, ans[soal.nama])
"""
