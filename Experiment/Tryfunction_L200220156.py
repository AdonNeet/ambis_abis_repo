class JajarGenjang(object):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        L = self.alas * self.tinggi
        return L

JajarGenjang1 = JajarGenjang(3, 5)
print(JajarGenjang1.luas())