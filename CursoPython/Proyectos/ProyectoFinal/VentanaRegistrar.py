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
    IngreApellido.pack()
    IngreApellido.config(
        font= ('Times', 15),
        fg="black",
    )

    Correo = Label(ventana3, text="Correo")
    Correo.pack()
    Correo.config(
        font= ('Times', 15),
        fg="black",
    )
    
    IngreUsuario = Label(ventana3, text="Usuario")
    IngreUsuario.pack()
    IngreUsuario.config(
        font= ('Times', 15),
        fg="black",
    )

    IngreContraseña = Label(ventana3, text="Contraseña")
    IngreContraseña.pack()
    IngreContraseña.config(
        font= ('Times', 15),
        fg="black",
    )

    Texto1.place(x=75, y=3)
    IngreNombre.place(x=3, y=40)
    IngreApellido.place(x=3, y=70)
    Correo.place(x=3, y=100)
    IngreUsuario.place(x=3, y=130)
    IngreContraseña.place(x=3, y=160)


    # Entrys

    Nombre3 = StringVar
    Apellido3 = StringVar
    Correo3 = StringVar
    Usuario3 = StringVar
    Contraseña3 = StringVar


    Entry1 = Entry(ventana3, justify='center', textvariable=Nombre3)
    Entry1.pack()
    Entry1.config(
        bg="white",
        fg="black",
        font= ('Times', 11),
        width= 25
    )

    Entry2 = Entry(ventana3, justify='center', textvariable=Apellido3)
    Entry2.pack()
    Entry2.config(
        bg="white",
        fg="black",
        font= ('Times', 11),
        width= 25
    )

    Entry3 = Entry(ventana3, justify='center', textvariable=Correo3)
    Entry3.pack()
    Entry3.config(
        bg="white",
        fg="black",
        font= ('Times', 11),
        width= 25
    )

    Entry4 = Entry(ventana3, justify='center', textvariable=Usuario3)
    Entry4.pack()
    Entry4.config(
        bg="white",
        fg="black",
        font= ('Times', 11),
        width= 25
    )

    Entry5 = Entry(ventana3, justify='center', textvariable=Contraseña3)
    Entry5.pack()
    Entry5.config(
        bg="white",
        fg="black",
        font= ('Times', 11),
        width= 25
    )

    Entry1.place(x= 110, y=42.5)
    Entry2.place(x= 110, y=72.5)
    Entry3.place(x= 110, y=102.5)
    Entry4.place(x= 110, y=132.5)
    Entry5.place(x= 110, y=162.5)
 
    # Button
    def Registro():
        Usuarios.setdefault(Entry4.get(),{"password": Entry5.get})

    Registrar3 = Button(ventana3, text='Registrar', command=Registro)
    Registrar3.pack()
    Registrar3.config(
        fg="black",
        font= ('Times', 10),
        cursor= 'arrow',
        height= 1,
        width= 30
    )

      



    ventana3.mainloop() 


Registrar()