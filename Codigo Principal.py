menu = '''

          "Banco"          

   [A] Saque
   [B] Deposito
   [C] Extrato
   [E] Sair

'''
saldo = 500
limite = 1500
extrato = ""
numeros_de_saques = 0
LIMITE_DE_SAQUES = 4

while  True:

    opcao = input(menu) 
    
    if opcao == "A":
        valor = int(input("Valor de Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_limite_de_saques = numeros_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print ("Saldo Insuficiente!")
        elif excedeu_limite:
            print("Limite de Saque Excedido!")
        elif excedeu_limite_de_saques:
            print("Limite de Saque diarios excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_de_saques += 1
        
        else:
            print ("Operação Com Erro Tente Novamente!")



    if opcao == "B":
        valor = int(input("Valor de Deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print ("Operação Com Erro Tente Novamente!")

    elif opcao == "C":
        print("========EXTRATO========")
        print("Operações Inexistentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================")

    elif opcao == "E":
        break

    else:
        ("Operação Não Reconhecida Tente Novamente!") 