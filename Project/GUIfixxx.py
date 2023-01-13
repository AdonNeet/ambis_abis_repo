from tkinter import *
from pathlib import Path as p
import platform
import random
import data as d
from tkinter.messagebox import showinfo

# mencari current working directory
tmp = str(p.cwd())
print(tmp)

class Window1(Tk):
    def __init__(self):
        super().__init__()
        self.tinggi = str(d.tb.tinggi)
        self.jari = str(d.tb.jari)
        self.geometry("800x500")
        self.title("Window 1")
        self.resizable(False,False)
        if(platform.system()=='Linux'):
            self.img_tabung= PhotoImage(file=tmp+'/image/tabung_new.gif')
        else:
            self.img_tabung= PhotoImage(file=tmp+'\\image\\tabung_new.gif')
        self.ans = StringVar()
        
        gambartabung = Label(self, image=self.img_tabung)
        gambartabung.place(x=50,y=5)
        teks1 = Label(self,text='Jari - Jari: '+self.jari, font=('Arial',20,'bold'))
        teks1.place(x=350,y=130)
        teks2 = Label(self,text='Tinggi :'+self.tinggi, font=('Arial',20,'bold'))
        teks2.place(x=350,y=180)
        teks3 = Label(self,text='Volume air : ?', font=('Arial',20,'bold'))
        teks3.place(x=350,y=230)

        teks5 = Label(self,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=350,y=280)
        jawaban = Entry(self, width= 20,borderwidth=3,font=('Arial',18),textvariable=self.ans)
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
        if(platform.system()=='Linux'):
            self.img_kubus= PhotoImage(file=tmp+'/image/kubus_new.gif')
        else:
            self.img_kubus= PhotoImage(file=tmp+'\\image\\kubus_new.gif')
        self.sisi = str(d.k.sisi)
        self.ans = StringVar()
        
        gambarkubus = Label(self, image=self.img_kubus)
        gambarkubus.place(x=50,y=5)
        teks2 = Label(self,text='Sisi: '+self.sisi, font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks4 = Label(self,text='Volume air : ?', font=('Arial',20,'bold'))
        teks4.place(x=500,y=180)

        teks5 = Label(self,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=60,y=350)
        jawaban = Entry(self, width= 40,borderwidth=3,font=('Arial',18),textvariable=self.ans)
        jawaban.place(x=60,y=400)

        but_aswer = Button(self, text='Check', font=('Arial',14,'bold'),padx=20,command=d.k.check)
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
        if(platform.system()=='Linux'):
            self.img_balok= PhotoImage(file=tmp+'/image/balok_new.gif')
        else:
            self.img_balok= PhotoImage(file=tmp+'\\image\\balok_new.gif')
        self.panjang = str(d.b.panjang)
        self.lebar = str(d.b.lebar)
        self.tinggi = str(d.b.tinggi)


        gambarbalok = Label(self, image=self.img_balok)
        gambarbalok.place(x=50,y=50)
        teks1 = Label(self,text='Panjang :'+self.panjang, font=('Arial',20,'bold'))
        teks1.place(x=500,y=80)
        teks2 = Label(self,text='Lebar:'+self.lebar, font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks3 = Label(self,text='Tinggi :'+self.tinggi, font=('Arial',20,'bold'))
        teks3.place(x=500,y=180)
        teks4 = Label(self,text='Volume air: ?', font=('Arial',20,'bold'))
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

__name__ = "__main__"

if __name__ == "__main__":
    start_window = random.choice([Window1, Window2, Window3, Window4])
    window1 = start_window()
    window1.mainloop()

