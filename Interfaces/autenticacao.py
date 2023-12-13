import tkinter as tk
from tkinter import messagebox
from tkinter import *

def verificar_autenticacao():
    if entrada_usuario.get() == "" or entrada_senha.get() == "":
        messagebox.showerror("Erro","Usuario ou senha invalidos!")
    else:
        messagebox.showinfo("Concluido", "Sucesso!")
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

label_usuario = tk.Label(barra_dados, text="Usuario", font=("Verdana", 12, "bold"))
label_usuario.grid(row=1)
label_senha = tk.Label(barra_dados, text="Senha", font=("Verdana", 12, "bold"))
label_senha.grid(row=2)

entrada_usuario = tk.Entry(barra_dados)
entrada_senha = tk.Entry(barra_dados, show="*")
entrada_usuario.grid(row=1, column=1)
entrada_senha.grid(row=2, column=1)

botao_login = tk.Button(barra_dados, text="Entrar",font=("Verdana", 12, "bold"), command=verificar_autenticacao)
botao_login.grid()
botao_cadastro = tk.Button(barra_dados, text="Cadastrar", font=("Verdana", 12, "bold"))
#adicionar a funcao cadastro apos text
botao_cadastro.grid()





janela_autenticacao.mainloop()