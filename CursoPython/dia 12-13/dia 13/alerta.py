from tkinter import *
from tkinter import messagebox

ventana = Tk()

def Mensaje():
    messagebox.showerror('Titulo', 'Contenido')
    pass

btn = Button(ventana, text='Mensaje', command=Mensaje)
btn.grid(column=0, row=0) 

ventana.mainloop()