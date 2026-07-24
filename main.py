import flet as ft
from views.login_view import tela_login
from views.init_view import init_page


async def main(page: ft.Page):
    def route_change(e):
        #page.views.clear()

        
        if page.route == '/':
            page.window.width = 400
            page.window.height = 250
            page.title = 'Login'
            page.padding = 30
            page.theme_mode = ft.ThemeMode.DARK
            page.window.resizable = False
            
            page.views.append(tela_login(page))

        elif page.route == '/init':

            page.window.maximized= True
            page.title = 'Gerenciador'
            page.padding = 30
            page.theme_mode = ft.ThemeMode.LIGHT
            page.window.resizable = True
            
            page.views.append(init_page())

        else:
            page.views.append(tela_login(page))
        page.update()
        
            

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None)

ft.app(target = main)
'''if __name__ == '__init__':
    ft.run(main)'''

    