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

while num_batalhas <= 3:
    estado_atacante = input()
    armas_atacante = []

    quantia_ouro = int(input())
    quantidade_soldados = int(input())

    while len(armas_atacante) < 3:
        arma = input()

        if verificar_arma(armas, arma):
            armas_atacante.append(arma)
        else:
            print("@ selecione uma arma válida! @")

    # Verifico se estado atacante é da aliança ou da coroa, para subtrair o ouro e tropas enviado pra batalha
    if verifica_estado(estados_alianca, estado_atacante):

        subtrai_ouro(estados_alianca, quantia_ouro) # Subtraio o ouro da aliança
        subtrai_soldados(estados_alianca, quantidade_soldados) # Subtraio os soldados da aliança

        if estado_com_vantagem(estado_atacante):
            print(f"o estado de {estado_atacante} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!")
        # Nesse if acima, devo chamar a função que calcula o poder do atacante e por esse if dentro dela


        # Aqui começo a tratar do defensor, se o atacante é da aliança, o defensor deve ser da coroa
        estado_defensor = input()

        if verifica_estado(estados_coroa, estado_defensor): #Verifico se o defensor é da coroa
            armas_defensor = []

            quantia_ouro = int(input())
            quantidade_soldados = int(input())

            while len(armas_defensor) < 3:
                arma = input()

                if verificar_arma(armas, arma):
                    armas_defensor.append(arma)
                else:
                    print("@ selecione uma arma válida! @")
            subtrai_ouro(estados_coroa, quantia_ouro)
            subtrai_soldados(estados_coroa, quantidade_soldados)

            # Aqui eu devo calculo o valor da força desse estado

        else:
            print("@ escolha um estado válido para contra-atacar! @")

    elif verifica_estado(estados_coroa, estado_atacante):
        subtrai_ouro(estados_coroa, quantia_ouro)
        subtrai_soldados(estados_coroa, quantidade_soldados) 
    else:
        print("@ estado não encontrado ou não faz parte das regiões em guerra! @")