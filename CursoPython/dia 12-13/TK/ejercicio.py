from tkinter import *

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Clases de python')

Lbl = Label(ventana, text='Bienvenidos')
Btn = Button(ventana, text='Click 1')
Btn2 = Button(ventana, text='Click 2')
Cajat = Entry(ventana, justify='center')

Lbl.pack()

Lbl.config(
    background='black',
    foreground='white',
    anchor= CENTER,
    font=('Time', 30),
    width=20,
    height=3
)

Btn.config(
    background='blue',
    foreground='white',
    anchor= CENTER,
    font=('Time', 15),
    width=12,
    height=3
)

Btn2.config(
    background='blue',
    foreground='white',
    anchor= CENTER,
    font=('Time', 15),
    width=12,
    height=3
)


Lbl.place(x= 0, y=0)
Btn.place(x= 0, y=161)
Btn2.place(x= 324, y=161)
Cajat.place(x=0, y= 500)


ventana.geometry('500x500')

ventana.mainloop()