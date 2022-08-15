#---------------- COMEÇO DO PRAGRAMA ------------------
print('Bem-Vindo a lanchonete de Davi Alves de Andrade')
print('*' *18 + 'Cardápio'+ '*' * 18)
print('| Código |       Descrição       |   Valor |')
print('|   100  |     Cachorro-Quente   | R$  9.00|')
print('|   101  | Cachorro-Quente Duplo | R$ 11,00| ')
print('|   102  |         X-Egg         | R$ 12,00| ')
print('|   103  |       X-Salada        | R$ 13,00| ')
print('|   104  |        X-Bacon        | R$ 14,00| ')
print('|   105  |        X-Tudo         | R$ 17,00| ')
print('|   200  |    Refrigerante Lata  | R$  5,00| ')
print('|   201  |      Chá Gelado       | R$  4,00| ')

total = 0
#---------------- COMEÇO DO LAÇO DE REPETIÇÃO ------------------
while True: #Toda vez que o cliente errar ou fizer um novo pedido ele voltará para o menu princial.
    produto = int(input('Entre com o código do produto desejado: \n')) #O cliente poderá escolher os produtos utilizando o código disponibilizado.
    if produto == 100:
        print('Você escolheu Cachorro-Quente no valor de R$ 9.00 ')
        total += 9.00
    elif produto == 101:
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 12.00 ')
        total += 12.00

    elif produto == 102:
        print('Você escolheu X-Egg no valor de R$ 12,00 ')
        total += 12.00

    elif produto == 103:
        print('Você escolheu X-Salada no valor de R$ 13,00 ')
        total += 13.00

    elif produto == 104:
        print('Você escolheu X-Bacon no valor de R$ 14,00 ')
        total += 14.00

    elif produto == 105:
        print('Você escolheu X-Tudo no valor de R$ 17,00 ')
        total += 17,00


    elif produto == 200:
        print('Você escolheu Refrigerante Lata no valor de R$ 5,00 ')
        total += 5.00

    elif produto == 201:
        print('Você escolheu Chá Gelado no valor de R$ 4,00 ')
        total += 4.00
    else:
        print('Escolha um código valido!')
        continue
    nova_compra = input('Você deseja pedir mais alguma coisa?\n'
                        '1 - SIM\n'
                        '0 - NÃO\n') # Se o cliente escolher "sim" ele volta para pedir novamente, caso contrário, ele encerra com o total a ser pago.
    if nova_compra == '1':
        continue
    elif nova_compra == '0':
        print('Obrigado! O total da sua compra foi: R$ {:.2f}'.format(total)) # Aqui termina o nosso programa com o cliente satisfeito.
        break
#---------------- FIM DO LAÇO DE REPETIÇÃO ------------------
    else:
        print('Opção invalida... Voltando para o menu principal!')
        continue
#---------------- FIM DO PROGRAMA ------------------