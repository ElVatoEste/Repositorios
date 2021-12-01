from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox

# -------------------------------------------------------

Usuarios = {
    "Admin":{"password":"abcd23"} 

}
# ----------------------------

Usu = StringVar
Contra = StringVar


def Verificar():
    if Usu in Usuarios:
        if Contra == Usuarios[Usu]["password"]:
            print("Hola xd")
        else:
            print("Contraseña invalida")

    elif Usu not in Usuarios:
        print("Usuario invalido")
        

# -------------------------------------------------------


#-------------------------------------
# diseño

ventana = Tk()


ventana.title('VatGram')
ventana.tk.call('wm', 'iconphoto', ventana._w, tkinter.PhotoImage(file="CursoPython\Proyectos\ProyectoFinal\icon.png"))
ventana.geometry('700x420')
ventana.resizable(0, 0) 

back = tkinter.Frame(master=ventana,bg='black')
back.pack_propagate(0)
back.pack(fill=tkinter.BOTH, expand=1)

img = PhotoImage(file="CursoPython\Proyectos\ProyectoFinal\Imagen.png")

lbl_image = Label(ventana, image=img).pack()
# ------------------------------------------------


# ---------------------------------------------------------------------
# Caja de texto 

NombreUsuario = Entry(ventana, justify='center', textvariable=Usu)
NombreUsuario.pack()
NombreUsuario.config(
    bg="white",
    fg="black",
    font= ('Times', 11),
    cursor= 'arrow',
    width= 20
)
NombreUsuario.place(x= 420, y=150)

ContraseñaUsuario = Entry(ventana, justify='center', textvariable=Contra)
ContraseñaUsuario.pack()
ContraseñaUsuario.config(
    bg="white",
    fg="black",
    font= ('Times', 11),
    cursor= 'arrow',
    width= 20
)
ContraseñaUsuario.place(x= 420, y=200)

# -------------------------------------------------------------



IniciarSecion = Button(ventana, text='iniciar sesión', command=Verificar)
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