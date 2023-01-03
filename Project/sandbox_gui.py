from tkinter import *
import solveSoal


class MainWindow():
    def __init__(self, root):
        self.root = root
        root.geometry('300x200')
        root.resizable(False, False)
    
    # frame utama
    self.main_frame = Frame(root)

    # halaman utama
    


if __name__ == '__main__':
    root = Tk()
    window = MainWindow(root)
    root.mainloop()