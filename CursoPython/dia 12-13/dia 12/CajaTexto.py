from tkinter import *
import time

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Titulo')

# fuinciones
def Accion():
    ventana.iconify()
    time.sleep(0.1)
    ventana.deiconify()

    


Lbl = Label(ventana, text='Hola mundo')
Lbl.pack(anchor= CENTER)

Lbl.config(
    fg= 'blue',
    bg= '#ff8003',
    font= ('Times', 10),
    cursor= 'watch'
)

# caja de texto
CT = Entry(ventana, justify='center').pack()


# boton 
Btn = Button(ventana, text='Pulsar', command=Accion)
Btn.pack()
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    height= 5,
    width= 10
)


ventana.geometry('500x500')
# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()