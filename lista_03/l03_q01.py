viloes = []
validador = ""

while(validador != "Ja temos nossa lista de suspeitos"):
    entrada = input()

    if(entrada == "Novo vilão - Muito Perigoso"):
        vilao = input()
        viloes.append(vilao)
    elif(entrada == "Novo vilão - Meio perigoso"):
        vilao = input()
        viloes.insert(0, vilao)
    elif(entrada == "O que ele está fazendo aqui?"):
        viloes.remove(vilao)
    elif(entrada == "Vilão mais perigoso do que pensávamos"):
        indice_atual = int(input())
        indice_novo = int(input())
        aux = viloes[indice_novo]
        viloes[indice_novo] = viloes[indice_atual]
        viloes[indice_atual] = aux
