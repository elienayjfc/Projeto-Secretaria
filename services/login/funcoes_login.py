#Função da area de login.
def login(usuario,senha):
#Dados que serão puxados do banco de dados.
    usuariodb = "admin"
    senhadb = "admin"
#tentativas de acesso.
    tentativas = 3

    while tentativas > 0:
        #usuario = input("Usuário: ")
        #senha = input("Senha: ")
#Dados corretos!
        if usuario == usuariodb and senha == senhadb:
            print("Login Realizado com sucesso")
            return True
#Dados incorretos!       
        else:
            print("Usuário ou senha incorreto")
            tentativas -= 1
    print("Acesso bloqueado")
    return False

#login() 