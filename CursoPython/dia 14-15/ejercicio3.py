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
    ventana2.geometry("300x220")
    ventana2.title("Registro de personas")

    Lbl = Label(ventana2, text='Caculadora python')
    Lbl.config(
        font=("Times", 20),
    )

    Lbl2 =  Label(ventana2, text="Ingrese su primer numero:")
    Lbl2.config(
        font= ('Times', 11),
    )

    Lbl3 =  Label(ventana2, text="Ingrese su segundo numero:")
    Lbl3.config(
        font= ('Times', 11),
    )

    Lbl4 =  Label(ventana2, text="Calculo matematico ingresado")
    Lbl4.config(
        font= ('Times', 15),
    )

    Lbl.pack()
    Lbl2.place(x=45,y=35)
    Lbl3.place(x=38,y=65)
    Lbl4.pack(side = BOTTOM)

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
    bg="white",
    font=("Times", 18),
    width=3
)
Boton2 = Button(ventana1, text="ºF", command=Fahrenheit)
Boton2.config(
    bg="white",
    font=("Times", 18),
    width=3
)

Boton1.place(x=110, y=60)
Boton2.place(x=170, y=60)


ventana1.mainloop()