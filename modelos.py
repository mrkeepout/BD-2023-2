import sqlite3
import hashlib

#Modelo Classe Usuario
class Usuario:
    salt = '5gz'

    def __init__(self):
        pass

    def __str__(self):
        return f'Nome: {self.nome} {self.sobrenome}\nLogin: {self.login}\nUri Foto Usuario: {self.uri_foto_user}\nFunção: {self.funcao}'

    def salvar(self):
        
        try:
            conexao_bd = sqlite3.connect('sgmld_sem_heranca_alim.db')
            cursor = conexao_bd.cursor()
#            salt = '5gz'
            self.senha = self.senha + salt
            hash_senha = hashlib.sha256(self.senha.encode('utf-8')).hexdigest()
            cursor.execute(f'''INSERT INTO Usuario (Nome, Sobrenome, Login, Senha, URI_foto_user, Funcao)
            VALUES ('{self.nome}', '{self.sobrenome}', '{self.login}', '{hash_senha}', '{self.uri_foto_user}', '{self.funcao}')''')
            conexao_bd.commit()
            print('Usuário cadastrado com sucesso!')
        except Exception as error:
            print('Erro ao cadastrar usuário!')
            print(error)
        finally:
            conexao_bd.close()

    def atualizar(self):
        try:
            conexao_bd = sqlite3.connect('sgmld_sem_heranca_alim.db')
            cursor = conexao_bd.cursor()
            cursor.execute(f'''UPDATE Usuario SET Nome = '{self.nome}', Sobrenome = '{self.sobrenome}', Login = '{self.login}', URI_foto_user = '{self.uri_foto_user}', Funcao = '{self.funcao}' WHERE ID_USER = {self.id_user}''')
            conexao_bd.commit()
            print('Usuário atualizado com sucesso!')
        except Exception as error:
            print('Erro ao atualizar usuário!')
            print(error)
        finally:    
            conexao_bd.close()

    def deletar(self, id_user):
        try:
            conexao_bd = sqlite3.connect('sgmld_sem_heranca_alim.db')
            cursor = conexao_bd.cursor()
            cursor.execute(f'''DELETE FROM Usuario WHERE ID_USER = {id_user}''')
            conexao_bd.commit()
            print('Usuário deletado com sucesso!')
        except Exception as error:
            print('Erro ao deletar usuário!')
            print(error)
        finally:
            conexao_bd.close()

    def buscar(login):
        try:
            conexao_bd = sqlite3.connect('sgmld_sem_heranca_alim.db')
            cursor = conexao_bd.cursor()
            cursor.execute(f'''SELECT * FROM Usuario WHERE Login = "{login}"''')
            resultados = cursor.fetchall()
            if len(resultados) == 0:
                return None
            linha = resultados[0]
            id_user = linha[0]
            nome = linha[1]
            sobrenome = linha[2]
            login = linha[3]
            senha = linha[4]
            uri_foto_user = linha[5]
            funcao = linha[6]
            usuario = Usuario()
            usuario.id_user = id_user
            usuario.nome = nome
            usuario.sobrenome = sobrenome
            usuario.login = login
            usuario.senha = senha
            usuario.uri_foto_user = uri_foto_user
            usuario.funcao = funcao
            return usuario
        
        except Exception as error:
            print('Erro ao buscar usuário!')
            print(error)
        finally:
            conexao_bd.close()
            

    def set_funcao(self, funcao):
        if funcao == 'Administrador' or funcao == 'Chefe do laboratório' or funcao == 'Membro do laboratorio':
            self.funcao = funcao
        else:  
            print('Função inválida!')
            raise Exception('Função inválida!')

    def get_funcao(self):
        return self.funcao
    