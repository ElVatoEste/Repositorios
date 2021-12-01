from tkinter import *
import tkinter

ventana = Tk()


ventana.title('The game')
ventana.geometry('700x420')
ventana.resizable(0, 0) 

back = tkinter.Frame(master=ventana,bg='black')
back.pack_propagate(0)
back.pack(fill=tkinter.BOTH, expand=1)

img = PhotoImage(file="CursoPython\Proyectos\ProyectoFinal\Imagen.png")

lbl_image = Label(ventana, image=img).pack()

NombreUsuario = Entry(ventana, justify='center')
NombreUsuario.pack()
NombreUsuario.config(
    bg="white",
    fg="black",
    font= ('Times', 11),
    cursor= 'arrow',
    width= 20
)
NombreUsuario.place(x= 420, y=150)

IniciarSecion = Button(ventana, text='iniciar sesión')
IniciarSecion.pack()
IniciarSecion.config(
    bg="#818181",
    fg="black",
    font= ('Times', 10),
    cursor= 'arrow',
    height= 1,
    width= 30
)

IniciarSecion.place(x= 410.5, y=250)

ventana.mainloop()