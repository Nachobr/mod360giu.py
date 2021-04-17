from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import subprocess
import os
import sys

window = Tk()

window.title("Modelado en 360°")

window.geometry('900x700')

def submit():
    x1 = textNameBox.get()
    x2 = numXBox.get()
    x3 = numYBox.get()
    os.system("python3 parse.py " + " -n"+ textNameBox.get() + " -x" + numXBox.get() + " -y" + numYBox.get())

lbl = Label(window, text="Bienvenido a la aplicación de Modelado en 360° de Objetos" , font=("Arial Bold", 12))
lbl.grid(row = 0, column = 0)

lbl1 = Label(window, text="Escribe un nombre" , font=("Arial Bold", 12))
lbl1.grid(row = 1, column = 0)

textNameBox = Entry(window, width=10)
textNameBox.grid(row = 1, column = 1)

lbl2 = Label(window, text="Cantidad de fotos" , font=("Arial Bold", 12))
lbl2.grid(row = 2, column = 0)

numXBox = Entry(window, width=10)
numXBox.grid(row = 2, column = 1)

lbl3 = Label(window, text="Cantidad de vistas" , font=("Arial Bold", 12))
lbl3.grid(row = 3, column = 0)

numYBox = Entry(window, width=10)
numYBox.grid(row = 3, column = 1)

btn = Button(window, text="Crear Visualización en 360°" , command= submit) #, command= parse)
btn.grid(row = 4, column = 1)



#btn1 = Button(window, text="Importar desde Meli", command=clicked)

#btn1.grid(row = 2, column = 0)



window.mainloop()
