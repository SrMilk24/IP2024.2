personalidades = {
    "Zumbi dos Palmares": {"legado": 1000, "ramo": "Revolucionário", "impacto": 0},
    "Frei Caneca": {"legado": 900, "ramo": "Revolucionário", "impacto": 0},
    "Paulo Freire": {"legado": 800, "ramo": "Educador", "impacto": 0},
    "Clarice Lispector": {"legado": 800, "ramo": "Escritor", "impacto": 0},
    "Ariano Suassuna": {"legado": 700, "ramo": "Escritor", "impacto": 0},
    "Chico Science": {"legado": 600, "ramo": "Artista", "impacto": 0},
    "Luiz Gonzaga": {"legado": 500, "ramo": "Artista", "impacto": 0},
    "Eduardo Campos": {"legado": 400, "ramo": "Político", "impacto": 0},
    "Rivaldo": {"legado": 300, "ramo": "Atleta", "impacto": 0},
    "Lia de Itamaracá": {"legado": 200, "ramo": "Artista", "impacto": 0}
}

ordem_relevancia = {
    "Revolucionário": 1,
    "Líder comunitário": 2,
    "Cientista": 3,
    "Político": 4,
    "Escritor": 5,
    "Educador": 6,
    "Artista": 7,
    "Atleta": 8
}

def set_pontos_bairro(personalidades, personalidade, populacao, ordem):
    pontos = populacao // ordem
    personalidades[personalidade]['impacto'] += pontos

def set_categoria(personalidades, personalidade, categoria):
    personalidades[personalidade]['ramo'] = categoria

def popularidade_bairro(personalidades, n):
    for _ in range(n):
        bairro = input()
        populacao = int(input())
        for x in range(1, 4):
            figura = input().split("-")
            figura_nome = figura[0].strip()
            figura_ramo = figura[1].strip()
            set_pontos_bairro(personalidades, figura_nome, populacao, x)
            set_categoria(personalidades, figura_nome, figura_ramo)

def calcular_vencedor(personalidades):

    personalidades_ordem = sorted(personalidades.items(), key=lambda item: (item[1]['impacto'] + item[1]['legado'], ordem_relevancia[item[1]['ramo']]), reverse=True)
    figura_1 = personalidades_ordem[0]
    figura_2 = personalidades_ordem[1]

    if figura_1[1]['impacto'] + figura_1[1]['legado'] == figura_2[1]['impacto'] + figura_2[1]['legado']:
        print(f"Temos um empate entre {figura_1[0]} e {figura_2[0]}, vamos usar os critérios de desempate para ver quem fica com o prêmio.")
        
        if ordem_relevancia[figura_1[1]['ramo']] < ordem_relevancia[figura_2[1]['ramo']]:
            vencedor = figura_1
            perdedor = figura_2
        else:
            vencedor = figura_2
            perdedor = figura_1
        
        print(f"Após utilizar os critérios de desempate, {vencedor[0]} ficou com o prêmio.")
    else:
        vencedor = figura_1
        perdedor = figura_2

    print(f"1º: {vencedor[0]} com {vencedor[1]['legado']} pontos de legado, {vencedor[1]['impacto']} pontos de impacto e {vencedor[1]['impacto'] + vencedor[1]['legado']} pontos totais")
    print(f"2º: {perdedor[0]} com {perdedor[1]['legado']} pontos de legado, {perdedor[1]['impacto']} pontos de impacto e {perdedor[1]['impacto'] + perdedor[1]['legado']} pontos totais")

n = int(input())
popularidade_bairro(personalidades, n)
calcular_vencedor(personalidades)
