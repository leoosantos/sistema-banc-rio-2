menu = """

[d] Despositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("-------------------- Depósito --------------------")
        dep = float(input("\nInforme o valor que deseja depositar: "))
        saldo += dep
        extrato.append(f"...Deposito\t\t\t\t+ R$ {str(dep)}")
        print(f"\nSaldo Atual: R$ {saldo}\n")
        print("--------------------------------------------------")
        
    elif opcao == "s":
        print("-------------------- Saque --------------------")
        if numero_saques == LIMITE_SAQUES:
            print("\n  Você atingiu o limite de vezes para saque.\n")
        elif limite <= 0:
            print("\n   Você atingiu o limite diário de saque.\n")
        else:
            saque = float(input("\nInforme o valor que deseja sacar: "))
            if (saldo >= saque) and (saque <= limite):
                extrato.append(f"...Saque\t\t\t\t- R$ {str(saque)}")
                limite -= saque
                saldo -= saque
                numero_saques += 1
                print("\nSaque realizado com sucesso!")
                print(f"\nLimite atual: R$ {limite}\n")
            else:
                print("\nValor indisponível para saque.")
        print("-----------------------------------------------")
        
    elif opcao == "e":
        print("-------------------- Extrato --------------------")
        for i in range(len(extrato)):
            print(f"\n{extrato[i]}")
        print(f"\n\t\tSaldo Atual: R$ {saldo}\n")
        print("-------------------------------------------------")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")