from tkinter import *

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Titulo')

Lbl = Label(ventana, text='Primer mensaje')
Lbl2 = Label(ventana, text='Segundo mensaje')
Lbl3 = Label(ventana, text='Tercer mensaje')
Lbl.pack(anchor= CENTER)

Lbl.config(
    fg= 'blue',
    bg= 'gray',
    font= ('Times', 24),
    cursor= 'watch'
)
Lbl2.config(
    fg= 'red',
    font= ('Arial', 24),
    cursor= 'cross'
)


Lbl.grid(column= 0, row=0)
Lbl2.grid(column= 2, row=2)
Lbl3.grid(column= 3, row=3)

# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()