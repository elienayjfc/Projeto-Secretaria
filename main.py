from views.login_view import telaLogin
from views.login_view import fechar_tela
from services.login.funcoes_login import login
from tkinter import messagebox
from views.init_view import tela_init



def autenticacao(u,s): 
    if login(u,s):
        messagebox.showinfo('Sucesso', "Login Realizado")
        fechar_tela()
        tela_init()
     
    else: messagebox.showinfo( 'Erro',"Usuario ou senha incorretos")


if __name__ == "__main__":
    app =  telaLogin(autenticacao)
    app.mainloop()
  
    