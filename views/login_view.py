from tkinter import *
from tkinter import ttk

def telaLogin(callback_login): 
    root = Tk()
    tela = ttk.Frame(root, padding= 50)
    tela.grid()

    ttk.Label(tela, text= "Usuario:").grid(column=0,row=0)
    login_view = ttk.Entry(tela, text= "usuario: ").grid(column=1, row=0)
    ttk.Label(tela, text= "Senha").grid(column=0, row = 1)
    senha_view = ttk.Entry(tela, show="*").grid(column=1, row=1)
    ttk.Button(tela, text="Entrar", command=lambda: callback_login(login_view.get(), senha_view.get())).grid(column=1, row=2)
    
    return tela