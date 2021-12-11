from tkinter import *



ventana1 = Tk()
ventana1.geometry("320x160")
ventana1.title("Convetidor de grados")
ventana1.resizable(0, 0) 
ventana1.config(
    bg="black",
)

def Celcius():
    ventana1.iconify()
    ventana2 = Toplevel()

def Fahrenheit():
    ventana1.iconify()
    ventana3 = Toplevel()

Texto1 = Label(ventana1, text="Bienvenido al sistema convertidor de grados\nSeleccione su opción")
Texto1.config(
    bg="black",
    fg="White",
    font=("Times", 12)
    )
Texto1.pack(anchor=CENTER)

Boton1 = Button(ventana1, text="ºC", command=Celcius)
Boton1.config(
    bg="black",
    fg="White",
    font=("Times", 18),
    width=3
)
Boton2 = Frame(ventana1, text="ºF", command=Fahrenheit)
Boton2.config(
    bg="black",
    fg="White",
    font=("Times", 18),
    width=3
)

Boton1.place(x=110, y=60)
Boton2.place(x=170, y=60)


ventana1.mainloop()