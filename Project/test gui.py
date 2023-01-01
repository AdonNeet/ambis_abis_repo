from tkinter import *
import random
root = Tk()
root.geometry('800x500')

fram1 = Frame(root)
fram2 = Frame(root)



root.resizable(False,False)
"""Mengakses gambar"""
img_tabung= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\tabung_new.gif')
img_kubus= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\kubus_new.gif')
img_balok= PhotoImage(file='C:\\Users\\Money\\Documents\\GitHub\\ambis_abis_repo\\Project\\image\\balok_new.gif')

"""Gui untuk tabung"""
def gmbr_tnbng():
        label = Label(root, image=img_tabung)
        label.place(x=50,y=5)
        teks1 = Label(root,text='Jari - Jari:', font=('Arial',20,'bold'))
        teks1.place(x=350,y=130)
        teks2 = Label(root,text='Tinggi :', font=('Arial',20,'bold'))
        teks2.place(x=350,y=180)
        teks3 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
        teks3.place(x=350,y=230)

        teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=350,y=280)
        jawaban = Entry(root, width= 20,borderwidth=3,font=('Arial',18))
        jawaban.place(x=350,y=330)
        but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20,command=check_tabung)
        but_aswer.place(x=620,y=325)
"""Gui untuk Kubus"""
def gmbr_kubus():
        label = Label(root, image=img_kubus)
        label.place(x=50,y=5)
        teks2 = Label(root,text='Sisi:', font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks4 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
        teks4.place(x=500,y=180)

        teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=60,y=350)
        jawaban = Entry(root, width= 40,borderwidth=3,font=('Arial',18))
        jawaban.place(x=60,y=400)

        but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20,command=check)
        but_aswer.place(x=589,y=396)
"""Gui untuk Balok"""
def gmbr_balok():
        label = Label(root, image=img_balok)
        label.place(x=50,y=50)
        teks1 = Label(root,text='Panjang :', font=('Arial',20,'bold'))
        teks1.place(x=500,y=80)
        teks2 = Label(root,text='Lebar:', font=('Arial',20,'bold'))
        teks2.place(x=500,y=130)
        teks3 = Label(root,text='Tinggi :', font=('Arial',20,'bold'))
        teks3.place(x=500,y=180)
        teks4 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
        teks4.place(x=500,y=230)

        teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
        teks5.place(x=60,y=300)
        jawaban = Entry(root, width= 40,borderwidth=3,font=('Arial',18))
        jawaban.place(x=60,y=350)

        but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20,command=check)
        but_aswer.place(x=589,y=346)

img = (img_tabung,img_kubus,img_balok)
"""Menciptakan soal random berserta gambarnya"""
def newpage():
        img_s = (random.choice(img))
        label = Label(root, image=img_s)
        if img_s == img_tabung:
            fram1.grid()
            gambartabung = Label(fram1, text=gmbr_tnbng())
            gambartabung.grid()
            def check_tabung():
                fram1.grid_forget()
                gambartabung.destroy()
                newpage()
            
        elif img_s == img_kubus:
            gmbr_kubus()
        elif img_s == img_balok:       
            gmbr_balok()
            
"""Membuat command untuk tombol cek pada tabung"""
def check_tabung():
        fram1.pack_forget()
        newpage()
def check():
        pass
def check():
        pass
"""Mencetak soal"""
label = Label(root, text=newpage())
label.grid()





root.mainloop()
"""
gui balok
label.place(x=50,y=50)
teks1 = Label(root,text='Panjang :', font=('Arial',20,'bold'))
teks1.place(x=500,y=80)
teks2 = Label(root,text='Lebar:', font=('Arial',20,'bold'))
teks2.place(x=500,y=130)
teks3 = Label(root,text='Tinggi :', font=('Arial',20,'bold'))
teks3.place(x=500,y=180)
teks4 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
teks4.place(x=500,y=230)

teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
teks5.place(x=60,y=300)
jawaban = Entry(root, width= 40,borderwidth=3,font=('Arial',18))
jawaban.place(x=60,y=350)

but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20)
but_aswer.place(x=589,y=346)
"""



""" gui kubus
label.place(x=50,y=5)
teks2 = Label(root,text='Sisi:', font=('Arial',20,'bold'))
teks2.place(x=500,y=130)
teks4 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
teks4.place(x=500,y=180)

teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
teks5.place(x=60,y=350)
jawaban = Entry(root, width= 40,borderwidth=3,font=('Arial',18))
jawaban.place(x=60,y=400)

but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20)
but_aswer.place(x=589,y=396)
"""
'''
gui tabung
label.place(x=50,y=5)
teks1 = Label(root,text='Jari - Jari:', font=('Arial',20,'bold'))
teks1.place(x=350,y=130)
teks2 = Label(root,text='Tinggi :', font=('Arial',20,'bold'))
teks2.place(x=350,y=180)
teks3 = Label(root,text='Volume : ?', font=('Arial',20,'bold'))
teks3.place(x=350,y=230)

teks5 = Label(root,text='Answer :', font=('Arial',20,'bold'))
teks5.place(x=350,y=280)
jawaban = Entry(root, width= 20,borderwidth=3,font=('Arial',18))
jawaban.place(x=350,y=330)

but_aswer = Button(root, text='Check', font=('Arial',14,'bold'),padx=20)

but_aswer.place(x=620,y=325)
'''


