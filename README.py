# Sistema-Bancario-Basico-DIO-
print(" ########## Ben-vindo ao banco Mascarenhas ###########")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação inválida! Não é possível depositar valor nulos ou negativo")
    
    elif opcao == "2":
        valor = float(input("Informe o valor desejado para saque: "))
        
        excedeu_o_saldo = valor > saldo
        excedeu_o_limite = valor > limite 
        excedeu_n_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_o_saldo:
            print("O valor solicitado excede o saldo atual!")
        elif excedeu_o_limite:
            print("O valor solicitado excede o limite diário!")
        elif excedeu_n_saques:
            print("Já utilizou o número de limites de saques diários!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido!")
            
    elif opcao == "3":
        print("\n******************************  E X T R A T O ******************************")
        print("Conta sem movimentações!!! " if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("******************************************************************************")
    elif opcao =="0":
        break
    else:
        print("Operação inválida. Por gentileza,selecione uma das operações do menu!")
