import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor
import tela_menu



#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca


#-----------------------------------------------------------------------
def show_cadastro():
    janela_livro = tk.Tk()
    janela_livro.title("Cadastro de livros")
    janela_livro.geometry("800x600")
    janela_livro.configure(background=cor1)
    janela_livro.resizable(width=False, height=False)
#-----------------------------------------------------------------------
    barra_titulo = Frame(janela_livro, width=800, height=200, relief="flat")
    barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    barra_dados = Frame(janela_livro, width=800, height=400, relief="flat")
    barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    barra_interacoes = Frame(janela_livro, width=800, height=200, relief="flat")
    barra_interacoes.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)
    #Remover Widgets Login

    tk.Label(barra_titulo, text="Cadastro de livros", font=("Verdana", 30, "bold")).grid(padx=250)

    label_titulo = tk.Label(barra_dados, text="Título:", font=("Verdana", 12, "bold"))
    label_titulo.grid(row=1)
    entrada_titulo = tk.Entry(barra_dados)
    entrada_titulo.grid(row=1, column=1)

    label_autor = tk.Label(barra_dados, text="Autor:", font=("Verdana", 12, "bold"))
    label_autor.grid(row=2)
    entrada_autor = tk.Entry(barra_dados) 
    entrada_autor.grid(row=2, column=1)

    label_isbn = tk.Label(barra_dados, text="ISBN:", font=("Verdana", 12, "bold"))
    label_isbn.grid(row=3)
    entrada_isbn = tk.Entry(barra_dados, width= 50)
    entrada_isbn.grid(row=3, column=1)
    
    label_descricao = tk.Label(barra_dados, text="Descrição:",font=("Verdana", 12, "bold"))
    label_descricao.grid(row=4)
    entrada_descricao = tk.Entry(barra_dados, width= 50)
    entrada_descricao.grid(row=4, column=1)
    
    label_categoria = tk.Label(barra_dados, text="Categoria:",font=("Verdana", 12, "bold"))
    label_categoria.grid(row=5)
    entrada_categoria = tk.Entry(barra_dados, width= 50)
    entrada_categoria.grid(row=5, column=1)

    label_data_aquisicao = tk.Label(barra_dados, text="Data de aquisição:",font=("Verdana", 12, "bold"))
    label_data_aquisicao.grid(row=6)
    entrada_data_aquisicao = tk.Entry(barra_dados, width= 50)
    entrada_data_aquisicao.grid(row=6, column=1)

    label_localizacao = tk.Label(barra_dados, text="Localização física:",font=("Verdana", 12, "bold"))
    label_localizacao.grid(row=7)
    entrada_localizacao = tk.Entry(barra_dados, width= 50)
    entrada_localizacao.grid(row=7, column=1)

    label_conservacao = tk.Label(barra_interacoes, text="Estado de conservação:", font=("Verdana", 12, "bold")).grid(row=5, column=0)
    n = tk.StringVar()
    tipo_combo_box = ttk.Combobox(barra_interacoes, width= 15, textvariable=n, font=("Verdana", 12, "bold"))
    tipo_combo_box["values"] = ("Excelente", "Muito bom", "Bom", "Regular", "Ruim")
    tipo_combo_box.grid(row= 8, column=1)
        
    label_capa = tk.Label(barra_dados, text="URI da capa do livro:",font=("Verdana", 12, "bold"))
    label_capa.grid(row=9)
    entrada_capa = tk.Entry(barra_dados, width= 50)
    entrada_capa.grid(row=9, column=1)

    def cadastrar_banco():
        titulo_Banco = entrada_titulo.get()
        autor_Banco = entrada_autor.get()
        isbn_Banco = entrada_isbn.get()
        descricao_Banco = entrada_descricao.get()
        categoria_Banco = entrada_categoria.get()
        data_aquisicao_Banco = entrada_data_aquisicao.get()
        localizacao_Banco = entrada_localizacao.get()
        conservacao_Banco = tipo_combo_box.get()
        material_Banco = ""
        capa_Banco = 'https://www.google.com.br' #entrada_capa.get()
        
        cadastro_cursor.cursor.execute("""
        INSERT INTO LIVRO(Titulo, Autor, ISBN, URI_capa_livro) VALUES(?, ?, ?, ?)
        """, (titulo_Banco, autor_Banco, isbn_Banco, capa_Banco))
        cadastro_cursor.comn.commit()

        cadastro_cursor.cursor.execute("""
        INSERT INTO RECURSO(Data_aquisicao, Localizacao_fisica, Estado_conservacao, Descricao, Categoria, fk_LIVRO_ISBN, fk_MAT_DIDAT_ID) VALUES(?, ?, ?, ?, ?, ?, ?)
        """, (data_aquisicao_Banco, localizacao_Banco, conservacao_Banco, descricao_Banco, categoria_Banco, isbn_Banco, material_Banco))
        cadastro_cursor.comn.commit()
        messagebox.showinfo(title="Cadastro Status", message="Cadastramento feito com Sucesso!")
        voltar()

    def voltar():
        janela_livro.withdraw()
        tela_menu.show()

    botao_cadastro_tela = tk.Button(barra_interacoes, text="Cadastrar", font=("Verdana", 12, "bold"), command = cadastrar_banco)
    botao_cadastro_tela.grid()
    botao_voltar = tk.Button(barra_interacoes, text="Voltar", font=("Verdana", 12, "bold"), command=voltar)
    botao_voltar.grid()