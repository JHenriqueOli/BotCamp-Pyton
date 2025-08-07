class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class ContaBancaria:
    LIMITE_SAQUE = 500
    MAX_SAQUES_DIA = 3

    def __init__(self, numero, usuario, agencia="0001"):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > ContaBancaria.LIMITE_SAQUE:
            print("Limite de saque excedido (R$ 500).")
        elif self.saques_diarios >= ContaBancaria.MAX_SAQUES_DIA:
            print("Limite de saques diários atingido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            print("Saque realizado com sucesso.")

    def exibir_extrato(self):
        print(f"\n===== EXTRATO - Conta {self.numero} =====")
        if not self.extrato:
            print("Não há movimentações.")
        else:
            for mov in self.extrato:
                print(mov)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("======================================")

# Sistema principal para gerenciar usuários e contas
class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self):
        cpf = input("Informe o CPF: ")
        if self.buscar_usuario_por_cpf(cpf):
            print("Usuário já cadastrado.")
            return

        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")

        novo_usuario = Usuario(nome, nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso.")

    def buscar_usuario_por_cpf(self, cpf):
        return next((u for u in self.usuarios if u.cpf == cpf), None)

    def cadastrar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.buscar_usuario_por_cpf(cpf)
        if not usuario:
            print("Usuário não encontrado.")
            return

        numero_conta = len(self.contas) + 1
        nova_conta = ContaBancaria(numero_conta, usuario)
        self.contas.append(nova_conta)
        print(f"Conta criada com sucesso. Número: {numero_conta}, Agência: {nova_conta.agencia}")

    def buscar_conta_por_numero(self, numero):
        return next((c for c in self.contas if c.numero == numero), None)

    def menu(self):
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
                self.cadastrar_usuario()
            elif opcao == "2":
                self.cadastrar_conta()
            elif opcao in ["3", "4", "5"]:
                try:
                    numero = int(input("Informe o número da conta: "))
                    conta = self.buscar_conta_por_numero(numero)
                    if not conta:
                        print("Conta não encontrada.")
                        continue

                    if opcao == "3":
                        valor = float(input("Valor do depósito: R$ "))
                        conta.depositar(valor)
                    elif opcao == "4":
                        valor = float(input("Valor do saque: R$ "))
                        conta.sacar(valor)
                    elif opcao == "5":
                        conta.exibir_extrato()
                except ValueError:
                    print("Entrada inválida.")
            elif opcao == "6":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida.")

# Iniciar o sistema
if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.menu()