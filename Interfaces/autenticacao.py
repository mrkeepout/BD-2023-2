import tkinter as tk
from tkinter import messagebox

def verificar_autenticacao():
    if entrada_usuario.get() is "" or entrada_senha.get() is "":
        messagebox.showerror("Erro","Usuario ou senha invalidos!")
    else:
        messagebox.showinfo("Concluido", "Sucesso!")
    

janela_autenticacao = tk.Tk()
janela_autenticacao.title("Autenticação")
janela_autenticacao.geometry("800x600")

tk.Label(janela_autenticacao, text="Autenticação", font=("Arial", 30)).grid(column=400, pady=40)

label_usuario = tk.Label(janela_autenticacao, text="Usuario")
label_usuario.grid(row=1, padx=10)
label_senha = tk.Label(janela_autenticacao, text="Senha")
label_senha.grid(row=2, padx= 10)

entrada_usuario = tk.Entry(janela_autenticacao)
entrada_senha = tk.Entry(janela_autenticacao, show="*")
entrada_usuario.grid(row=1, column=1, padx=10)
entrada_senha.grid(row=2, column=1, padx=10)

botao_login = tk.Button(janela_autenticacao, text="Entrar", command=verificar_autenticacao)
botao_login.grid(padx= 10)
botao_cadastro = tk.Button(janela_autenticacao, text="Cadastrar")
#adicionar a funcao cadastro apos text
botao_cadastro.grid(padx= 10)





janela_autenticacao.mainloop()