import flet as ft 

def gerencial(page: ft.Page):

    async def back_init(e):
        #page.session.clear()
        await page.push_route('/init')

    congregacoes = ft.Dropdown(
        value ='Congregações',
        label= 'Congregações',
        options = [
            ft.DropdownOption(key='Sub sede', text= 'Sub sede'),
            ft.DropdownOption(key='Cascalheiras', text= 'Cascalheiras'),
            ft.DropdownOption(key='Jardim da Glória 3', text= 'Jardim da Glória 3'),
            ft.DropdownOption(key='Vila Esportiva', text= 'Vila Esportiva'),
            ft.DropdownOption(key='Santa Clara', text= 'Santa Clara'),
            ft.DropdownOption(key='Jardim Daliana', text= 'Jardim Daliana'),
            ft.DropdownOption(key='Gavea 1', text= 'Gavea 1'),
            ft.DropdownOption(key='Gavea 2', text= 'Gavea 2'),
            ft.DropdownOption(key='Serra Dourada', text= 'Serra Dourada'),
            ft.DropdownOption(key='São Damião', text= 'São Damião'),


        ],

    )
    filtroData = ft.DateRangePicker()

    return ft.View(
        controls= [ ft.Row(
            controls =[ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click=back_init),
                       congregacoes, ft.Button('Selecione o periodo', on_click= lambda _: page.show_dialog(filtroData))
                       

            ],
                    
        ),
            
            ft.Text('Cheguei na pagina de relatorios')]
    )

