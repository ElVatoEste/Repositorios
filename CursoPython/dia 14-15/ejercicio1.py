from tkinter import *
from tkinter import messagebox

def Mensaje():

    c1 = CT1.get()
    c2 = CT2.get()
    c3 = CT3.get()
    c4 = CT4.get()

    if c1 == "" or c2 == "" or c3 == "" or c4 == "":
        messagebox.showerror("Error", "Un campo esta vacio")
    else:
        textolargo = (f"{CT1.get()} {CT2.get()} es una persona de {CT3.get()} años y es {CT4.get()}") 
        Lbl5.configure(text= textolargo)


ventana = Tk()

ventana.geometry("300x150")
ventana.title("Registro de personas")

Lbl = Label(ventana, text='Ingrese su primer nombre').pack(anchor= NW)
Lbl2 = Label(ventana, text='Ingrese su primer apellido').pack(anchor= NW)
Lbl3 = Label(ventana, text='Ingrese su edad').pack(anchor= NW)
Lbl4 = Label(ventana, text='Ingrese su profesión').pack(anchor= NW)
Lbl5 = Label(ventana, text="")
Lbl5.pack()

CT1 = Entry(ventana, justify='center')
CT2 = Entry(ventana, justify='center')
CT3 = Entry(ventana, justify='center')
CT4 = Entry(ventana, justify='center')

CT1.place(x=170, y=0)
CT2.place(x=170, y=20)
CT3.place(x=170, y=40)
CT4.place(x=170, y=60)

Btn = Button(ventana, text='Ingresar', command=Mensaje)
Btn.pack(anchor=CENTER)
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    width= 8
)
Btn.place(x=125,y=110)

ventana.mainloop()