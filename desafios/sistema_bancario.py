menu = """
Bem-vindo ao sistema bancário!
Escolha uma opção:

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

"""

saldo= 0
limite = 500
extrato = ""
numeroSaque = 0
LIMITESAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valorSaque = float(input("Informe o valor do saque: "))

        if valorSaque > saldo:
            print("Saldo insuficiente!")
        elif valorSaque > limite:
            print("Valor acima do limite de saque!")
        elif numeroSaque >= LIMITESAQUE:
            print("Número máximo de saques atingido!")
        else:
            saldo -= valorSaque
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            numeroSaque += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        valorDeposito = float(input("Informe o valor do depósito: "))
        if valorDeposito <= 0:
            print("Valor inválido para depósito!")
        else:
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        print("\nExtrato:")
        if extrato == "":
            print("Nenhuma transação realizada.")
        else:
            print(extrato)

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")