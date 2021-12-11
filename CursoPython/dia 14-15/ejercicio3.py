from tkinter import *



ventana1 = Tk()
ventana1.geometry("320x160")
ventana1.title("Convetidor de grados")
ventana1.resizable(0, 0) 
ventana1.config(
    bg="black",
)

def Celcius():

    ventana2 = Toplevel()
    ventana2.resizable(0, 0) 
    ventana2.geometry("250x150")
    ventana2.title("Celcius")
    ventana2.config(
        bg="Black"
    )


    def Ingresar():
        
        _valor1 = float(En1.get())
        _valor = (_valor1-32)*5/9
        print(_valor)
        L3.config(
            text=_valor
        )
       

    L1 = Label(ventana2, text="Fahrenheit")
    L1.pack()
    L1.config(
        bg="Black",
        fg="White"
    )

    Grados = DoubleVar()
    
    En1 = Entry(ventana2, justify="center", textvariable=Grados)
    En1.pack()


    L2 = Label(ventana2, text="Celcius")
    L2.pack()
    L2.config(
        bg="Black",
        fg="White"
    )


    L3 = Label(ventana2, justify="center", text="***")
    L3.pack()
    L3.config(
        bg="white",
        width=17,
    )

    Btn1 = Button(ventana2, text="Ingresar", command=Ingresar)
    Btn1.pack(pady=10)


def Fahrenheit():

    ventana3 = Toplevel()
    ventana3.resizable(0, 0) 
    ventana3.geometry("250x150")
    ventana3.title("Fahrenheit")
    ventana3.config(
        bg="Black"
    )


    def Ingresar():
        
        _valor1 = float(En1.get())
        _valor = (_valor1*9/5)+32
        print(_valor)
        L3.config(
            text=_valor
        )
       

    L1 = Label(ventana3, text="Celcius")
    L1.pack()
    L1.config(
        bg="Black",
        fg="White"
    )

    Grados = DoubleVar()
    
    En1 = Entry(ventana3, justify="center", textvariable=Grados)
    En1.pack()


    L2 = Label(ventana3, text="Fahrenheit")
    L2.pack()
    L2.config(
        bg="Black",
        fg="White"
    )


    L3 = Label(ventana3, justify="center", text="***")
    L3.pack()
    L3.config(
        bg="white",
        width=17,
    )

    Btn1 = Button(ventana3, text="Ingresar", command=Ingresar)
    Btn1.pack(pady=10)



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