#---------------- COMEÇO DO PROGRAMA -----------------
print('Bem-Vindo a Companhia de Logística Davi Alves de Andrade ')
#---------------- COMEÇO dimensoesObjeto -------------
def dimensoesObjeto():
    while True: #Foi criado um laço de repetição para cada passo de envio do produto.
        try:
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
            altura = float(input('Digite a altura do objeto (em cm): '))
            volume = comprimento * largura * altura
            print('O volume do objeto é (em cm^3): {}'.format(volume)) #Aqui será disponibilizado o tamanho do nosso objeto.
            if comprimento == 0 or largura == 0 or altura == 0: #caso um dos valores das dimensões forem zero, o objeto não existe, sendo inválido para o nosso calculo.
                print('Você digitou alguma dimensão do objeto com o valor "0"')
                print('Por favor entre com as dimensões desejadas novamente!')
                continue
            elif (volume <1000):
                return 10

            elif (volume >= 1000) and (volume < 10000):
                return 20

            elif (volume >= 10000) and (volume < 30000):
                return 30

            elif (volume >= 30000) and (volume < 100000):
                return 50

            else:
                print('Não aceitamos objetos com dimensões tão grandes...')
                print('Por favor entre com as dimensões desejadas novamente!')
                continue
        except ValueError:
            print('Você digitou alguma dimensão do objeto com um valor não númerico...') #Caso o cliente digite uma letra, ocorrerá um erro e será solicitado um valor real novamente.
            print('Por favor entre com as dimensões desejadas novamente!')
            continue
#---------------- FIM do dimensõesObjeto --------------

#---------------- COMEÇO do pesoObjeto ----------------
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): ')) #Aqui será disponibilizado o peso do nosso objeto.
            if (peso <= 0.1):
                return 1
            elif (peso > 0.1) and (peso < 1):
                return 1.5
            elif (peso >= 1) and (peso < 10):
                return 2
            elif (peso >= 10) and (peso < 30):
                return 3
            else:
                print('Não aceitamos objetos tão pesados...')
                print('Por favor entre com o peso desejado novamente!')
                continue
        except ValueError:
            print('Você digitou o peso do objeto com um valor não númerico...')
            print('Por favor entre com o peso desejado novamente!')
            continue
#---------------- FIM do pesoObjeto ------------------

#---------------- COMEÇO do rotaObjeto ---------------
def rotaObjeto():
    while True:
        try:
            print('BR - De Brasília para Rio de Janeiro')
            print('BS - De Brasília para São paulo')
            print('RB - De Rio de Janeiro para Brasília')
            print('RS - De Rio de Janeiro para São Paulo')
            print('SR - De São Paulo para Rio de Janeiro')
            print('SB - De São Paula para Brasília')
            rota = input('Selecione a rota: ') #Aqui será decidida a rota do envio.

            if rota == 'RS':
                return 1
            elif rota == 'SR':
                return 1
            elif rota == 'BS':
                return 1.2
            elif rota == 'SB':
                return 1.2
            elif rota == 'BR':
                return 1.5
            elif rota == 'RB':
                return 1.5
            else:
                print('Você digitou uma rota inexistente...')
                print('Por favor entre com a rota desejada novamente!')
                continue

        except ValueError:
            print('Por favor entre com a rota desejada novamente!')
#---------------- FIM do rotaObjeto ------------------

dimensoesFinal = dimensoesObjeto()
pesoFinal = pesoObjeto()
tarifasFinal = rotaObjeto()
valor_total = dimensoesFinal * pesoFinal * tarifasFinal

print('Total a pagar: R$ {:.2f} (tarifa do objeto: {} * tarifa do peso: {} * tarifa da rota: {})'.format(valor_total, dimensoesFinal, pesoFinal, tarifasFinal)) #Aqui será disponibilizado os dados contabilizados e o total a ser pago.
#---------------- FIM DO PROGRAMA --------------------





