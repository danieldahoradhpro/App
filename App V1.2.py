from tkinter import *
import tkinter.messagebox
def save_data():
    try:
        fileD = open("Pedidos.txt", "a")
        fileD.write("Local\n")
        fileD.write("%s\n" % local.get())
        fileD.write("Pedido\n")
        fileD.write("%s\n" % pedido.get())
        fileD.write("Endereço\n")
        fileD.write("%s\n" % endereço.get("1.0", END))
        local.delete(0, END)
        pedido.delete(0, END)
        endereço.delete("1.0", END)
    except Exception as ex:
tkinter.message.showerror("Erro!", "O servidor está cheio\n %s" % ex)
app = Tk()
app.title('Deliveries Premium')
Label(app, text = "Local").pack()
local = Entry(app)
local.pack()
Label(app, text = "Pedido").pack()
pedido = Entry(app)
pedido.pack()
Label(app, text = "Endereço").pack()
endereço = Text(app)
endereço.pack()
Button(app, text = "Enviar seu Pedido.", command = save_data).pack()
app.mainloop()
