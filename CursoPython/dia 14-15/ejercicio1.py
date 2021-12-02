from tkinter import *

ventana = Tk()

ventana.geometry("300x150")
ventana.title("Registro de personas")

Lbl = Label(ventana, text='Ingrese su primer nombre').pack(anchor= NW)
Lbl2 = Label(ventana, text='Ingrese su primer apellido').pack(anchor= NW)
Lbl3 = Label(ventana, text='Ingrese su edad').pack(anchor= NW)
Lbl4 = Label(ventana, text='Ingrese su profesión').pack(anchor= NW)

CT1 = Entry(ventana, justify='center').pack()
CT2 = Entry(ventana, justify='center').pack()
CT3 = Entry(ventana, justify='center').pack()
CT4 = Entry(ventana, justify='center').pack()

Ct1.

Btn = Button(ventana, text='Ingresar')
Btn.pack(anchor=CENTER)
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    width= 8
)

ventana.mainloop()