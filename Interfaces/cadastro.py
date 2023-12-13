import tkinter as tk
from tkinter import messagebox


def verificar_cadastro():
    if entrada_nome.get() is "" or entrada_senha is "" or entrada_sobrenome is "" or entrada_usuario is "":
        messagebox.showerror("Erro", "Falha ao criar conta!")
    else:
        messagebox.showinfo("Sucesso!", "Cadastro Concluido!")

janela_cadastro = tk.Tk()
janela_cadastro.title("Cadastro")
janela_cadastro.geometry("800x600")

tk.Label(janela_cadastro, text="Cadastro", font=("Arial", 20)).grid()
label_usuario = tk.Label(janela_cadastro, text="Usuario")
label_usuario.grid(row=1)
label_nome = tk.Label(janela_cadastro, text="Nome")
label_nome.grid(row=2)
label_sobrenome = tk.Label(janela_cadastro, text="Sobrenome")
label_sobrenome.grid(row=3)
label_senha = tk.Label(janela_cadastro, text="Senha")
label_senha.grid(row=4)
label_funcao = tk.Label(janela_cadastro, text="Funcao")


entrada_usuario = tk.Entry(janela_cadastro)
entrada_senha = tk.Entry(janela_cadastro)
entrada_nome = tk.Entry(janela_cadastro)
entrada_sobrenome = tk.Entry(janela_cadastro)
entrada_usuario.grid(row=1, column=1)
entrada_nome.grid(row=2, column=1)
entrada_sobrenome.grid(row=3, column=1)
entrada_senha.grid(row=4, column=1)

botao_concluir = tk.Button(janela_cadastro, text="Cadastrar", command=verificar_cadastro)
botao_concluir.grid()
botao_voltar = tk.Button(janela_cadastro, text="Voltar", command=janela_cadastro.destroy)
botao_voltar.grid()

janela_cadastro.mainloop()