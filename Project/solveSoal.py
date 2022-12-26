import initSoal
print('ini dari solveSoal')
# bagian dict
class dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
# init dict
ans = dictionary()

def kubus(s):
        """
        Mencari volume kubus       
        """
        print('Volume kubus tersebut adalah', s**3)
        return (s**3)
        
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

quest = initSoal.instances

# langsung solve tanpa harus buat temporary var
for soal in quest:
    if(soal.bentuk=='kubus'):
        ans.add(soal.nama, kubus(soal.sisi))
    elif(soal.bentuk=='balok'):
        ans.add(soal.nama, balok(soal.panjang, soal.lebar, soal.tinggi))
    else:
        ans.add(soal.nama, tabung(soal.jari, soal.tinggi))

print('\n')

""" # for check the output        
for soal in initSoal.instances:
    print(soal.nama, soal.bentuk, ans[soal.nama])
"""
