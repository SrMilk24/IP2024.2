quant_folhas = int(input())
populacao = int(input())
altura = int(input())

folhas_necessarias = 0


folhas_pessoa = quant_folhas / populacao

if(altura < 2):
    print('Isso não é uma árvore, é um arbusto!')
else:
 
    folhas_arvore = folhas_pessoa / 2
    
    for x in range(1, altura+1):
        folhas_necessarias += x*2
        
    if(folhas_necessarias > quant_folhas):
        print('Infelizmente não poderemos comemorar o Natal esse ano, não conseguimos fazer uma única árvore!')
    else:
        print('{}'.format('⠀'*(altura+1)), end='')
        print('*')
        for x in range(altura):
            print('{}'.format('⠀' * (altura - x)), end='')
            print('{}'.format('+'*(x+1)), end='⠀')
            print('{}'.format('+'* (x+1)))
            
    arvores_populacao = populacao * folhas_necessarias

    if(quant_folhas >= arvores_populacao):
        print('O Grinch não conseguiu estragar o Natal dessa vez!')
    else:
        print('Essa árvore está muito grande, dessa forma não conseguiremos entregar para a cidade toda')
    

