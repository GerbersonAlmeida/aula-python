def cadastrar_produto(estoque):
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    estoque(nome) = qtd
    print("Produto cadastrado")
    
def vender(estoque):
    nome = input("Produto para vender: ")
    if nome in estoque and estoque[nome] > 0:
        estoque[nome] -= 1
        print("Venda realizada! ")
    else:
        print("Produto indispensavel!")
        
def mostrar(estoque):
    print("\n-------- ESTOQUE---------")
    for p, q in estoque.items():
        print(f"{p}:{q}")
        
def menu():
    estoque = {}
    