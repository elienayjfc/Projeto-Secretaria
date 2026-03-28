from views.login_view import telaLogin
from services.login.funcoes_login import login
from tkinter import messagebox
 

def autenticacao(u,s):
    if login(u,s):
        messagebox.showinfo("Login Realizado")
    else: messagebox.showinfo("Usuario ou senha incorretos")





if __name__ == "__init__":
    app =  telaLogin(autenticacao)
    app.mainloop()
    
