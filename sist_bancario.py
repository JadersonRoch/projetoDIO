#print('Sistema Unibanco Python')

saudacao = '\n*** Seja bem vindo ao Python Unibanco ***'
menu_opcoes = """
    Informe uma das opções abaixo:
    
    [1] - Saque
    [2] - Depositar
    [3] - Consultar Saldo
    [4] - Consultar Extrato
    [5] - Sair

"""

menu_opcoesDois = """
    Informe a opção desejada:
    
    [1] - Saque
    [2] - Depositar
    [3] - Consultar Saldo
    [4] - Consultar Extrato
    [5] - Sair

"""

numero_saque_dia = 3
valor_saque = 0
valor_saldo = 0
movimentacao_saque = []
movimentacao_deposito = []



print(saudacao)
print(menu_opcoes)
opcao = 0
while True:
    
    #print(menu_opcoesDois)
    
    opcao = int(input(''))
    
    if opcao == 1:
      valor_saque = float( input('Informe o valor do Saque:\n'))
      if valor_saque > valor_saldo:
          print('\nSaldo insuficiente em conta!') 
         
      elif numero_saque_dia == 0:
          print('Número de saque diario finalizado.')
          continue 
          
      elif valor_saque <= 500:          
          valor_saldo -= valor_saque
          numero_saque_dia -= 1
          
           #Adiciona na lista as movimentações
          movimentacao_saque.append(('saque',valor_saque))
          print('Saque Realizado.') 
          print(f'\nSaldo Atual: {valor_saldo}')
      else:
          print('Saque não autorizado!\nValor superior ao limite de saque!\n')
          
    elif opcao == 2:
        valor_deposito = float(input('Informe o valor de deposito:'))
        if valor_deposito < 0:
            print(f'\nOperação invalida, informado valor negativo!!')
        else:
            valor_saldo += valor_deposito      
            print(f'Deposito no valor de R$ {valor_deposito} realizado.')
        
              
            #Adiciona na lista as movimentações
            movimentacao_deposito.append(('deposito',valor_deposito) )
    
    elif opcao == 3:
        print(f'\nSaldo Atual da Conta: R$ {valor_saldo}')
        
    elif opcao == 4:
        print('Extrato Bancario:')
        extratos = movimentacao_saque + movimentacao_deposito
        
        for movimentacao in extratos:
            tipo, valor = movimentacao
            
            if tipo == 'deposito':
                print(f'Realizado deposito de R$ {valor}.')
            elif tipo == 'saque':
                print(f'Saque de R$ {valor} realizado.')
                
    elif opcao == 5:
        print('\nFinalizando Transação!\n\n')
        break
    
    print(menu_opcoesDois)
    
        
        
    