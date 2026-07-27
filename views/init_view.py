import flet as ft

def init_page (page = ft.Page):

    async def relatorio_gerencial(e):
            #page.session.clear()
            await page.push_route('/relatorio_gerencial')

    async def cadastro_membros(e):
         await page.push_route('/cadastro_membros')
            
    menuGeral = ft.MenuBar(controls= [
        ft.SubmenuButton(content= ft.Text('Congregações', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Relatorio gerencial'),on_click = relatorio_gerencial),
            ft.MenuItemButton(content= ft.Text('Relatorios de culto'))]),
        ft.SubmenuButton(width= 100, content= ft.Text('Membros', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Cadastrar Membros'), on_click = cadastro_membros),
            ft.MenuItemButton(content= ft.Text('situação cadastral')),
            ft.MenuItemButton(content= ft.Text('Remover Membros'))]),
          ft.SubmenuButton( width= 100,content= ft.Text('Ministerios',text_align = ft.TextAlign.CENTER ),controls= [
            ft.MenuItemButton(content= ft.Text('Nova consagração')),
            ft.MenuItemButton(content= ft.Text('Alterar Ministerios')),
            ft.MenuItemButton(content= ft.Text('Departamentos'))])
        
    ])

    menu = ft.Column(
        
        controls= [
            ft.Row( controls= [menuGeral],
            alignment= ft.MainAxisAlignment.CENTER,
            )  
        ]
    )
    #usuario = page.session.get('Usuario logado')

    

    async def fazer_logout(e):
        #page.session.clear()
        await page.push_route('/')

    return ft.View(
        route= '/init',
        controls= [ft.Row(controls= [menu, ft.IconButton(icon= ft.Icons.EXIT_TO_APP, on_click=fazer_logout)],
                           alignment= ft.MainAxisAlignment.CENTER)]
    )




   

