from tkinter import *

def Mensaje():

    #basico
    print("hola")


ventana = Tk()

ventana.geometry("300x300")
ventana.title("Registro de personas")

Lbl = Label(ventana, text='Caculadora python')
Lbl.pack()
Lbl.config(
    font=("Times", 20),
)

Lbl2 =  Label(ventana, text="Ingrese su primer numero:")
Lbl2.config(
    font= ('Times', 11),
)

Lbl2.place(x=45,y=35)

Numero1 = IntVar

Btn = Button(ventana, text='Ingresar', command=Mensaje)
Btn.pack(anchor=CENTER)
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    width= 8
)
Btn.place(x=125,y=110)

ventana.mainloop()