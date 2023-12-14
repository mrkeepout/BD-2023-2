import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor
import tela_autenticacao



#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#-----------------------------------------------------------------------
def servico_salgar_senha(salt, senha):
    import hashlib
    senha = senha + salt
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def show_cadastro():
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("800x600")
    janela_cadastro.configure(background=cor1)
    janela_cadastro.resizable(width=False, height=False)
#-----------------------------------------------------------------------
    barra_titulo = Frame(janela_cadastro, width=800, height=200, relief="flat")
    barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    barra_dados = Frame(janela_cadastro, width=800, height=400, relief="flat")
    barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    barra_interacoes = Frame(janela_cadastro, width=800, height=200, relief="flat")
    barra_interacoes.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)
    #Remover Widgets Login

    tk.Label(barra_titulo, text="Cadastro", font=("Verdana", 30, "bold")).grid(padx=250)

    label_usuario = tk.Label(barra_dados, text="Usuario", font=("Verdana", 12, "bold"))
    label_usuario.grid(row=1)
    label_senha = tk.Label(barra_dados, text="Senha", font=("Verdana", 12, "bold"))
    label_senha.grid(row=2)

    entrada_usuario = tk.Entry(barra_dados)
    entrada_senha = tk.Entry(barra_dados, show="*")
    entrada_usuario.grid(row=1, column=1)
    entrada_senha.grid(row=2, column=1)
    label_nome = tk.Label(barra_dados, text="Nome:", font=("Verdana", 12, "bold"))
    label_nome.grid(row=3)
    label_sobrenome = tk.Label(barra_dados, text="Sobrenome:",font=("Verdana", 12, "bold"))
    label_sobrenome.grid(row=4)

    entrada_nome = tk.Entry(barra_dados, width= 50)
    entrada_sobrenome = tk.Entry(barra_dados, width= 50)

    entrada_nome.grid(row=3, column=1)
    entrada_sobrenome.grid(row=4, column=1)

    label_funcao = tk.Label(barra_interacoes, text="Tipo de cadastro:", font=("Verdana", 12, "bold")).grid(row=5, column=0)
    n = tk.StringVar()
    tipo_combo_box = ttk.Combobox(barra_interacoes, width= 15, textvariable=n, font=("Verdana", 12, "bold"))
    tipo_combo_box["values"] = ("Cliente", "Administrador")
    tipo_combo_box.grid(row= 5, column=1)

   
    def cadastrar_banco():
        usuario_Banco = entrada_usuario.get()
        senha_Banco = entrada_senha.get()
        nome_Banco = entrada_nome.get()
        sobrenome_Banco = entrada_sobrenome.get()
        funcao_Banco = tipo_combo_box.get()
        teste_imagem = 'https://www.google.com.br'
        
        salt = '5gz'
        hash_senha = servico_salgar_senha(salt, senha_Banco)
        
        cadastro_cursor.cursor.execute("""
        INSERT INTO USUARIO(Nome, Sobrenome, Login, Senha, URI_foto_user, Funcao) VALUES(?,?,?,?,?,?)
        """, (nome_Banco, sobrenome_Banco, usuario_Banco, hash_senha, teste_imagem, funcao_Banco))
        cadastro_cursor.comn.commit()
        messagebox.showinfo(title="Cadastro Status", message="Cadastramento feito com Sucesso!")

        voltar()

    def voltar():
        janela_cadastro.withdraw()
        tela_autenticacao.show_autenticacao()
    
    botao_cadastro_tela = tk.Button(barra_interacoes, text="Cadastrar", font=("Verdana", 12, "bold"), command = cadastrar_banco)
    botao_cadastro_tela.grid()
    botao_voltar = tk.Button(barra_interacoes, text="Voltar", font=("Verdana", 12, "bold"), command=voltar)
    botao_voltar.grid()