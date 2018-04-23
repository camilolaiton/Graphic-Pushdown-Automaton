from grafos import automataGrafico
from tkinter import *
from PIL import Image, ImageTk

#Transiciones para grafo 1
label_PtoP = ["b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["b/b/λ", "a/a/λ"]
label_QtoR = ["λ/#/#"]

edges1 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

#Transiciones para grafo 2
label_PtoP = ["b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["b/b/λ", "a/a/λ"]
label_QtoQ = ["b/b/λ", "a/a/λ"]
label_QtoR = ["λ/#/#"]

edges2 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

root = Tk()

automata1 = automataGrafico("Palindromo Impar", edges1)
"""
def generar(a):
	automata1.generarAutomata(False, a)
	return automata1
"""

def Click(elegir):
	
    photo2 = PhotoImage(file="resources/Palindromo Impar"+elegir+".png")
    label.configure(image=photo2)
    label.image = photo2


image = Image.open("resources/Palindromo Impar.png")
photo = ImageTk.PhotoImage(image)
label = Label(root,image=photo)

label.pack()


labelframe = LabelFrame(root)
labelframe.pack(fill="both", expand="yes")


left = Label(labelframe)

button=Button(labelframe, padx = 5, pady = 5, text="Next",command = lambda: Click(""))
button.pack(side = RIGHT)


R1 = Radiobutton(labelframe, text="Choice 1", value=1)
R1.pack(side = LEFT)

R2 = Radiobutton(labelframe, text="Choice 2",  value=2)
R2.pack(side = LEFT)

left.pack()
root.mainloop()