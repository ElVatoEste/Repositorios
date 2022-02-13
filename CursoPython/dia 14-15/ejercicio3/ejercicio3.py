from tkinter import *

# Lo acabo de recuperar :'c

ventana1 = Tk()
# Proporciones de la ventana
ventana1.geometry("320x160")
ventana1.title("Convetidor de grados")
# Bloquea el tamaño de la ventana
ventana1.resizable(0, 0) 

# Ventana con fondo negro
ventana1.config(
    bg="black",
)


def Celcius():

    # Creacion de una ventana hija
    ventana2 = Toplevel()
    # Se hace casi lo mismo que en la ventana madre
    ventana2.resizable(0, 0) 
    ventana2.geometry("250x150")
    ventana2.title("Celcius")
    ventana2.config(
        bg="Black"
    )

    # Funcion ingresar para el boton
    def Ingresar():
        
        Cvalor1 = float(En1.get())
        Cvalor = (Cvalor1-32)*5/9
        L3.config(
            text=Cvalor
        )
       

    # Al estar ordenados automaticamente por pack(), no hay sectores definidos
    L1 = Label(ventana2, text="Fahrenheit")
    L1.pack()
    L1.config(
        bg="Black",
        fg="White"
    )

    # Se le dice al sistema que el valor a ingresar sera un flotante
    Grados = DoubleVar()
    
    En1 = Entry(ventana2, justify="center", textvariable=Grados)
    En1.pack()


    L2 = Label(ventana2, text="Celcius")
    L2.pack()
    L2.config(
        bg="Black",
        fg="White"
    )

    # Este label sera el que de la respuesta
    L3 = Label(ventana2, justify="center", text="")
    L3.pack()
    L3.config(
        bg="white",
        width=17,
    )

    Btn1 = Button(ventana2, text="Ingresar", command=Ingresar)
    Btn1.pack(pady=10)


def Fahrenheit():

    # Creacion de una ventana hija
    ventana3 = Toplevel()

    # Se hace casi lo mismo que en la ventana madre
    ventana3.resizable(0, 0) 
    ventana3.geometry("250x150")
    ventana3.title("Fahrenheit")
    ventana3.config(
        bg="Black"
    )

    # Funcion ingresar para el boton
    def Ingresar():
        
        Fvalor1 = float(En1.get())
        Fvalor = (Fvalor1*9/5)+32

        L3.config(
            text=Fvalor
        )
       
    # Al estar ordenados automaticamente por pack(), no hay sectores definidos
    L1 = Label(ventana3, text="Celcius")
    L1.pack()
    L1.config(
        bg="Black",
        fg="White"
    )

    # Se le dice al sistema que el valor a ingresar sera un flotante
    Grados = DoubleVar()
    
    En1 = Entry(ventana3, justify="center", textvariable=Grados)
    En1.pack()


    L2 = Label(ventana3, text="Fahrenheit")
    L2.pack()
    L2.config(
        bg="Black",
        fg="White"
    )

    # Este label sera el que de la respuesta
    L3 = Label(ventana3, justify="center", text="")
    L3.pack()
    L3.config(
        bg="white",
        width=17,
    )

    Btn1 = Button(ventana3, text="Ingresar", command=Ingresar)
    Btn1.pack(pady=10)


# codigo de la ventana madre

Texto1 = Label(ventana1, text="Bienvenido al sistema convertidor de grados\nSeleccione su opción")
Texto1.config(
    bg="black",
    fg="White",
    font=("Times", 12)
    )
Texto1.pack(anchor=CENTER)

# Seccion de botones --------------------------------------------
# A cada boton se le asigna su comando correspondiente.

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