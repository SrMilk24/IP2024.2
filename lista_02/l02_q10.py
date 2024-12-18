quantidade = int(input())
condicao = True

tamanho_item = 0
total_chutes = 0
print('Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!')
print('Quantos materiais mágicos estão trancados nos baús?')
print('Vamos começar desbloqueando os materiais!')
for x in range(1,quantidade+1):
    item = input()
    tamanho_item = len(item)
    print(tamanho_item)
    if(tamanho_item <= 5):
        total_chutes = 7
    elif(tamanho_item > 5 and tamanho_item <= 10):
        total_chutes = 9
    elif(tamanho_item > 10 and tamanho_item <=13):
        total_chutes = 13
    else:
        total_chutes = 16

    print('Material {} de {}'.format(x, quantidade))
    item_cifrado = ''

    for x in item:
        if(x == ' '):
            item_cifrado += x
        else:
            item_cifrado += '_'
    print('Senha mágica: {}'.format(item_cifrado))

    while(condicao):
        letra = input()
        if letra in item:
            tamanho_item -= item.count(letra)
            print('Acertamos uma letra! Ela aparece um total de {} vezes na senha'.format(item.count(letra)))
            if(tamanho_item == 0):
                print('Parabéns! Você desbloqueou o material mágico \'{}\'!'.format(item))
                condicao = False
                break
        else:
            print('Erramos a letra! Porém ainda temos mais tentativas.')
        total_chutes -= 1

        if(total_chutes == 0):
            condicao = False
            break