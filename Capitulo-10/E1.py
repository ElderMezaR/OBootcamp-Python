from tkinter import ttk
import tkinter

window = tk.Tk()

def limpiar(event):
    seleccionado.set('')

window.rowconfigure(0, weight=3)
window.rowconfigure(1, weight=1)
boton = tkinter.Button(window, text='Haz click!')

seleccionado = tk.StringVar()
r1 = ttk.Radiobutton(window, text= 'Opcion 1', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='Opcion 2', value='2', variable= seleccionado)
r3 = ttk.Radiobutton(window, text='Opcion 3', value='3', variable= seleccionado)


r1.grid(column=0, row=0, padx=5)
r2.grid(column=1, row=0, padx=5 )
r3.grid(column=2, row=0, padx=0)

boton.grid(column=0, row=1, padx=5)
boton.bind('<Button-1>', limpiar)

#print(dir(r1))

window.mainloop()
