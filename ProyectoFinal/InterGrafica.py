from tkinter import *
from tkinter import messagebox
from ventana2 import AbrirVentana2
from VentanaRegistrar import Registrar
from Usuarios import Usuarios
import time
from tkinter import ttk
from tkinter.ttk import Progressbar
import random


# ----------------------------
# definiciones


ColorFondo = "#818181"
Aleatorio = random.randrange(1, 20)

def Verificar():
    Username = NombreUsuario.get()
    Password = ContraseñaUsuario.get()

    if Username == "":
        messagebox.showerror("Alert", "Campo vacio")
        NombreUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            width= 20,
            highlightbackground = "red",
            highlightcolor= "red",
            highlightthickness=1
        )
        ContraseñaUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            width= 20,
            highlightbackground = "red",
            highlightcolor= "red",
            highlightthickness=1
        )

    elif Username not in Usuarios:
        messagebox.showwarning("Error", "Usuario invalido")
        NombreUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            width= 20,
            highlightbackground = "red",
            highlightcolor= "red",
            highlightthickness=1
        )
        ContraseñaUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            width= 20,
            highlightbackground = "red",
            highlightcolor= "red",
            highlightthickness=1
        )

    elif Username in Usuarios and Password == Usuarios[Username]["password"]:
        style = ttk.Style()

        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background= 'Orange')

        bar = Progressbar(ventana, length=220, style="black.Horizontal.TProgressbar", mode="indeterminate")
        bar['value'] = 0
        bar.place(x= 410, y=370)

        for x in range(20):
            if x >= 300:
                break
            bar['value'] += Aleatorio
            ventana.update_idletasks()
            time.sleep(0.2)
            
        time.sleep(0.5)
        messagebox.showinfo("Login", "Inicio de secion exitoso")
    
        NombreUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            cursor= 'arrow',
            width= 20,
        )
        ContraseñaUsuario.config(
            bg="white",
            fg="black",
            font= ('Times', 11),
            cursor= 'arrow',
            width= 20,
        )
        ventana.destroy()
        AbrirVentana2()


    elif Username in Usuarios:
        if Password != Usuarios[Username]["password"]:
            messagebox.showerror("Error", "Contraseña invalida")

            NombreUsuario.config(
                bg="white",
                fg="black",
                font= ('Times', 11),
                width= 20,
                highlightthickness=0
            )

            ContraseñaUsuario.config(
                bg="white",
                fg="black",
                font= ('Times', 11),
                width= 20,
                highlightbackground = "red",
                highlightcolor= "red",
                highlightthickness=1
            )



# -------------------------------------------------------


#-------------------------------------
# diseño

ventana = Tk()


ventana.title('VatGram')
ventana.iconbitmap("ProyectoFinal\imagenes\icon.ico")
ventana.geometry('700x420')
ventana.resizable(0, 0) 

back = Frame(master=ventana,bg='black')
back.pack_propagate(0)
back.pack(fill=BOTH, expand=1)

img = PhotoImage(file="ProyectoFinal\imagenes\Imagen.png")

lbl_image = Label(ventana, image=img).pack()
# ------------------------------------------------

Login =  Label(ventana, text="Usuario")
Login.config(
    background=ColorFondo,
    font= ('Times', 11)
)
Pass = Label(ventana, text="Contraseña")
Pass.config(
    background=ColorFondo,
    font= ('Times', 11)
)

Login.place(x= 405, y=129)
Pass.place(x= 405, y=169)

# ---------------------------------------------------------------------
# Caja de texto 

Usu = StringVar()
Contra = StringVar()

NombreUsuario = Entry(ventana, justify='center', textvariable=Usu)
NombreUsuario.pack()
NombreUsuario.config(
    bg="white",
    fg="black",
    font= ('Times', 11),
    width= 20
)
NombreUsuario.place(x= 485, y=130)

ContraseñaUsuario = Entry(ventana, justify='center', textvariable=Contra)
ContraseñaUsuario.pack()
ContraseñaUsuario.config(
    show="*",
    bg="white",
    fg="black",
    font= ('Times', 11),
    width= 20
)
ContraseñaUsuario.place(x= 485, y=170)

# -------------------------------------------------------------


IniciarSecion = Button(ventana, text='iniciar sesión', command=Verificar)
IniciarSecion.pack()
IniciarSecion.config(
    bg=ColorFondo,
    fg="black",
    font= ('Times', 10),
    cursor= 'arrow',
    height= 1,
    width= 30
)

Registrar = Button(ventana, text='Registrar', command=Registrar)
Registrar.pack()
Registrar.config(
    bg=ColorFondo,
    fg="black",
    font= ('Times', 10),
    cursor= 'arrow',
    height= 1,
    width= 30
)

Registrar.place(x= 410.5, y=310)
IniciarSecion.place(x= 410.5, y=240)


# -------------------------------------------------------------
ventana.mainloop()