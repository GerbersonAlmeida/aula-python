#programa que pede usuario e senha 
usuario = input("Cadastre usuario: ")
senha = input("Cadastre senha: ")

print("\n###### USUÁRIO CADASTRADO COM SUCESSO ######\n\n")
usuario1 = str(input("Informe o usuario: "))
senha1 = str(input("Senha: "))
if usuario == usuario1 and senha == senha1:
    nivel = int(input("Qual seu nivel de usuário: (1 ou 2)"))
    if nivel == 1:
        print("Bem-vindo, administrador!!")
    elif nivel == 2:
        print("Bem_vindo, usuário!!")
    else:
        print("Nivel de usuário não encontrado!!")
else:
    print("Usuário ou senha incorretos!!")