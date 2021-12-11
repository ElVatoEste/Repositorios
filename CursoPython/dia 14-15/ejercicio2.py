from tkinter import *



signo = ""
def Multiplicar():
    
    _valor1 = int(Numero1.get())
    _valor2 = int(Numero2.get())
    _valor = _valor1+_valor2

    signo = "*"
    
    Lbl4 =  Label(ventana, text="Calculo matematico ingresado: \n{} {} {} = {}".format(_valor1, signo, Numero2, _valor))
    Lbl4.config(
        font= ('Times', 11),
    )

    Lbl4.place(x=20, y=160)




ventana = Tk()

ventana.geometry("300x230")
ventana.title("Registro de personas")

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



Lbl.pack()
Lbl2.place(x=45,y=35)
Lbl3.place(x=38,y=65)

Btn1 = Button(ventana, text='+', command=Multiplicar)
Btn1.pack(anchor=CENTER)
Btn1.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3
)


Btn2 = Button(ventana, text='-', command=Multiplicar)
Btn2.pack(anchor=CENTER)
Btn2.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3
)


Btn3 = Button(ventana, text='*', command=Multiplicar)
Btn3.pack(anchor=CENTER)
Btn3.config(
    font= ("Times", 20),
    cursor= 'arrow',
    width=3
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