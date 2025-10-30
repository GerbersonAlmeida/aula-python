#Solicitando ao usuario que informe a hora atual (apenas o número da hora)
hora = int(input("Digite a hora atual(0 a 23): "))

#Estrutura condicional para verificar se é de manhã, tarde ou noite
if hora <= 18: 
    print("Bom dia!")
elif hora > 12 and hora < 18:
    print("Boa tarde!")
else: 
    print("Boa noite!")
