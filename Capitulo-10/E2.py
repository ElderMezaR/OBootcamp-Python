import tkinter as tk


root = tk.Tk()
root.geometry('100x250')
root.title('Lista de invitados')

root.rowconfigure(0, weight=1)

invitados = ['Juan', 'Sebastian', 'Eduardo', 'José', 'María', 'Laura']
langs_var = tk.StringVar(value=invitados)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended'
)

listbox.grid(
    column=0,
    row=0,
    sticky='NS',
    padx=10
)
label = tk.Label(text="Invitados a la fiesta!")
label.grid(column=0, row=1, sticky='NS')


root.mainloop()
