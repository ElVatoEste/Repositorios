from tkinter import *


ventana = Tk()
ventana.resizable(0, 0) 

signo = ""

def Sumar():

    _valor1 = float(Numero1.get())
    _valor2 = float(Numero2.get())
    _valor = _valor1+_valor2

    signo = "+"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(_valor1, signo, _valor2, _valor))

def Multiplicar():

    _valor1 = float(Numero1.get())
    _valor2 = float(Numero2.get())
    _valor = _valor1*_valor2

    signo = "*"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(_valor1, signo, _valor2, _valor))
    

def Restar():

    _valor1 = float(Numero1.get())
    _valor2 = float(Numero2.get())
    _valor = _valor1-_valor2

    signo = "-"

    Lbl4.config(text="Calculo matematico ingresado \n{} {} {} = {}".format(_valor1, signo, _valor2, _valor))


ventana.geometry("300x220")
ventana.title("Calculadora")

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


Numero1 = DoubleVar()
Numero2 = DoubleVar()

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