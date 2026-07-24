import flet as ft

def init_page (page = ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    menuCongregações = ft.MenuBar(controls= [
        ft.SubmenuButton(expand = True,content= ft.Text('Congregações', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Relatorio gerencial')),
            ft.MenuItemButton(content= ft.Text('Relatorios de culto'))]),
    ])
    menuMembros = ft.MenuBar(controls= [
        ft.SubmenuButton(width= 150,expand = True, content= ft.Text('Membros', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Cadastrar Membros')),
            ft.MenuItemButton(content= ft.Text('situação cadastral')),
            ft.MenuItemButton(content= ft.Text('Remover Membros'))]) 

    ])
    menuMinisterio = ft.MenuBar(controls= [
        ft.SubmenuButton( width= 100, expand= True ,content= ft.Text('Ministerios',text_align = ft.TextAlign.CENTER ),controls= [
            ft.MenuItemButton(content= ft.Text('Nova consagração')),
            ft.MenuItemButton(content= ft.Text('Alterar Ministerios')),
            ft.MenuItemButton(content= ft.Text('Departamentos'))
        ])
    ])
    menuGeral = ft.MenuBar(controls= [
        ft.SubmenuButton(content= ft.Text('Congregações', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Relatorio gerencial')),
            ft.MenuItemButton(content= ft.Text('Relatorios de culto'))]),
        ft.SubmenuButton(width= 100, content= ft.Text('Membros', text_align= ft.TextAlign.CENTER), controls= [
            ft.MenuItemButton(content= ft.Text('Cadastrar Membros')),
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



    page.add(menu)

ft.app(target = init_page)