import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Note : sebaiknya pakai grid aja

class MainWindow(tk.Tk):
    def __init__(self,root):
        self.root = root
        root.geometry("300x200")
        root.resizable(False,False)
        root.title("Start")

        #frame setiap halaman
        self.frame_awal = ttk.Frame(root)
        self.frame_utama = ttk.Frame(root)
        self.frame_akhir = ttk.Frame(root)

        self.frame_awal.pack(fill="x",expand=True)

        #Halaman Awal
        awal_label = ttk.Label(self.frame_awal,text="Klik untuk memulai")
        awal_label.pack()
        start_button = ttk.Button(self.frame_awal,text="Start",command=self.ke_halaman_utama)
        start_button.pack()

        #Halaman utama
        utama_label = ttk.Label(self.frame_utama,text="Pilih bagunan dan klik generate")
        utama_label.pack()
        option_shape = ttk.OptionMenu(self.frame_utama,tk.StringVar(),"Option 1", "Option 1","Option 2","Option 3")
        option_shape.pack(side="left")
        value_entry = ttk.Entry(self.frame_utama)
        value_entry.pack(side="left")
        generate_button = ttk.Button(self.frame_utama,text="Generate",command=self.ke_halaman_akhir)
        generate_button.pack()
        quit_button = ttk.Button(self.frame_utama,text="Quit",command=root.destroy)
        quit_button.pack()

        # Menampilkan halaman awal saat aplikasi pertama kali dijalankan
        self.frame_awal.pack()
        self.frame_utama.pack_forget()
        self.frame_akhir.pack_forget()

    def ke_halaman_utama(self):
        '''Fungsi ke halaman utama'''
        root.title("Generate")
        self.frame_awal.pack_forget()
        self.frame_utama.pack()
        self.frame_akhir.pack_forget()

    def ke_halaman_akhir(self):
        '''Menampilkan Hasil'''
        hasil = "Hasilnya adalah :"
        showinfo(title="Hasil",message=hasil)

root = tk.Tk()
app = MainWindow(root)
root.mainloop()
