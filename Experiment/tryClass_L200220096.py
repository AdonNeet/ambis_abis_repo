class Data:
    name = str
    nim = str

data1 = Data()

data1.name = "Muhammad Ardhan Aulia Rahman"
data1.nim = "L200220096"

print("Nama : ", data1.name, "NIM : ", data1.nim)

print("\n-----------------------------------------------")

class Cat:
	def __init__(self, type, color):
		self.type = type
		self.color = color

Moly = Cat("Local", "White")
Pipo = Cat("Persia", "Black White")

print('\nMoly details:')
print('Type: ', Moly.type)
print('Color: ', Moly.color)

print('\nBuzo details:')
print('Type: ', Pipo.type)
print('Color: ', Pipo.color)
