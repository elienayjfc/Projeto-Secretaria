from views.login_view import telaLogin
from services.login.funcoes_login import login
from tkinter import messagebox
 

def autenticacao(u,s): #resolver tamanho da mesage box
    if login(u,s):
        messagebox.showinfo('Sucesso', "Login Realizado")
    else: messagebox.showinfo( 'Erro',"Usuario ou senha incorretos")





if __name__ == "__main__":
    app =  telaLogin(autenticacao)
    app.mainloop()
    