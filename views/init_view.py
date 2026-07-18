import tkinter as tk
from tkinter import messagebox



#Janela inicial Progama
def tela_init():
    root = tk.Tk()
    root.title("ADJG")
    frm = tk.Frame(root)
    root.geometry('800x500')
    frm.pack(side='left', anchor='n')

    #Menu Congregações

    congregacao = tk.Menubutton(frm, text = 'Congregações', relief = 'raised', padx= 40, pady=20)
    congregacao.pack(side=tk.LEFT)
    menu_congregacao= tk.Menu(congregacao, tearoff=0)
    menu_congregacao.add_command(label='Relatorios gerencial', command=lambda: messagebox.showinfo('Aviso', 'Novo criado'))
    menu_congregacao.add_command(label='Relatorio de cultos ', command=lambda: messagebox.showinfo('Aviso', 'Novo criado'))
    menu_congregacao.add_command(label='futuro ...          ', command=lambda: messagebox.showinfo('Aviso', 'Novo criado'))
    congregacao.config(menu = menu_congregacao)

    #Menu Membros

    membros = tk.Menubutton(frm, text='Membros', relief = 'raised', padx= 40, pady=20)
    membros.pack(side=tk.LEFT)
    menu_membros = tk.Menu(membros, tearoff=0)
    menu_membros.add_command(label='Adicionar membros ')
    menu_membros.add_command(label='Situação cadastral')
    menu_membros.add_command(label='Remover membros   ')
    membros.config(menu = menu_membros)


    root.mainloop() 

#tela_init()