import flet as ft 
from services.login.funcoes_login import login


def tela_login(page: ft.Page):
    
    usuario = ft.TextField(hint_text='Usuario', label='Usuário')
    senha = ft.TextField(hint_text='Senha', label = 'senha', password=True)
    #new_button = ft.Button('Entrar', bgcolor= ft.Colors.GREEN_100, color=ft.Colors.GREEN) #on_click adiciona uma função ao butão
    
    layout =  ft.Column (spacing= 5, 
                             alignment= ft.MainAxisAlignment.CENTER,
                             controls= [
                                 ft.Row(ft.Container(content= usuario), alignment= ft.CrossAxisAlignment.CENTER),
                                 ft.Row(ft.Container(content=senha),alignment= ft.CrossAxisAlignment.CENTER),
                                 #ft.Row(ft.Container(content=new_button),alignment= ft.CrossAxisAlignment.CENTER)
                             ])


    async def fazer_login(e):
        if login(usuario.value, senha.value) == True:
            alerta = ft.Text('Logado com sucesso')
            page.add(alerta)
            #page.session.set('Usuario logado', usuario.value)
            await page.push_route('/init')
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Usuario ou senha incorretos'), bgcolor= ft.Colors.ERROR)
            page.snack_bar.open =True
            page.update()
            
    return ft.View(
        route= '/',
        padding= 30,
        controls= [layout, 
                   ft.Row(
                       alignment= ft.CrossAxisAlignment.CENTER,
                       controls=[ft.ElevatedButton('Entrar',on_click=fazer_login)])]
                       
        )

            
            
            
    
    
        
  

