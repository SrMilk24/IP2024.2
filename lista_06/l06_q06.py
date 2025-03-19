estados_alianca = ('PE', 'PB', 'RN', 'CE', 'AL', 'BA')
anexados_alianca = []
estados_coroa = ('SP', 'RJ', 'ES', 'MG', 'PR', 'RS')
anexados_coroa = []

alianca = {
    'estados': estados_alianca,
    'pontos_vida': 1000,
    'riqueza': 20000,
    'quantidade_soldados': 10000,
    'quantidade_vitorias': 0,
    'quantidade_derrotas': 1,
    'estados_anexados': anexados_alianca
}

coroa = {
    'estados': estados_coroa,
    'pontos_vida': 1000,
    'riqueza': 20000,
    'quantidade_soldados': 10000,
    'quantidade_vitorias': 0,
    'quantidade_derrotas': 1,
    'estados_anexados': anexados_coroa
}

armas = {
    'Mosquete': 7000,
    'Baioneta': 3000,
    'Canhão': 10000,
    'Espada': 3500,
    'Pederneira': 5000
}

def calcula_pontuacao(dict_armas, ouro, soldados, armas_estado):
    dano_armas = 0
    for arma in armas_estado:
        dano_armas += dict_armas[arma]
        
    forca = ((ouro*2) + (soldados * 4) + (dano_armas * 4)) / 10

    return forca

def verifica_estado(lista_estados, estado):
    return estado in lista_estados

def verificar_arma(armas, arma):
    if arma in armas:
        return True
    else:
        print("@ selecione uma arma válida! @")
        return False

def estado_com_vantagem(estado):
    if estado == 'PE' or estado == 'PB' or estado == 'RN':
        return True
    else:
        return False
    
def subtrai_ouro(lista_estados, ouro):
    lista_estados['riqueza'] -= ouro
    return None

def subtrai_soldados(lista_estados, soldados):
    lista_estados['quantidade_soldados'] -= soldados
    return None

num_batalhas = 1

def add_armas(armas_possiveis):
    armas_estado = []
    while len(armas_estado) < 3:
        arma = input()
        if verificar_arma(armas_possiveis, arma):
            armas_estado.append(arma)
    return armas_estado

while num_batalhas < 4:
    atacante = input()

    if (atacante not in estados_alianca) and (atacante not in estados_coroa):
        print("@ estado não encontrado ou não faz parte das regiões em guerra! @")
    ouro_atacante = int(input())
    soldados_atacante = int(input())
    armas_atacante = add_armas(armas)
    forca_atacante = calcula_pontuacao(armas, ouro_atacante, soldados_atacante, armas_atacante)
 
    if estado_com_vantagem(atacante):
        print(f"o estado de {atacante} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!")
        forca_atacante *= 1.1
    

    defensor = input()
    while ((atacante in estados_alianca) and (defensor not in estados_coroa)) or ((atacante in estados_coroa) and (defensor not in estados_alianca)):
        print("@ escolha um estado válido para contra-atacar! @")
        defensor = input()

    ouro_defensor = int(input())
    soldados_defensor = int(input())
    armas_defendor = add_armas(armas)

    forca_defensor = calcula_pontuacao(armas, ouro_defensor, soldados_defensor, armas_defendor)

    if forca_atacante > forca_defensor:
        print(f"o estado de {atacante} acaba de consagrar mais uma vitória e derrotou o estado de {defensor} e agora o anexará!")
    else:
        print(f"o estado de {defensor} acaba de consagrar mais uma vitória e derrotou o estado de {atacante} e agora o anexará!")


    print(f"=== resultado da {num_batalhas}º batalha ===")


    num_batalhas += 1
