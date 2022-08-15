listaPeca = []
#---------------- COMEÇO cadastrarPeca -----------------
def cadastrarPeca (codigo):
    print('Cadastre a peça desejada!')
    print('O código da peça é: {}'.format(codigo))
    nome = input('Qual o nome da peça? ')
    fabricante = input('Qual o fabricante da peça? ')
    valor = input('Qual o valor da peça? ')
    dicionarioPeca = {'codigo' : codigo,'nome': nome, 'fabricante': fabricante, 'valor': valor}
# ---------------- FIM cadastrarPeca -----------------

    listaPeca.append(dicionarioPeca.copy())
#---------------- COMEÇO consultarPeca -----------------
def cosultarPeca():
    while True:
        try:
            consultar = int(input('Entre com a opção desejada:\n'
                                  '1 - Consultar Todas as Peças\n'
                                  '2 - Consultar por Código\n'
                                  '3 - Consultar por fabricante\n'
                                  '4 - Retornar ao Menu\n'
                                  '>'))
            if consultar == 1:
                print('Essas são todas as peças cadastradas!')
                for peca in listaPeca: #seleciona cada dicionario dentro da lista.
                    print('-' * 10)
                    for key, value in peca.items(): #seleciona cada conjunto de chave/valor do dicionario.
                        print('{} : {}'.format(key,value))
            elif consultar == 2:
                print('Você escolheu a consulta de peça por código!')
                entrada = int(input('Digite o código da peça: '))
                for peca in listaPeca:
                    if(peca['codigo'] == entrada):
                        print('-' * 10)
                        for key, value in peca.items():
                            print('{} : {}'.format(key,value))
            elif consultar == 3:
                print('Você escolheu consultar pelo fabricante!')
                entrada = input('Digite o fabricante da peça: ')
                for peca in listaPeca:
                    if(peca['fabricante'] == entrada):
                        print('-' * 10)
                        for key, value in peca.items():
                            print('{} : {}'.format(key,value))
            elif consultar == 4:
                break
            else:
                print('O número digitado é inválido!')
                print('Você pode consultar apenas as peças existentes!')

        except ValueError:
            print('Você digitou algum caracter com um valor não númerico...')
#---------------- FIM consultarPeca -----------------

#---------------- COMEÇO removerPeca -------------------
def removerPeca():
    print('Remova a peça desejada!')
    entrada = int(input('Digite o codigo da peça a ser removida: '))
    for peca in listaPeca:
        if (peca['codigo'] == entrada):
            listaPeca.remove(peca)
            print('Peça removida com sucesso!')
#---------------- FIM DO removerPeca -------------------

#---------------- COMEÇO DO PROGRAMA -------------------
print('Bem-Vindo ao Controle de Estoque da Bicicletaria do Davi Alves de Andrade')
codigo = 0
while True:
    try:
        opcao = int(input('Digite a opção desejada: \n'
                           '1 - Cadastrar peça\n'
                           '2 - Consultar peça\n'
                           '3 - Remover peça\n'
                           '4 - Sair\n' #Finaliza o programa dando um "break".
                           '>'))
        if opcao == 1:
            codigo += 1
            cadastrarPeca(codigo)
        elif opcao == 2:
            cosultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Fim de programa...')
            break
        else:
            print('O número digitado é inválido!')


    except ValueError:
        print('Você digitou algum objeto com um valor não númerico...')  # Caso o usúario digite uma letra, ocorrerá um erro e será solicitado um valor real novamente.
#---------------- FIM DO PROGRAMA -----------------
