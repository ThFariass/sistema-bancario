menu = """ 

[D] Despositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Digite o valor para deposito: "))
         
        if valor > 0:
            saldo += valor
            extrato += f"\nDeposito {valor:.2f}"
        else:
            print("Operação invalida")

    elif opcao == "s":
        valor = float(input("Valor que deseja sacar: "))
        
        excedeu_valor = valor > saldo
            
        excedeu_limite = valor > limite
            
        execedeu_saque = numero_saques >= LIMITE_SAQUE
            
        if excedeu_valor:
            print("Operação invalida por conta de saldo")
        elif excedeu_limite:
            print("Operação invalida por conta de limite")
        elif execedeu_saque:
            print("Operação invalida por conta de saque")
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque de {valor:.2f}"
            numero_saques += 1
            
        else: 
            print("volar falhou")
    
    elif opcao == "e":
        print("=========EXTRATO=========")
        print("nao foram realizadas movimentações" 
              if not extrato 
              else extrato
)
        print(f"\nextrato de {saldo:.2f}")
        print("=====================")
    elif opcao == "q":
        break 
    
    else:
        print("Operação invalida")