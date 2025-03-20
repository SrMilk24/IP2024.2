estados_alianca = ['PE', 'PB', 'RN', 'CE', 'AL', 'BA']
anexados_alianca = []
estados_coroa = ['SP', 'RJ', 'ES', 'MG', 'PR', 'RS']
anexados_coroa = []

alianca = {
    'estados': estados_alianca,
    'pontos_vida': 1000.0,
    'riqueza': 20000,
    'quantidade_soldados': 10000,
    'quantidade_vitorias': 0,
    'quantidade_derrotas': 0,
    'estados_anexados': anexados_alianca
}

coroa = {
    'estados': estados_coroa,
    'pontos_vida': 1000.0,
    'riqueza': 20000,
    'quantidade_soldados': 10000,
    'quantidade_vitorias': 0,
    'quantidade_derrotas': 0,
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
        
    forca = ((ouro * 2) + (soldados * 4) + (dano_armas * 4)) / 10
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
    return estado in ['PE', 'PB', 'RN']

def subtrai_ouro(lista_estados, ouro):
    lista_estados['riqueza'] -= ouro

def subtrai_soldados(lista_estados, soldados):
    lista_estados['quantidade_soldados'] -= soldados

def add_armas(armas_possiveis):
    armas_estado = []
    while len(armas_estado) < 3:
        arma = input()
        if verificar_arma(armas_possiveis, arma):
            armas_estado.append(arma)
    return armas_estado

def anexa_estado(lista_anexar, estado):
    lista_anexar.append(estado)

def reintegra_estado(bloco_vencedor, bloco_perdedor):
    if bloco_perdedor['estados_anexados']:
        estado_reintegrado = bloco_perdedor['estados_anexados'].pop()
        bloco_vencedor['estados'].append(estado_reintegrado)

def processar_vitoria(vencedor, perdedor, estados_alianca, anexados_alianca, anexados_coroa, alianca, coroa, forca_vencedor, forca_perdedor):
    print(f"o estado de {vencedor} acaba de consagrar mais uma vitória e derrotou o estado de {perdedor} e agora o anexará!")

    if vencedor in estados_alianca:
        anexa_estado(anexados_alianca, perdedor)
        reintegra_estado(alianca, coroa)
        alianca['quantidade_vitorias'] += 1
        coroa['quantidade_derrotas'] += 1
        dano = coroa['pontos_vida'] * (1 - (forca_perdedor / forca_vencedor))
        coroa['pontos_vida'] = round(coroa['pontos_vida'] - dano, 2)  # Arredonda para 2 casas decimais
        return ["aliança", perdedor]
    else:
        anexa_estado(anexados_coroa, perdedor)
        reintegra_estado(coroa, alianca)
        coroa['quantidade_vitorias'] += 1
        alianca['quantidade_derrotas'] += 1
        dano = alianca['pontos_vida'] * (1 - (forca_perdedor / forca_vencedor))
        alianca['pontos_vida'] = round(alianca['pontos_vida'] - dano, 2)  # Arredonda para 2 casas decimais
        return ["coroa", perdedor]

num_batalhas = 1

while num_batalhas < 4:
    atacante = input()

    if (atacante not in estados_alianca) and (atacante not in estados_coroa):
        print("@ estado não encontrado ou não faz parte das regiões em guerra! @")
        continue

    ouro_atacante = int(input())
    soldados_atacante = int(input())
    armas_atacante = add_armas(armas)
    forca_atacante = calcula_pontuacao(armas, ouro_atacante, soldados_atacante, armas_atacante)
    
    defensor = input()
    while ((atacante in estados_alianca) and (defensor not in estados_coroa)) or ((atacante in estados_coroa) and (defensor not in estados_alianca)):
        print("@ escolha um estado válido para contra-atacar! @")
        defensor = input()

    ouro_defensor = int(input())
    soldados_defensor = int(input())
    armas_defensor = add_armas(armas)
    forca_defensor = calcula_pontuacao(armas, ouro_defensor, soldados_defensor, armas_defensor)

    if atacante in estados_alianca:
        subtrai_ouro(alianca, ouro_atacante)
        subtrai_soldados(alianca, soldados_atacante)
        subtrai_ouro(coroa, ouro_defensor)
        subtrai_soldados(coroa, soldados_defensor)
    else:
        subtrai_ouro(coroa, ouro_atacante)
        subtrai_soldados(coroa, soldados_atacante)
        subtrai_ouro(alianca, ouro_defensor)
        subtrai_soldados(alianca, soldados_defensor)
    
    if estado_com_vantagem(atacante):
        print(f"o estado de {atacante} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!")
        forca_atacante *= 1.1
    
    if forca_atacante > forca_defensor:
        vitorioso = processar_vitoria(atacante, defensor, estados_alianca, anexados_alianca, anexados_coroa, alianca, coroa, forca_atacante, forca_defensor)
    elif forca_atacante < forca_defensor:
        vitorioso = processar_vitoria(defensor, atacante, estados_alianca, anexados_alianca, anexados_coroa, alianca, coroa, forca_defensor, forca_atacante)
    else:
        print("na batalha desta rodada houve um empate!!!")
        vitorioso = None

    if alianca['riqueza'] <= 0 or alianca['quantidade_soldados'] <= 0 or coroa['riqueza'] <= 0 or coroa['quantidade_soldados'] <= 0:
        if alianca['riqueza'] <= 0 or alianca['quantidade_soldados'] <= 0:
            print("a aliança não possui recursos suficientes para continuar com a guerra! O vencedor será aquele que tiver o maior ponto de vida")
        else:
            print("a coroa não possui recursos suficientes para continuar com a guerra! O vencedor será aquele que tiver o maior ponto de vida")
        num_batalhas = 4
    else:
        print(f"=== resultado da {num_batalhas}º batalha ===")
        print()

        print(f"número de estados da aliança: {len(estados_alianca)-len(anexados_coroa)}")
        print(f"vitórias: {alianca['quantidade_vitorias']}")
        print(f"derrotas: {alianca['quantidade_derrotas']}")
        print(f"riqueza: {alianca['riqueza']:.1f}")
        print(f"nº soldados: {alianca['quantidade_soldados']}")
        print(f"pontos de vida: {alianca['pontos_vida']:.2f}")

        print()
        print(f"número de estados da coroa: {len(estados_coroa)-len(anexados_alianca)}")
        print(f"vitórias: {coroa['quantidade_vitorias']}")
        print(f"derrotas: {coroa['quantidade_derrotas']}")
        print(f"riqueza: {coroa['riqueza']:.1f}")
        print(f"nº soldados: {coroa['quantidade_soldados']}")
        print(f"pontos de vida: {coroa['pontos_vida']:.2f}")

        print()
        if vitorioso:
            if vitorioso[0] == "aliança":
                print(f"a alianca anexou o(s) seguinte(s) estado(s): {','.join(anexados_alianca)}")
            else:
                print(f"a coroa anexou o(s) seguinte(s) estado(s): {','.join(anexados_coroa)}")


        num_batalhas += 1

if alianca['pontos_vida'] > coroa['pontos_vida']:
    print("VIVA! A Revolução vingou, Pernambuco se uniu aos outros estados do Nordeste e ao Estado de Minas Gerais e criou a república Pernambucana!")
elif alianca['pontos_vida'] < coroa['pontos_vida']:
    print("infelizmente o sonho acabou! A revolução falhou o império Português venceu!")
else:
    print("a guerra foi em vão! As coisas ficarão como estão!")