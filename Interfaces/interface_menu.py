#import requests
from tkinter import *


#cores--------------------------------------------------------------------------------------------
cor0 = "#f0f3f5"  # Preta
cor1 = "#ffffff"  # branca
cor2 = "#0000FF"  # azul
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = "#DCDCDC"  # cinza claro
cor6 = "#A9A9A9"  # cinza escuro

#janela------------------------------------------------------------------------------------------
janela = Tk()
janela.title("Sistema de Gerenciamento de Materiais para um Laboratório Didático (SGMLD)")
janela.geometry("800x600")
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

#Dividindo a janela------------------------------------------------------------------------------------------

Meio = Frame(janela, width=800, height=275, bg=cor5, relief="flat")
Meio.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

base = Frame(janela, width=800, height=275, bg=cor6, relief="flat")
base.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

#Menu--------------------------------------------------------------------------------------------
barraMenu= Menu(janela)
menuFile= Menu(barraMenu,tearoff=0,font=("Verdana", 8, "bold"))
menuFile.add_command(label="Início")
menuFile.add_command(label="Sobre")
menuFile.add_separator()
menuFile.add_command(label="Sair",command=janela.quit)

barraMenu.add_cascade(label="File", menu=menuFile)

janela.config(menu=barraMenu)

#Janela Meio--------------------------------------------------------------------------------------------
j_meio = Label(Meio, text="Cadastros", bg=cor5, fg=cor4,anchor=NW, justify="left", font=("Verdana", 12, "bold"))
j_meio.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

botaoLivro = Button(Meio, text="Livros", width=15, bg=cor1, font=("Verdana", 12, "bold"))
botaoLivro.grid(column=0, row=1, pady=30, padx=15, sticky=NSEW)

botaoMatDid = Button(Meio, text="Materiais Didáticos",width=25, bg=cor1, font=("Verdana", 12, "bold"))
botaoMatDid.grid(column=1, row=1, pady=30, padx=15, sticky=NSEW)

botaoUsuario = Button(Meio, text="Usuários",width=15, bg=cor1, font=("Verdana", 12, "bold"))
botaoUsuario.grid(column=2, row=1, pady=30, padx=25, sticky=NSEW)

#Janela Base--------------------------------------------------------------------------------------------
j_base = Label(base, text="Demais Opções", bg=cor6, fg=cor1,anchor=NW, justify="left", font=("Verdana", 12, "bold"))
j_base.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

botaoPesquisa = Button(base, text="Pesquisa", width=25, bg=cor1, font=("Verdana", 12, "bold"))
botaoPesquisa.grid(column=0, row=2, pady=30, padx=15, sticky=NSEW)

botaoEmprestimo = Button(base, text="Empréstimo",width=25, bg=cor1, font=("Verdana", 12, "bold"))
botaoEmprestimo.grid(column=1, row=2, pady=30, padx=25, sticky=NSEW)



janela.mainloop()