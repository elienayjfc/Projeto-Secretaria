from tkinter import *
from tkinter import ttk

def telaLogin(callback_login): 
    root = Tk()
    tela = ttk.Frame(root, padding= 50)
    root.title("Login")
    tela.grid()

    ttk.Label(tela, text= "Usuario:").grid(column=0,row=0)
    login_view = ttk.Entry(tela, text= "usuario: ")
    login_view.grid(column=1, row=0)
    ttk.Label(tela, text= "Senha").grid(column=0, row = 1)
    senha_view = ttk.Entry(tela, show="*")
    senha_view.grid(column=1, row=1)
    entrar = ttk.Button(tela, text="Entrar", command=lambda: callback_login(login_view.get(), senha_view.get()))
    entrar.grid(column=1, row=2)
    
    return tela