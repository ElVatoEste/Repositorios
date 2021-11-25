from tkinter import *

# CREACION DE VENTANA
ventana = Tk()

ventana.title('Titulo')

Lbl = Label(ventana, text='Hola mundo')
Lbl.pack(anchor= CENTER)

Lbl.config(
    fg= 'blue',
    bg= 'red',
    font= ('Times', 10),
    cursor= 'watch'
)

# boton 
Btn = Button(ventana, text='Pulsar')
Btn.pack()
Btn.config(
    font= ('Times', 10),
    cursor= 'arrow',
    height=(20)
)


ventana.geometry('500x500')
# Creacion de ciclo para mantener ventana abierta
ventana.mainloop()