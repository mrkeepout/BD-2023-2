import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor
import tela_livro
import tela_material
import tela_cadastro

#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#janela------------------------------------------------------------------------------------------
def show(data):
    print(data)
    janela_menu = tk.Toplevel()
    janela_menu.title("Menu")
    janela_menu.geometry("800x600")
    janela_menu.configure(background=cor1)
    janela_menu.resizable(width=False, height=False)

#Dividindo a janela------------------------------------------------------------------------------------------
    barra_titulo = Frame(janela_menu, width=800, height=200, relief="flat")
    barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    barra_dados = Frame(janela_menu, width=800, height=400, relief="flat")
    barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    tk.Label(barra_titulo, text="Menu", font=("Verdana", 30, "bold")).grid(padx=250)

    botao_login = tk.Button(barra_dados, text="Realizar Emprestimo",font=("Verdana", 12, "bold"))
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Consultar Acervo",font=("Verdana", 12, "bold"))
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Cadastrar livro",font=("Verdana", 12, "bold"),  command = tela_livro.show_cadastro)
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Cadastrar material didático",font=("Verdana", 12, "bold"),  command = tela_material.show_cadastro)
    botao_login.grid()

    botao_cadastro = tk.Button(barra_dados, text="Cadastrar usuário", font=("Verdana", 12, "bold"), command=tela_cadastro.show_cadastro)
    botao_cadastro.grid()
    

    # janela_menu.mainloop()
