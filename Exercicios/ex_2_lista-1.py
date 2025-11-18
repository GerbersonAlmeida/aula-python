nomes = []
salarios = []

while True: 
    nome = input("Digite o nome do funcionario: (ou 'sair' para encerrar )")

    if nome == "sair":
        print("Programa Finalizado!")
        break
    nomes.append(nome)
    
    salario = float(input("Digite o salário do funcionário"))
    
    salarios.append(salario)
    
print(f"O total de funcionarios cadastrados é: {len(nomes)}.")
print(f"A média salarial dos funcionarios é: {sum(salarios)/len(salarios)}.")
print(f"O maior salario é")
    
