usuarios = []
contas = []
AGENCIA = "0001"

def cadastrar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf)
    
    if usuario:
        print("Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")
    
    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado. Cadastre-o primeiro.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": AGENCIA,
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "saques_diarios": 0
    })

    print(f"Conta criada com sucesso. Agência: {AGENCIA}, Conta: {numero_conta}")

def depositar(conta):
    valor = float(input("Valor do depósito: R$ "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def sacar(conta):
    valor = float(input("Valor do saque: R$ "))
    
    if valor > 500:
        print("Saque acima do limite de R$ 500 por operação.")
    elif conta["saques_diarios"] >= 3:
        print("Limite de 3 saques diários atingido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["saques_diarios"] += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido.")

def exibir_extrato(conta):
    print("\n====== EXTRATO ======")
    if not conta["extrato"]:
        print("Não há movimentações.")
    else:
        for mov in conta["extrato"]:
            print(mov)
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("=======================")

# Exemplo de loop principal (interface)
def menu():
    while True:
        print("""
        [1] Cadastrar usuário
        [2] Cadastrar conta
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [6] Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cadastrar_conta()
        elif opcao in ["3", "4", "5"]:
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)

            if not conta:
                print("Conta não encontrada.")
                continue

            if opcao == "3":
                depositar(conta)
            elif opcao == "4":
                sacar(conta)
            elif opcao == "5":
                exibir_extrato(conta)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()