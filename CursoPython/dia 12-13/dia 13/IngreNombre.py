from tkinter import *

ventana = Tk()
ventana.config(bd=25, bg="gray")

nom = StringVar()
nom1 = StringVar()


Label(ventana, text="Ingrese el nombre:").pack()

Entry(ventana, justify="center", textvariable=nom1).pack()


Label(ventana, text="Nombre ingresado:").pack()

Entry(ventana, justify="center", textvariable=nom, state="disabled").pack()

def Ingresar():
    nom.set(nom1.get())

Button(ventana, text="Ingresar", command=Ingresar).pack()

ventana.mainloop()