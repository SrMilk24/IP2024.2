def busca_palavra(tabela, palavra, linha, coluna, posicao_atual, direcao):

    if posicao_atual == len(palavra):
        return True
    
    if linha < 0 or linha >= len(tabela) or coluna < 0 or coluna >= len(tabela[0]) or tabela[linha][coluna] != palavra[posicao_atual]:
        return False
    
    temp = tabela[linha][coluna]
    tabela[linha][coluna] = '#'

    for mov_linha, mov_coluna in direcao:

        if busca_palavra(tabela, palavra, linha + mov_linha, coluna + mov_coluna, posicao_atual + 1, direcao):
            tabela[linha][coluna] = temp
            return True
        
    tabela[linha][coluna] = temp
    return False

def encontrar_lugar(matriz, lugares):
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for lugar in lugares:
        palavra = lugar.replace(" ", "").upper()
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if busca_palavra(matriz, palavra, i, j, 0, direcoes):
                    return lugar
    return None

entrada = int(input())
tabela = [input().split() for _ in range(entrada)]
lugares = ["Penguin Bar", "Praia Gelada", "PenguiCup Stadium", "Delegacia Polar", "SubzeroWay", "Frio de Janeiro"]
lugar_encontrado = encontrar_lugar(tabela, lugares)

if lugar_encontrado == "Delegacia Polar":
    print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
elif lugar_encontrado == "Frio de Janeiro":
    print("ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
elif lugar_encontrado:
    print(f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {lugar_encontrado}. Vamos salvar nosso Carnaval de Inverno!")
else:
    print("Nosso carnaval de inverno está perdido... NÃOOOOO")