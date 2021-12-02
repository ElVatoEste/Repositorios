from tkinter import *
from Usuarios import Usuarios

def Registrar():

    ventana3 = Tk()
    ventana3.title('VatGram')
    ventana3.iconbitmap("CursoPython\Proyectos\ProyectoFinal\imagenes\icon.ico")
    ventana3.geometry('300x250')
    ventana3.resizable(0, 0) 

    back = Frame(master=ventana3)
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    

    Texto1 = Label(ventana3, text="Ingrese sus datos")
    Texto1.pack()
    Texto1.config(
        font= ('Times', 15),
        fg="black",
    )
    
    IngreNombre = Label(ventana3, text="Nombre")
    IngreNombre.pack()
    IngreNombre.config(
        font= ('Times', 15),
        fg="black",
    )

    IngreApellido = Label(ventana3, text="Apellido")
    IngreNombre.pack()
    IngreNombre.config(
        font= ('Times', 15),
        fg="black",
    )

    Correo = Label(ventana3, text="Correo")
    IngreNombre.pack()
    IngreNombre.config(
        font= ('Times', 15),
        fg="black",
    )
    
    IngreUsuario = Label(ventana3, text="Usuario")
    IngreNombre.pack()
    IngreNombre.config(
        font= ('Times', 15),
        fg="black",
    )

    IngreContraseña = Label(ventana3, text="Contraseña")
    IngreNombre.pack()
    IngreNombre.config(
        font= ('Times', 15),
        fg="black",
    )

    Texto1.place(x=75, y=3)
    IngreNombre.place(x=3, y=40)
    IngreApellido.place(x=3, y=40)
    Correo.place(x=3, y=40)
    IngreUsuario.place(x=3, y=40)
    IngreContraseña.place(x=3, y=40)




    ventana3.mainloop()

Registrar()