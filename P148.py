# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:16:20 2023

@author: Aidan
"""

from tkinter import*

import random

root = Tk()

root.title("P148")

root.geometry("1600x600")

etiqueta1 = Label(root)

etiqueta2 = Label(root)

Lista_de_picnic = ["Toalla", "Jarra de agüita con u y dierecis al final de limon", "fruta", "comida", "Telefono y Bocina", "A tu amigo/pareja/familia", "Que no se te olvide un postre y toallitas humedas por si te bautizan las aves"]

etiqueta1["text"]= "Lista de picnic :D :" + " " + str(Lista_de_picnic)

def Objetos ():
    
    Lista_aleatoria = random.randint(0, 7)
    
    datos = Lista_de_picnic[Lista_aleatoria]
    
    print(Lista_aleatoria)
    
    etiqueta2["text"] = "Que no se me olvide llevarme:" + " " + str(datos)
    
etiqueta1.place(relx=0.5, rely=0.4, anchor=CENTER)

btn = Button(root, text="Que elemento llevarme", command=Objetos, bg="cyan", fg="black")

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

etiqueta2.place(relx=0.5, rely=0.6, anchor=CENTER)
    
root.mainloop()