from tkinter import *

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Clases de python')

Lbl = Label(ventana, text='Hola prix').pack()
Lbl2 = Label(ventana, text='Centro').pack(anchor= CENTER)
Lbl3 = Label(ventana, text='Derecha').pack(anchor= NW)
Lbl4 = Label(ventana, text='Izquierda').pack(anchor= SE)

# Tamaño de ventana
ventana.geometry('500x500')

# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()