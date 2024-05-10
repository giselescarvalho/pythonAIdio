import textwrap

def menu():
    menu = """
    [d] \tDepositar
    [s] sacar
    [e] extrato
    [n] nova conta
    [u] novo usuário
    [l] listar contas
    [q] sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso ###")
    else:
        print("## Operação falhou! O valor informado nao pode ser negativo")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("#### Operação falhou! Saldo insuficiente")
    elif excedeu_limite:
        print("##### Operação falhou! O valor do saques excede o limite")
    elif excedeu_saques:
        print("###### Operação falhou! Número máximo de saques excede o limite")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("####### Operação falhou! O valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("==========================================+")
    print("----------------- EXTRATO -----------------")   
    print("Não foram realizadas movimentações" if not extrato else extrato) 
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================+")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF")
        return
    
    nome = input("informe nome completo: ")
    data_nascimento = input("informe a data de nascimento no formato dd-mm-aaa: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    #dicionario:
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("@@@ Usuário cadastrado com sucesso")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Conta criada com sucesso ")
        #dicionario
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("###\n#   Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    pass

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo UnboundLocalError= 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("######### Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("Saque")
            valor = float(input("### Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif "n": # nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif "u": #novo usuário
            criar_usuario(usuarios)
        
        elif "l": # listar contas
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("opção inválida")



main()