import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def verificar_cadastro():
    if entrada_nome.get() == "" or entrada_senha == "" or entrada_sobrenome == "" or entrada_usuario == "":
        messagebox.showerror("Erro", "Falha ao criar conta!")
    else:
        messagebox.showinfo("Sucesso!", "Cadastro Concluido!")

#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#janela------------------------------------------------------------------------------------------
janela_cadastro = tk.Tk()
janela_cadastro.title("Cadastro")
janela_cadastro.geometry("800x600")
janela_cadastro.configure(background=cor1)
janela_cadastro.resizable(width=False, height=False)

#Dividindo a janela------------------------------------------------------------------------------------------
barra_titulo = Frame(janela_cadastro, width=800, height=200, relief="flat")
barra_titulo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

barra_dados = Frame(janela_cadastro, width=800, height=200, relief="flat")
barra_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

barra_interacoes = Frame(janela_cadastro, width=800, height=200, relief="flat")
barra_interacoes.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)


tk.Label(barra_titulo, text="Cadastro", font=("Verdana", 30, "bold")).grid(padx=300)

label_usuario = tk.Label(barra_dados, text="Usuario:", font=("Verdana", 12, "bold"))
label_usuario.grid(row=2)
label_nome = tk.Label(barra_dados, text="Nome:", font=("Verdana", 12, "bold"))
label_nome.grid(row=3)
label_sobrenome = tk.Label(barra_dados, text="Sobrenome:",font=("Verdana", 12, "bold"))
label_sobrenome.grid(row=4)
label_senha = tk.Label(barra_dados, text="Senha:",font=("Verdana", 12, "bold"))
label_senha.grid(row=5)
label_funcao = tk.Label(barra_dados, text="Funcao:", font=("Verdana", 12, "bold"))


entrada_usuario = tk.Entry(barra_dados, width=50)
entrada_senha = tk.Entry(barra_dados, width= 50, show="*")
entrada_nome = tk.Entry(barra_dados, width= 50)
entrada_sobrenome = tk.Entry(barra_dados, width= 50)
entrada_usuario.grid(row=2, column=1)
entrada_nome.grid(row=3, column=1)
entrada_sobrenome.grid(row=4, column=1)
entrada_senha.grid(row=5, column=1)

tk.Label(barra_interacoes, text="Tipo de cadastro:", font=("Verdana", 12, "bold")).grid(row=6, column=0)
n = tk.StringVar()
tipo_combo_box = ttk.Combobox(barra_interacoes, width= 15, textvariable=n, font=("Verdana", 12, "bold"))
tipo_combo_box["values"] = ("Cliente", "Administrador")
tipo_combo_box.grid(row= 6, column=1)

botao_concluir = tk.Button(barra_interacoes, text="Cadastrar",font=("Verdana", 12, "bold"), command=verificar_cadastro)
botao_concluir.grid()
botao_voltar = tk.Button(barra_interacoes, text="Voltar",font=("Verdana", 12, "bold"), command=janela_cadastro.destroy)
botao_voltar.grid()

janela_cadastro.mainloop()