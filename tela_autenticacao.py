import tkinter as tk
from tkinter import messagebox
from tkinter import *

#variaveis globais
callback_autenticar = None


def on_entrar_click():
    global entrada_usuario
    global entrada_senha
    global callback_autenticar
    login = entrada_usuario.get()
    senha = entrada_senha.get()
    if callback_autenticar is not None:
        callback_autenticar(login, senha)


#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#janela------------------------------------------------------------------------------------------
janela_autenticacao = tk.Tk()
janela_autenticacao.title("Autenticação")
janela_autenticacao.geometry("800x600")
janela_autenticacao.configure(background=cor1)
janela_autenticacao.resizable(width=False, height=False)

#Dividindo a janela------------------------------------------------------------------------------------------
barra_titulo = Frame(janela_autenticacao, width=800, height=200, relief="flat")
barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

barra_dados = Frame(janela_autenticacao, width=800, height=400, relief="flat")
barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)


tk.Label(barra_titulo, text="Autenticação", font=("Verdana", 30, "bold")).grid(padx=250)

label_usuario = tk.Label(barra_dados, text="Login", font=("Verdana", 12, "bold"))
label_usuario.grid(row=1)
label_senha = tk.Label(barra_dados, text="Senha", font=("Verdana", 12, "bold"))
label_senha.grid(row=2)

entrada_usuario = tk.Entry(barra_dados)
entrada_senha = tk.Entry(barra_dados, show="*")
entrada_usuario.grid(row=1, column=1)
entrada_senha.grid(row=2, column=1)

botao_login = tk.Button(barra_dados, text="Entrar",font=("Verdana", 12, "bold"), command=on_entrar_click)
botao_login.grid()
#botao_cadastro = tk.Button(barra_dados, text="Cadastrar", font=("Verdana", 12, "bold"))
#adicionar a funcao cadastro apos text
#botao_cadastro.grid()


def show(on_autenticar=None):
    if on_autenticar is not None:
        global callback_autenticar
        callback_autenticar = on_autenticar
           
    janela_autenticacao.mainloop()

