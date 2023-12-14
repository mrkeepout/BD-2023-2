import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tela_menu
import sqlite3
from datetime import datetime, timedelta
import tela_menu

#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#CONECCAO-------------------------------------------------------------------------------------------------
conn = sqlite3.connect('sgmld_sem_heranca_alim.db')
cursor = conn.cursor()

#janela------------------------------------------------------------------------------------------
def show_acervo(data):
    janela_acervo = tk.Tk()
    janela_acervo.title("Acervo de Consulta")
    janela_acervo.geometry("1600x800")
    janela_acervo.configure(background=cor1)
    janela_acervo.resizable(width=False, height=False)

    def alugar(idRecurso):
        print(data[0])
        print(idRecurso)
        try:
            cursor.execute(f'''INSERT INTO Emprestimo (Data_emprestimo, Data_devolucao_prevista, Status, fk_Recursos_ID_item, fk_Usuarios_ID_user)
            VALUES ('14/12/2023', '19/12/2023', 'Emprestado', '{idRecurso}', '{data[0]}')''')
            conn.commit()
            print('Empréstimo realizado com sucesso!')
            messagebox.showinfo(title="Emprestimo Status", message="Empréstimo realizado com Sucesso!")
            janela_acervo.withdraw()
            tela_menu.show(data)

        except Exception as error:
            print('Erro ao realizar empréstimo!')
            print(error)
        finally:
            conn.close()

    #def verificarIdItem(idUser, idRecurso):
    #    print(idUser,idRecurso)
    #    if idUser == data[0]:
    #        try:
    #            cursor.execute("UPDATE Emprestimo SET Status = 'Devolvido' WHERE fk_Recursos_ID_item = ? AND fk_Usuarios_ID_user = ?", (idRecurso, data[0]))
    #            conn.commit()
    #            print('Emprestimo atualizado com sucesso!')
    #            messagebox.showinfo(title="Emprestimo Status", message="Empréstimo devolvido com Sucesso!")
    #            janela_acervo.withdraw()
    #            tela_menu.show(data)
    #        except Exception as error:
    #            print('Erro ao atualizar emprestimo!')
    #            print(error)
    #        finally:
    #            conn.close()
    #    else:
    #        messagebox.showinfo(title="Emprestimo Status", message="Empréstimo não é do Usuário!")

    def verificarIdItem(idUser, idRecurso, data, conn, cursor):
        print(idUser, idRecurso)
        if idUser == data[0]:
            try:
                cursor.execute("SELECT * FROM Emprestimo WHERE fk_Recursos_ID_item = ? AND fk_Usuarios_ID_user = ?", (idRecurso, idUser))
                result = cursor.fetchone()
                print("Resultado da busca antes do UPDATE:", result)
                cursor.execute("UPDATE Emprestimo SET Status = 'Devolvido' WHERE fk_Recursos_ID_item = ? AND fk_Usuarios_ID_user = ?", (idRecurso, idUser))
                conn.commit()
                print('Emprestimo atualizado com sucesso!')
                messagebox.showinfo(title="Emprestimo Status", message="Empréstimo devolvido com Sucesso!")
                # Feche a janela e mostre o menu (certifique-se de que janela_acervo e tela_menu estão definidos)
                janela_acervo.withdraw()
                tela_menu.show(data)
            except Exception as error:
                print('Erro ao atualizar empréstimo!')
                print(error)
            finally:
                # Não feche a conexão aqui, pois você pode precisar dela fora desta função.
                pass
        else:
            messagebox.showinfo(title="Emprestimo Status", message="Empréstimo não é do Usuário!")


    def consulta_banco():
        recurso_termo = entrada_termo.get()
        coluna_pesquisa = tipo_combo_box.get()
        tabela_pesquisa = 'LIVRO'

        if coluna_pesquisa == 'Categoria':
            tabela_pesquisa = 'RECURSO'
        
        query = f"SELECT * FROM {tabela_pesquisa} WHERE {coluna_pesquisa} = ?"
        cursor.execute(query, (recurso_termo,))
        lista_recurso = cursor.fetchall()
        if not len(lista_recurso) > 0:
            messagebox.showerror(title="Recurso Status falho", message="Recurso não encontrado!")

        barra_resultados = Frame(janela_acervo, width=800, height=100, relief="flat")
        barra_resultados.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)
        # barra_resultados.destroy()
        try:
            for recurso in lista_recurso:
                id_busca = 0
                if tabela_pesquisa == 'LIVRO':
                    query_isbn= f"SELECT ID FROM RECURSO WHERE fk_LIVRO_ISBN = ?"
                    cursor.execute(query_isbn, (recurso[0],))
                    id_emprestimo = cursor.fetchone()
                    id_busca = id_emprestimo[0]

                    #querry_comparacao_id_isbn = f"SELECT Status FROM EMPRESTIMOS WHERE fk_ID_Recursos = ?"

                else:
                    id_busca = recurso[0]

                query_status = f"SELECT * FROM EMPRESTIMO WHERE fk_Recursos_ID_Item = ? AND Status = 'Emprestado' "
                cursor.execute(query_status, (id_busca, ))
                resultado_status = cursor.fetchone()
                print(resultado_status)

                status_emprestimo = resultado_status[2]
                idUser = resultado_status[4]
                print(status_emprestimo, idUser)
                if status_emprestimo == None or status_emprestimo[0] == '' or  status_emprestimo[0] == 'Devolvido':
                    status_emprestimo = 'Disponível'
                    tk.Button(barra_resultados, text="Emprestar", font=("Verdana", 12, "bold"), command=lambda idItem=recurso[0]: alugar(idItem)).grid(column=2)
                else:
                    tk.Button(barra_resultados, text="Devolver", font=("Verdana", 12, "bold"), command=lambda idUserRecurso = idUser: verificarIdItem(idUserRecurso, recurso[0], data, conn, cursor)).grid(column=2)

                print(recurso)
  

                tk.Label(barra_resultados, text=recurso, font=("Verdana", 12, "bold")).grid(column=0)
                tk.Label(barra_resultados, text=status_emprestimo, font=("Verdana", 12, "bold")).grid(column=1)

        except:
            messagebox.showerror(title="Recurso Status falho", message="Recurso não encontrado!")

#Dividindo a janela------------------------------------------------------------------------------------------
    barra_titulo = Frame(janela_acervo, width=800, height=200, relief="flat")
    barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    barra_dados = Frame(janela_acervo, width=800, height=200, relief="flat")
    barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    barra_posCombo = Frame(janela_acervo, width=800, height=200, relief="flat")
    barra_posCombo.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

    barra_botao = Frame(janela_acervo, width=800, height=100, relief="flat")
    barra_botao.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)


    

    tk.Label(barra_titulo, text="Acervo de Consulta", font=("Verdana", 30, "bold")).grid(padx=250)
    
    tk.Label(barra_dados, text="Selecione a referencia de pesquisa", font=("Verdana", 12, "bold")).grid(row=1, column=0)

    n = tk.StringVar()
    tipo_combo_box = ttk.Combobox(barra_dados, width= 15, textvariable=n, font=("Verdana", 12, "bold"))
    tipo_combo_box["values"] = ("Titulo", "Autor", "Categoria")
    tipo_combo_box.grid(row= 1, column=1)
    
    tk.Label(barra_posCombo, text="Termo de pesquisa: ", font=("Verdana", 12, "bold")).grid(row=3, column=0)
    entrada_termo = tk.Entry(barra_posCombo)
    entrada_termo.grid(row=3, column=1)

    botao_acervo = tk.Button(barra_botao, text="Buscar",font=("Verdana", 12, "bold"), command=consulta_banco).grid()

    janela_acervo.mainloop()
