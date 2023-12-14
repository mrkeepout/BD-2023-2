import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor
import tela_menu
import tela_adm
import tela_cadastro



#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

def show_autenticacao():
    def login():
        login_usuario = entrada_usuario.get()
        login_senha = entrada_senha.get()
        
        salt = '5gz'
        hash_senha = tela_cadastro.servico_salgar_senha(salt, login_senha)

        cadastro_cursor.cursor.execute("""
        SELECT * FROM USUARIO
        WHERE (Login = ? and Senha = ?)                               
        """, (login_usuario, hash_senha))
        print("Selecionou")
        verificar_login = cadastro_cursor.cursor.fetchone()

        try:
            if (login_usuario in verificar_login and hash_senha in verificar_login):
                messagebox.showinfo(title="Login Status", message="Sucesso!")
                janela_autenticacao.withdraw()
                if ('Administrador' in verificar_login):
                    tela_adm.show(verificar_login)
                else :
                    tela_menu.show(verificar_login)
        except:
            messagebox.showerror(title="Login Status", message="Usuario nao castrado!")

    def mudarPagina():
        janela_autenticacao.withdraw()
        tela_cadastro.show_cadastro()
        
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

    barra_interacoes = Frame(janela_autenticacao, width=800, height=200, relief="flat")
    barra_interacoes.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)

    tk.Label(barra_titulo, text="Autenticação", font=("Verdana", 30, "bold")).grid(padx=250)

    label_usuario = tk.Label(barra_dados, text="Usuario", font=("Verdana", 12, "bold"))
    label_usuario.grid(row=1)
    label_senha = tk.Label(barra_dados, text="Senha", font=("Verdana", 12, "bold"))
    label_senha.grid(row=2)

    entrada_usuario = tk.Entry(barra_dados)
    entrada_senha = tk.Entry(barra_dados, show="*")
    entrada_usuario.grid(row=1, column=1)
    entrada_senha.grid(row=2, column=1)

    botao_login = tk.Button(barra_dados, text="Entrar",font=("Verdana", 12, "bold"), command=login)
    botao_login.grid()

    botao_cadastro = tk.Button(barra_dados, text="Cadastrar", font=("Verdana", 12, "bold"), command=mudarPagina)
    botao_cadastro.grid()





    janela_autenticacao.mainloop()