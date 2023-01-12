import random
from tkinter import *
import tkin_sb as t
from tkinter.messagebox import showinfo

class kubus:
    def __init__(self, sisi):
        self.sisi = sisi
    def check(self):
        # Ambil jawaban dari input user
        answer = t.ans.get()      

        # Hitung volume kubus
        volume = self.sisi ** 3

        # Cek apakah jawaban sesuai dengan hasil perhitungan
        if answer == str(volume):
            # Tampilkan pesan informasi jika jawaban benar
            showinfo("Information", "Jawaban Anda benar!")
            t.cetak()
        else:
            # Tampilkan pesan error jika jawaban salah
            showinfo("Error", "Jawaban Anda salah!\nSilahkan coba lagi!")
k = kubus(random.randint(1, 50))

class tabung:
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi
    def check(self):
        # Ambil jawaban dari input user
        answer = t.ans.get()      

        # Hitung volume tabung
        volume = round((22/7)*(self.jari ** 2)*self.tinggi, 2)

        # Cek apakah jawaban sesuai dengan hasil perhitungan
        if answer == str(volume):
            # Tampilkan pesan informasi jika jawaban benar
            showinfo("Information", "Jawaban Anda benar!")
            t.cetak()
        else:
            # Tampilkan pesan error jika jawaban salah
            showinfo("Error", "Jawaban Anda salah!\nSilahkan coba lagi!")
tb = tabung(jari=random.randint(1, 50), tinggi=random.randint(1, 50))


class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def check(self):
        # Ambil jawaban dari input user
        answer = t.ans.get()      

        # Hitung volume balok
        volume = self.panjang * self.lebar * self.tinggi

        # Cek apakah jawaban sesuai dengan hasil perhitungan
        if answer == str(volume):
            # Tampilkan pesan informasi jika jawaban benar 
            showinfo("Information", "Jawaban Anda benar!")
            t.cetak()
        else:
            # Tampilkan pesan error jika jawaban salah
            showinfo("Error", "Jawaban Anda salah!\nSilahkan coba lagi!")
b = balok(panjang=random.randint(1, 50), lebar=random.randint(1, 50), tinggi=random.randint(1, 50))

# acak soal lagi, tinggal buat cara manggil soal lagi dari class diatas
def acak():
    k = kubus(random.randint(1, 50))
    tb = tabung(jari=random.randint(1, 50), tinggi=random.randint(1, 50))
    b = balok(panjang=random.randint(1, 50), lebar=random.randint(1, 50), tinggi=random.randint(1, 50))