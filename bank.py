def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! Por favor, insira um número válido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))
        
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Por favor, insira um número válido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema!")
            break
        
        else:
            print("Operação inválida, por favor selecione uma opção válida.")

# Executa o programa
if __name__ == "__main__":
    main()