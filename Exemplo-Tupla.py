numeros = () #Criação de tupla com o nome números que irá guardar números fornecidos pelo usuario

    #Estrutura de repetição para permitir que o usuário digite varios numeros
while True:
    n = int(input("Digite um número (ou -1 para sair): "))
    if n == -1:
        break
    numeros+=(n,)
#Estrutura que mostra o resumo com informações importantes dos dados na tupla  
if len(numeros) > 0: # O len mostra a quantidade de casas que tem a tupla número
    print("\n===== RESULTADOS =====") 
    print(f"Números digitados: {numeros}")
    print(f"Quantidade: {len(numeros)}")
    print(f"Soma: {sum(numeros)}") # sum soma os dados das casas da tupla numero
    print(f"Maior número: {max(numeros)}") # max mostra qual dos números digitados é o maior
    print(f"Menor número: {min(numeros)}") # min mostra qual dos números digitados é o menor
    
    media = sum(numeros)/len(numeros)
    
    if media >= 50:
        print(f"Média: {media:.2f} -> Alta!")
    else:
        print(f"Média: {media:.2f} -> Baixa!")
        
else:
    print("Nenhum número foi adcionado!")