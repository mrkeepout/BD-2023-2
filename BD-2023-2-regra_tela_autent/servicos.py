import modelos

#controladora usuario
def servico_autenticar(login, senha, on_autenticado, on_nao_autenticado):
    usuario2 = modelos.Usuario.buscar(login)
    if usuario2 is None:
        on_nao_autenticado()
        return
    #salt = '5gz'
    salt = modelos.Usuario.salt
    hash_senha = servico_salgar_senha(salt, senha)
    print(hash_senha +"\n")
    if usuario2 is not None:
        print(usuario2.senha)
    if usuario2.senha == hash_senha:
        on_autenticado(usuario2)
    else:
        on_nao_autenticado()

def servico_salgar_senha(salt, senha):
    import hashlib
    senha = senha + salt
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()
   