print('Bem-Vindo a Loja do Davi Alves de Andrade!')
valorproduto = float(input('Digite o valor do produto: R$ '))
quantidade = int(input('Digite a quantidade de produtos: '))
total = valorproduto * quantidade
print('O valor sem desconto é de: R$ {:.2f}'.format(valorproduto * quantidade))

if (quantidade >= 10) and (quantidade < 100):
    desconto = total - (total * 0.05)
    print('O valor com desconto é de: R$ {:.2f} (desconto de 5%)'.format(desconto))

elif (quantidade >= 100) and (quantidade < 1000):
    desconto = total - (total * 0.10)
    print('O valor com desconto é de: R$ {:.2f} (desconto de 10%)'.format(desconto))
elif quantidade >= 1000:
    desconto = total - (total * 0.15)
    print('O valor com desconto é de: R$ {:.2f} (desconto de 15%)'.format(desconto))
else:
    print('Você comprou menos de 10 unidades, por isso não haverá desconto!')