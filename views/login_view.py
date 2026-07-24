import flet as ft 
from services.login.funcoes_login import login
from views.init_view import main

def tela_login(page: ft.Page):
    page.window.width = 400
    page.window.height = 250
    page.title = 'Login'
    page.padding = 30
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

    


    def fazer_login():
        if login(usuario.value, senha.value) == True:
            alerta = ft.Text('Logado com sucesso')
            page.add(alerta)
            page.go(main)

            
            
            
    usuario = ft.TextField(hint_text='Usuario', label='Usuário')
    senha = ft.TextField(hint_text='Senha', label = 'senha', password=True)
    new_button = ft.Button('Entrar', bgcolor= ft.Colors.GREEN_100, color=ft.Colors.GREEN,on_click = fazer_login) #on_click adiciona uma função ao butão

    layout =  ft.Column (spacing= 5, 
                         alignment= ft.MainAxisAlignment.CENTER,
                         controls= [
                             ft.Row(ft.Container(content= usuario), alignment= ft.CrossAxisAlignment.CENTER),
                             ft.Row(ft.Container(content=senha),alignment= ft.CrossAxisAlignment.CENTER),
                             ft.Row(ft.Container(content=new_button),alignment= ft.CrossAxisAlignment.CENTER)
                         ])
    page.add(layout)
    



ft.app(target = tela_login)

