from tkinter import *


ventana = Tk()

# Esta linea me permite establer una medida fija, es decir no se puede ni expandir ni contraer la ventana
ventana.resizable(0, 0) 

signo = ""

# Defincion de funciones
def Sumar():

    zvalor1 = float(Numero1.get())
    zvalor2 = float(Numero2.get())
    zvalor = zvalor1+zvalor2

    signo = "+"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(zvalor1, signo, zvalor2, zvalor))

def Multiplicar():

    xvalor1 = float(Numero1.get())
    xvalor2 = float(Numero2.get())
    xvalor = xvalor1*xvalor2

    signo = "*"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(xvalor1, signo, xvalor2, xvalor))
    

def Restar():

    rvalor1 = float(Numero1.get())
    rvalor2 = float(Numero2.get())
    rvalor = rvalor1-rvalor2

    signo = "-"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(rvalor1, signo, rvalor2, rvalor))

# medida de la ventana
ventana.geometry("300x220")
ventana.title("Calculadora")


# Sector de los Labels --------------------------------------
Lbl = Label(ventana, text='Caculadora python')
Lbl.config(
    font=("Times", 20),
)

Lbl2 =  Label(ventana, text="Ingrese su primer numero:")
Lbl2.config(
    font= ('Times', 11),
)

Lbl3 =  Label(ventana, text="Ingrese su segundo numero:")
Lbl3.config(
    font= ('Times', 11),
)

Lbl4 =  Label(ventana, text="Calculo matematico ingresado")
Lbl4.config(
    font= ('Times', 15),
)

Lbl.pack()
Lbl2.place(x=45,y=35)
Lbl3.place(x=38,y=65)
Lbl4.pack(side = BOTTOM)

# Sector de botones ---------------------------------------------------------

Btn1 = Button(ventana, text='+', command=Sumar)
Btn1.pack(anchor=CENTER)
Btn1.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3,
    bg=("#f7bd56")
)


Btn2 = Button(ventana, text='-', command=Restar)
Btn2.pack(anchor=CENTER)
Btn2.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3,
    bg="#9acfdd"
)


Btn3 = Button(ventana, text='*', command=Multiplicar)
Btn3.pack(anchor=CENTER)
Btn3.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3,
    bg="#Cb82ff"
)

Btn1.place(x=60,y=100)
Btn2.place(x=130,y=100)
Btn3.place(x=200,y=100)

# decile al sistema que los valores que se ingresaran seran flotantes
Numero1 = DoubleVar()
Numero2 = DoubleVar()

# Sector de las entrys ----------------------------------------------
NumeroUno = Entry(ventana, textvariable=Numero1)
NumeroUno.pack()
NumeroUno.config(
    font= ('Times', 10),
    width= 7
)

NumeroDos = Entry(ventana, textvariable=Numero2)
NumeroDos.pack()
NumeroDos.config(
    font= ('Times', 10),
    width= 7
)

NumeroUno.place(x=215,y=37)
NumeroDos.place(x=215,y=67)

ventana.mainloop()