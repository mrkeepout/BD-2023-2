import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor

#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#janela------------------------------------------------------------------------------------------
def show():
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

    botao_login = tk.Button(barra_dados, text="Cadastrar Livros",font=("Verdana", 12, "bold"))
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Emprestimo",font=("Verdana", 12, "bold"))
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Acervo",font=("Verdana", 12, "bold"))
    botao_login.grid()

    # janela_menu.mainloop()
