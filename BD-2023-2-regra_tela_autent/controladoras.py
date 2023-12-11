import modelos
import servicos

#controladora usuario
def controladora_usuario():
    import modelos
    import tela_autenticacao

    def on_autenticado(usuario):
        print('Usuário '+usuario.login+ ' autenticado com sucesso!')
    
    def on_nao_autenticado():
        print('Login ou senha inválidos!')

    def on_autenticar_click(loginDaTela, senhaDaTela):
        login = loginDaTela
        senha = senhaDaTela
        print(login)
        print(senha)
        servicos.servico_autenticar(login, senha, on_autenticado, on_nao_autenticado)

    tela_autenticacao.show(on_autenticar_click)
