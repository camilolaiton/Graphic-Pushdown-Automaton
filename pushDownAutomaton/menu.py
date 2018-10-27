from tkinter import *

raiz = Tk()

def hola():
    print("hola")

# Crear el menu principal
menubarra = Menu(raiz)

# Crea un menu desplegable y lo agrega al menu barra
menuarchivo = Menu(menubarra, tearoff=0)
menuarchivo.add_command(label="Abrir", command=hola)
menuarchivo.add_command(label="Guardar", command=hola)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=raiz.quit)
menubarra.add_cascade(label="Archivo", menu=menuarchivo)

# Crea dos menus desplegables mas
menueditar = Menu(menubarra, tearoff=0)
menueditar.add_command(label="Cortar", command=hola)
menueditar.add_command(label="Copiar", command=hola)
menueditar.add_command(label="Pegar", command=hola)
menubarra.add_cascade(label="Editar", menu=menueditar)
menuayuda = Menu(menubarra, tearoff=0)
menuayuda.add_command(label="Acerca de...", command=hola)
menubarra.add_cascade(label="Ayuda", menu=menuayuda)

# Mostrar el menu
raiz.config(menu=menubarra)

# Mostrar la ventana
raiz.mainloop()