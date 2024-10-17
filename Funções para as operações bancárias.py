# Funções para as operações bancárias
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nValor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, valor, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nSaldo insuficiente para saque.")
    elif valor > limite:
        print("\nO valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("\nNúmero máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nValor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def exibir_menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """
    return input(menu)

# Função principal para execução do sistema
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "2":
            valor = float(input("\nInforme o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            print("\nObrigado por usar o sistema bancário!")
            break

        else:
            print("\nOpção inválida! Por favor, selecione uma opção válida.")

# Executar o sistema bancário
if __name__ == "__main__":
    main()
