from tkinter import *
from tkinter import ttk

#def tela():
root = Tk()
root.title("Login")

frame = ttk.Frame(root, padding=50)
frame.grid()
#return root, frame


def telaLogin(callback_login):
    #root, frame = tela()
    ttk.Label(frame, text="Usuário:").grid(column=0, row=0)
    login_view = ttk.Entry(frame)
    login_view.grid(column=1, row=0)
    ttk.Label(frame, text="Senha").grid(column=0, row=1)
    senha_view = ttk.Entry(frame, show="*")
    senha_view.grid(column=1, row=1)

    entrar = ttk.Button(
        frame,text="Entrar",
        command=lambda: callback_login(login_view.get(), senha_view.get()))
    
    entrar.grid(column=1, row=2)
    return root

def fechar_tela():
    root.destroy()

