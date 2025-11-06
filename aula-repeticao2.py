print("#####CADASTRO DE USUARIO######\n\n")
usuario_cadastrado = input("Nome: ").lower() .strip()
#inicia um loop para o usuario digitar uma senha de 8 digitos, caso digite um número de digitos diferente ele vai voltar a pedir a senha
while True:
    senha_cadastro = input("Senha: ").strip()
    
    if len(senha_cadastro) == 8:
        print("Usuário cadastrado com sucesso!!\n")
        break
    else:
        print("Sua senha deve ter 8 caracteres, digite novamente")

print("######  Login  #####\n")

#Inicia o loop que vai se repetir enquanto a condição for verdadeira
while True:# True é a condição booleana que sempre é verdadeira, logo esse loop será infinito 
    nome = input("Usuário: ").lower() .strip()
    senha = input("senha: ").strip()
    #condição booleana que vai verificar se amabas as condições são verdadeiras
    if nome == usuario_cadastrado and senha == senha_cadastro:
        print("Login realizado com sucesso!")
        break #Comando que interrompe imediatamente o loop
    else:
        print("Usuário ou senha incorretas! Tente novamente!")