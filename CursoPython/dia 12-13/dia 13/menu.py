from tkinter import *

Ventana = Tk()

menubar = Menu(Ventana)

Ventana.config(menu=menubar)

SegundoMenu = Menu(menubar, tearoff=0)
SegundoMenu.add_command(label="Nuevo")
SegundoMenu.add_separator()
SegundoMenu.add_command(label="Salir", command=Ventana.quit)

menubar.add_cascade(label="Archivo", menu=SegundoMenu)
menubar.add_cascade(label="Editar")
menubar.add_cascade(label="Ayuda")

Ventana.mainloop()