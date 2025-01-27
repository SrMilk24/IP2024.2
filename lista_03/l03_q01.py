viloes = []

validador = ""

while(validador != "Já temos nossa lista de vilões"):
    entrada = input()

    if(entrada == "Novo vilão - Muito Perigoso"):
        
        vilao = input()
        
        aux_lista = viloes #Crio uma lista auxiliar que é igual a lista de vilões
        viloes = [] #Zero a lista de vilões
        viloes.append(vilao) #Adiciono o novo vilão a lista original, que ficara na primeira posição
        
        #No for abaixo, apenas readiciono a lista os vilões da lista inicial
        for x in aux_lista:
            viloes.append(x)
        
    elif(entrada == "Novo vilão - Meio perigoso"):
        vilao = input()
        viloes.append(vilao)
    elif(entrada == "O que ele está fazendo aqui?"):
        vilao = input()
        aux_lista = []
        # Usando uma lista auxiliar, percoro a lista original, e adiciono na nova lista todos os vilões, menos o informado para ser removido
        for x in viloes:
            if x != vilao:
                aux_lista.append(x)
                
        viloes = aux_lista
    elif(entrada == "Vilão mais perigoso do que pensávamos"):
        indice_atual = int(input())
        indice_novo = int(input())
        aux = viloes[indice_novo]
        viloes[indice_novo] = viloes[indice_atual]
        viloes[indice_atual] = aux
    elif(entrada == "Que estranho, esses dois vilões… troque-os de lugar"):
        vilao_1 = input()
        vilao_2 = input()
        for x in range(len(viloes)):
            if(viloes[x] == vilao_1):
                viloes[x] = vilao_2
            elif(viloes[x] == vilao_2):
                viloes[x] = vilao_1
    elif(entrada == "Essa posição não está de acordo, ele nem odeia carecas"):
        vilao = input()
        aux_lista = []
        for x in viloes:
            if x != vilao:
                aux_lista.append(x)
        aux_lista.append(vilao)
        viloes = aux_lista
    elif(entrada == "Como a lista está ficando?"):
        for x in range(len(viloes)):
            if (x != len(viloes) - 1):
                print(viloes[x], end=', ')
            else:
                print(viloes[x])
    elif(entrada == "Já temos nossa lista de vilões"):
        print("O resultado final ficou assim:")
        for x in range(len(viloes)):
            if (x != len(viloes) - 1):
                print(f"{viloes[x]}", end=', ')
            else:
                
                print(viloes[x])
        validador = "Já temos nossa lista de vilões"