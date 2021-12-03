from tkinter import *


def AbrirVentana2():

    Ventana2 = Tk()
    Ventana2.title('VatGram')
    Ventana2.iconbitmap("ProyectoFinal\imagenes\icon.ico")
    Ventana2.geometry('600x600')
    Ventana2.resizable(0, 0) 

    back = Frame(master=Ventana2,bg='black')
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    Ventana2.mainloop()
