saudacao = '\n*** Seja bem vindo ao Python Unibanco ***\n'

def menu():
    print('\nOperações disponíveis:\n')
    print('[1] - Saque')
    print('[2] - Depositar')
    print('[3] - Consultar Saldo')
    print('[4] - Consultar Extrato')
    print('[5] - Sair')
    print('\n\n')


#Desenvolvimento das funções
def saque(*,valor, saldo_em_conta, extrato):
    if saldo_em_conta < 0 or valor > saldo_em_conta:
        print('Valor em Conta Insuficiente!.')
        print(f'Saldo Atual: R$: {saldo_em_conta}')
    else:
        saldo_em_conta -= valor
        print(f'Saque no valor de R$ {valor} realizado!.')
        print(f'Saldo Atual: R$ {saldo_em_conta}')
        extrato += f'Saque Realizado: R$ {valor}\n'
    return saldo_em_conta, extrato    

def deposita(valor, saldo_em_conta, extrato,/):
    saldo_em_conta += valor
    extrato += f'Deposito Realizado: R$ {valor}\n'
    return saldo_em_conta, extrato

def consulta_saldo(saldo_em_conta):
    print('*** Saldo Atual ***')
    print(f'R${saldo_em_conta}\n')
     
def consulta_extrato(saldo_em_conta, /, *, extrato ):    
    print('****************** Extrato Bancario ***************\n')
    print('Sem Movimentações no Período.' if not extrato else extrato)
    print(f'Saldo Atual: {saldo_em_conta}.')
    print('\n****************** ** ***************************\n')


def criar_usuario(nome, / , cpf, data_nascimento, email, senha):
    if not nome:
        raise ValueError("Nome do usuário não pode ser vazio.")
    if not cpf:
        raise ValueError("CPF do usuário não pode ser vazio.")
    if not data_nascimento:
        raise ValueError("Data de nascimento do usuário não pode ser vazia.")
    if not email:
        raise ValueError("Email do usuário não pode ser vazio.")
    if not senha:
        raise ValueError("Senha do usuário não pode ser vazia.")

    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "email": email,
        "senha": senha
    }

    print(f"Usuario criado com sucesso: {usuario}")
    return usuario

conta = 0
def gerar_numero_conta():
    global conta
    conta += 1
    return f"{conta:04}"

def criar_conta(usuario_id, /, tipo_conta, saldo_inicial):
    if not usuario_id:
        raise ValueError("ID do usuário não pode ser vazio.")
    if not tipo_conta:
        raise ValueError("Tipo da conta não pode ser vazio.")
    if saldo_inicial < 0:
        raise ValueError("Saldo inicial da conta não pode ser negativo.")

    numero_conta = gerar_numero_conta()
    
    conta = {
        "numero_conta": numero_conta,
        "usuario_id": usuario_id,
        "tipo_conta": tipo_conta,
        "saldo_inicial": saldo_inicial
    }

    if usuario_id not in contas_banco:
        contas_banco[usuario_id] = []
        
    contas_banco[usuario_id].append(conta)
    print(f"Conta criada com sucesso para o usuario {usuario_id}: {conta}")
    return conta

def solicitar_criacao_conta(usuario_id):
    tipo_conta = input("Informe o tipo de conta (corrente ou poupança): ")
    saldo_inicial = float(input("Informe o saldo inicial: "))
    return criar_conta(usuario_id, tipo_conta, saldo_inicial)


def autenticar_usuario(cpf, senha, usuarios_banco):
    if cpf in usuarios_banco and usuarios_banco[cpf]["senha"] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("CPF ou senha inválidos.")
        return False
    
def verificar_conta_usuario(usuario_id):
    # verificando se o usuário já tem uma conta   
    return usuario_id in contas_banco and len(contas_banco[usuario_id]) > 0    

#iniciando o codigo para excução das funções

usuarios_banco = {}  # armazenamento de usuários
contas_banco = {}    # armazenamento de contas
usuario_logado = False
usuario_id = None
saldo_em_conta = 1000
extrato = ""  

print(f'{saudacao}')
   
opcao = 0
    
while True:
    if usuario_logado:
        menu()
        opcao = int(input('\nInforme a operação desejada:\n'))
        if opcao == 1:
            valor_saque = float(input('Informe o valor de Saque:\n'))
            saldo_em_conta, extrato = saque(valor_saque, saldo_em_conta, extrato)
        elif opcao == 2:
            valor_deposito = float(input('Informe o valor para deposito:\n'))
            saldo_em_conta, extrato = deposita(valor_deposito, saldo_em_conta, extrato)
        elif opcao == 3:
            consulta_saldo(saldo_em_conta)
        elif opcao == 4:
            consulta_extrato(extrato, saldo_em_conta)
        elif opcao == 5:
            break
        else:
            print('Operação Invalida, selecione a opção desejada.')
    else:
        print("Você precisa estar logado para realizar operações.")
        opcao = int(input('\n1. Criar Usuário\n2. Login\n0. Sair\nOpção: '))
        if opcao == 1:
            nome = input("Informe seu nome completo: ")
            cpf = input("Informe seu CPF: ")
            data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
            email = input("Informe seu email: ")
            senha = input("Informe sua senha: ")
            usuario = criar_usuario(nome, cpf, data_nascimento, email, senha)
            usuarios_banco[cpf] = usuario
            usuario_logado = True
            usuario_id = cpf
            if not verificar_conta_usuario(usuario_id):
                solicitar_criacao_conta(usuario_id)
        elif opcao == 2:
            cpf = input("Informe seu CPF: ")
            senha = input("Informe sua senha: ")
            usuario_logado = autenticar_usuario(cpf, senha, usuarios_banco)
            if usuario_logado:
                usuario_id = cpf
                if not verificar_conta_usuario(usuario_id):
                    solicitar_criacao_conta(usuario_id)
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")
            