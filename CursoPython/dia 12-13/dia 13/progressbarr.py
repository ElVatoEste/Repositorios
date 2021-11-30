from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


ventana = Tk()

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background= 'Red')

bar = Progressbar(ventana, length=200, style="black.Horizontal.TProgressbar")

bar['value'] = 20
bar.grid(column=0, row=0)

ventana.mainloop()
