from tkinter import *
import time

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Titulo')

# fuinciones
def Accion():
    ventana.iconify()
    time.sleep(0.5)
    ventana.deiconify()

    


Lbl = Label(ventana, text='Hola mundo')
Lbl.pack(anchor= CENTER)

Lbl.config(
    fg= 'blue',
    bg= 'red',
    font= ('Times', 10),
    cursor= 'watch'
)

# boton 
Btn = Button(ventana, text='Pulsar', command=Accion)
Btn.pack()
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    height= 10,
    width= 10
)


ventana.geometry('500x500')
# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()