#Simulador de empréstimo bancário

print("###### SISTEMA DE ANÁLISE DE CRÉDITO ######")

#Declaração de variveis
nome = str(input("Nome do cliente: "))
renda = float(input("Informe a renda mensal do cliente: R$"))
valor_pedido = float(input("Informe o valor do empréstimo solicitado: "))
parcelas = int(input("Informe o número de parcelas: "))
historico = input("Está negativado? (s/n): ")

#Variavel para encontrar o valor das parcelas
valor_parcela = valor_pedido/ parcelas

#Exibe um resumo inicial do cliente
print(f"\nCliente: {nome}")
print(f"valor do empréstimo: R$ {valor_pedido:.2f}")
print(f"Pacelas: {parcelas}x de R$ {valor_parcela:.2f}")

#Condição para descobrir se a pessoa é negativada 
if historico  == "s": 
    print("Emprestimo negado, nome com restrição!")

else: 
    #Condição para verificar se a parcela não ultrapassa 30% da renda
    print("Não há restrição no nome")
    if valor_parcela > renda *0.3:
        print("Emprestimo negado!, valor das parcelas comprometem mais de 30% da renda.")
    else:
        #Verificar valor do emprestimo em relção á renda
        print("parcelas aprovadas!")
        if valor_pedido > renda*20:
            print("Emprestimo negado! valor solicitado muito alto para a renda informada.")
        elif renda >= 5000 and  valor_pedido <= 10000: 
            print("Emprestimo APROVADO com taxa reduzida! Cliente perfil premium.")
        elif renda >= 3000 and renda < 5000:
            print("Emprestimo APROVADO com taxa padrâo.")
        else:
            print("Emprestimo APROVADO com taxa elevada (cliente de risco).")

print("\n ###### ANALISE CONCLUIDA ######")
