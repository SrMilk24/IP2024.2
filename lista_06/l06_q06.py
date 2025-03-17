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

def verifica_estado(lista_estados, estado):
    return estado in lista_estados

def verificar_arma(armas, arma):
    return arma in armas

def calcular_forca(dic_armas, ouro, soldados, armas, estado):
    letalidade_armas = 0
    
    for arma in armas:
        letalidade_armas += dic_armas.get(arma)
    forca = ((ouro * 2) + (soldados * 4) + (letalidade_armas * 4)) / 10

    if estado == 'PE' or estado == 'PB' or estado == 'RN':
        forca *= 1.1
        print(f"o estado de {estado} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!")
    return forca

def calcular_dano_batalha(estado_atacante, ouro_atacante, soldados_atacante, armas_atacante, estado_defensor, ouro_defensor, soldados_defensor, armas_defensor):
    if verifica_estado(estado_atacante not in estados_alianca) and verifica_estado(estado_atacante not in estados_coroa):
        print("@ estado não encontrado ou não faz parte das regiões em guerra! @")
