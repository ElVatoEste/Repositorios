from tkinter import *

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Titulo')

Lbl = Label(ventana, text='Hola mundo')
Lbl.pack(anchor= CENTER)

# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()