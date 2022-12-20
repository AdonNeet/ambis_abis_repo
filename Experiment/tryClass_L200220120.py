class Product:
    __vendor_message = "bayar sesuai dengan harga tertera"
    name = ""
    price = ""
    size = ""
    unit = ""

    def __init__(self, name):
        "Ini adalah constructor"
        self.name = name
        self.unit = "ml"
        self.size = 250

    def get_vendor_message(self):
        print(self.__vendor_message)

    def set_price(self, price):
        self.price = price

p = Product("milkuat")
p.set_price(5500)
print("%s dengan ukuran %d %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))
p2 = Product("teh gelas")
p2.set_price(4500)
print("%s dengan ukuran %d %s harganya Rp. %d" % (p2.name, p2.size, p2.unit, p2.price))

p.get_vendor_message()

