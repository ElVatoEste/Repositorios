from tkinter import *

def Registrar():

    ventana3 = Tk()
    ventana3.title('VatGram')
    ventana3.iconbitmap("CursoPython\Proyectos\ProyectoFinal\imagenes\icon.ico")
    ventana3.geometry('700x420')
    ventana3.resizable(0, 0) 

    back = Frame(master=ventana3,bg='black')
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    ventana3.mainloop()

    Login =  Label(ventana3, text="Usuario")
    Login.config(
        font= ('Times', 11)
    )
    Login.place(x=100, y=100)