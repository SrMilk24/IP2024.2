quant_folhas = int(input())
populacao = int(input())
altura = int(input())

folhas_pessoa = quant_folhas / populacao

if(folhas_pessoa < 6):
    print('Isso não é uma árvore, é um arbusto!')
else:
    #formula -> h = (-1 + raiz(1+8x))/2

    