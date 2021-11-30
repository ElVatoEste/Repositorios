from tkinter import *
from tkinter.ttk import *


ventana = Tk()

Hombre = Radiobutton(ventana, text='Hombre', value='Hombre')
Hombre.grid(column=0, row=0)

Mujer = Radiobutton(ventana, text='Mujer', value='Mujer')
Mujer.grid(column=1, row=0)

ventana.mainloop()