from tkinter import *
import random

from tkinter.messagebox import showinfo
class Window1(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("Window 1")
        self.resizable(False,False)
        self.img_tabung= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\tabung_new.gif')
        
        gambartabung = Label(self, image=self.img_tabung)
        gambartabung.place(x=50,y=5)
        teks1 = Label(self,text='Jari - Jari: ', font=('Arial',20,'bold'))
        teks1.place(x=350,y=130)
        teks2 = Label(self,text='Tinggi :', font=('Arial',20,'bold'))
        teks2.place(x=350,y=180)
        teks3 = Label(self,text='Volume : ?', font=('Arial',20,'bold'))
        teks3.place(x=350,y=230)

        teks5 = Label(self,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=350,y=280)
        jawaban = Entry(self, width= 20,borderwidth=3,font=('Arial',18))
        jawaban.place(x=350,y=330)
        but_aswer = Button(self, text='Check', font=('Arial',14,'bold'),padx=20,command=self.go_to_random_window)
        but_aswer.place(x=620,y=325)

    def go_to_random_window(self):
        self.destroy()
        next_window = random.choice([Window2, Window3, Window4])
        window = next_window()

class Window2(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Window 2")
        self.resizable(False,False)
        self.img_kubus= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\kubus_new.gif')
        
        gambarkubus = Label(self, image=self.img_kubus)
        gambarkubus.place(x=50,y=5)
        teks2 = Label(self,text='Sisi: ', font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks4 = Label(self,text='Volume : ?', font=('Arial',20,'bold'))
        teks4.place(x=500,y=180)

        teks5 = Label(self,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=60,y=350)
        jawaban = Entry(self, width= 40,borderwidth=3,font=('Arial',18))
        jawaban.place(x=60,y=400)

        but_aswer = Button(self, text='Check', font=('Arial',14,'bold'),padx=20,command=self.go_to_random_window)
        but_aswer.place(x=589,y=396)

    def go_to_random_window(self):
        self.destroy()
        next_window = random.choice([Window1, Window3, Window4])
        window = next_window()

class Window3(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Window 3")
        self.resizable(False,False)
        self.img_balok= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\balok_new.gif')

        gambarbalok = Label(self, image=self.img_balok)
        gambarbalok.place(x=50,y=50)
        teks1 = Label(self,text='Panjang :', font=('Arial',20,'bold'))
        teks1.place(x=500,y=80)
        teks2 = Label(self,text='Lebar:', font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks3 = Label(self,text='Tinggi :', font=('Arial',20,'bold'))
        teks3.place(x=500,y=180)
        teks4 = Label(self,text='Volume : ?', font=('Arial',20,'bold'))
        teks4.place(x=500,y=230)

        teks5 = Label(self,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=60,y=300)
        jawaban = Entry(self, width= 40,borderwidth=3,font=('Arial',18))
        jawaban.place(x=60,y=350)

        but_aswer = Button(self, text='Check', font=('Arial',14,'bold'),padx=20,command=self.go_to_random_window)
        but_aswer.place(x=589,y=346)

    def go_to_random_window(self):
        self.destroy()
        next_window = random.choice([Window1, Window2, Window4])
        window = next_window()

class Window4(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Window 4")
        self.resizable(False,False)

        self.button = Button(self, text="Next", command=self.go_to_random_window)
        self.button.pack()

    def go_to_random_window(self):
        self.destroy()
        next_window = random.choice([Window1, Window2, Window3])
        window = next_window()

if __name__ == "__main__":
    start_window = random.choice([Window1, Window2, Window3, Window4])
    window1 = start_window()
    window1.mainloop()

