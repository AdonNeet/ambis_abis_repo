import tkinter as tk
import random

# fungsi untuk menghitung volume air
def hitung_volume():
    # ambil nilai random untuk panjang, lebar, dan tinggi
    panjang = random.randint(1,10)
    lebar = random.randint(1,10)
    tinggi = random.randint(1,10)

    # hitung volume
    volume = panjang * lebar * tinggi

    # tampilkan hasilnya
    hasil_.config(text=volume)
    panjang_.config(text=panjang)
    lebar_.config(text=lebar)
    tinggi_.config(text=tinggi)

# buat form utama
root = tk.Tk()
root.title("Volume Air")
root.geometry("300x200")
root.resizable(False,False)

# Frame
frame_utama = tk.Frame(root)
frame_utama.grid(padx=70,pady=30)

# Label
panjang_ = tk.Label(frame_utama,text="")
panjang_label = tk.Label(frame_utama,text="Panjang :")

lebar_ = tk.Label(frame_utama,text="")
lebar_label = tk.Label(frame_utama,text="Lebar :")

tinggi_ = tk.Label(frame_utama,text="")
tinggi_label = tk.Label(frame_utama,text="Tinggi :")

hasil_ = tk.Label(frame_utama,text="")
hasil_label = tk.Label(frame_utama,text="Volome air :")

# Button
hitung_button = tk.Button(frame_utama,text="Hitung", command=hitung_volume)

# letakkan tombol dan label ke dalam form
panjang_label.grid(row=0,column=0)
panjang_.grid(row=0,column=1)

lebar_label.grid(row=1,column=0)
lebar_.grid(row=1,column=1)

tinggi_label.grid(row=2,column=0)
tinggi_.grid(row=2,column=1)

hasil_label.grid(row=3,column=0)
hasil_.grid(row=3,column=1)

hitung_button.grid(row=4)

# jalankan GUI
root.mainloop()