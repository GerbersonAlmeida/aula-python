
#Laço For para mostrar no intervalo de 100 números quais são impar e quais são par, RANGE na estrutura subistitui o "i++"
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} é par\n")
    else:
        print(f"{i} é impar\n")
        