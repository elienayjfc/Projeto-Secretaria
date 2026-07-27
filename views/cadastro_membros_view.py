import flet as ft
import datetime

def cadastro_membros(page: ft.Page):
    async def back_init(e):
            await page.push_route('/init')
    def data(e):
        if date.value:
             campo_data.value = date.value.strftime("%d/%m/%Y")
             page.update()

    nome = ft.TextField(label = 'Nome completo', icon= ft.Icons.ASSIGNMENT)
    campo_data = ft.TextField(label= 'Data de nascimento', on_click= lambda _: page.show_dialog(date), read_only= True, icon= ft.Icons.CALENDAR_MONTH)
    date = ft.DatePicker(entry_mode= ft.DatePickerEntryMode.INPUT, on_change= data)
    botao = ft.IconButton(icon= ft.Icons.CALENDAR_MONTH, on_click= lambda _: page.show_dialog(date))
    numero = ft.TextField(label= 'Numero de contato', keyboard_type= ft.KeyboardType.NUMBER,
                          input_filter= ft.NumbersOnlyInputFilter() ,max_length= 11,counter= '', icon= ft.Icons.PHONE)
    endereco = ft.TextField(label='Endereço')
    numeroC = ft.TextField(label='Número', width=75, label_style= ft.TextStyle(size= 10))
    bairro = ft.Dropdown(
         value='Bairro',
         label= 'Bairro',
         options= [
              ft.DropdownOption(key='Jardim da glória', text= 'Jardim da Glória'),
              ft.DropdownOption(key='Cascalheiras', text= 'Cascalheiras'),
              ft.DropdownOption(key='Santa Clara B', text= 'Santa Clara B'),
              ft.DropdownOption(key='Santa Clara', text= 'Santa Clara'),
              ft.DropdownOption(key='Gavea 1', text= 'Gavea 1'),
              ft.DropdownOption(key='Gavea 2', text= 'Gavea 2'),
              ft.DropdownOption(key='Jardim daliana', text= 'Jardim daliana'),
              ft.DropdownOption(key='Serra Dourada', text= 'Serra Dourada'),
              ft.DropdownOption(key='São Cosme', text= 'São Cosme'),
              ft.DropdownOption(key='São Damião', text= 'São Damião'),

         ]
    )



    return ft.View(
        route= '/cadastro_membros',
        
        controls= [
             
            ft.Row(
                  controls= [
                  ft.IconButton(icon= ft.Icons.ARROW_BACK, on_click= back_init),
                  nome, campo_data,numero 
            ],alignment=  ft.MainAxisAlignment.CENTER),
            ft.Row(
                 controls= [
                      endereco, numeroC, bairro
                 ], alignment= ft.MainAxisAlignment.CENTER
            ),

            
        ]
)