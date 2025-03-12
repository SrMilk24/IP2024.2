dicionario = {
    "cidade" : {
        "lider": "nome lider",
        "batalha": "nome batalha",
        "participantes": 0
    },
    "cidade2" : {
        "lider": "nome lider",
        "batalha": "nome batalha",
        "participantes": 0
    },
    
}

def verificar_cidade(cidades, cidade):
    return cidade in cidades


def adicionar_cidade(cidades, cidade, dados):
    novos_dados = dados.split(", ")
    if verificar_cidade(cidades, cidade):
        print(f"Atualizando a cidade {cidade}...")
        print(f"Dados atualizados para {cidade}.")
        cidades[cidade]["lider"] = novos_dados[0]
        cidades[cidade]["batalha"] = novos_dados[1]
        cidades[cidade]["participantes"] = novos_dados[2]
    else:
        print(f"Dados adicionados para {cidade}.")
        cidades[cidade] = {
            "lider": novos_dados[0],
            "batalha": novos_dados[1],
            "participantes": novos_dados[2]
        }
    return cidades

def remover_cidade(cidades, cidade):
    if verificar_cidade(cidades, cidade):
        print(f"Dados removidos para a cidade {cidade}.")
        cidades.pop(cidade)
    else:
        print(f"Nenhum dado encontrado para a cidade {cidade}.")

    return cidades

def calcula_total(cidades):
    participantes = 0
    for cidade in cidades:
        participantes += int(cidades[cidade]['participantes'])

    return participantes
# Ler a ação

cidades = {}
entrada = ""
while entrada != "FIM":
    cidade = input()
    

    if cidade == "FIM":
        entrada = "FIM"
    else:
        acao = input()
        if acao == "adicionar":
            dados = input()
            adicionar_cidade(cidades, cidade, dados)
        elif acao == "deletar":
            remover_cidade(cidades, cidade)
        else:
            print("Comando inválido! Digite 'adicionar' ou 'deletar'.")
print("RESUMO DAS CONTRIBUIÇÕES DA REVOLUÇÃO PERNAMBUCANA")
print("--------------------------------------------------")
total_participantes = calcula_total(cidades)

for cidade in cidades:
    print(f"{cidade}: O(a) líder {cidades[cidade]['lider']} liderou a {cidades[cidade]['batalha']} com {((float(cidades[cidade]['participantes']))/total_participantes)*100:.2f}% dos revolucionários registrados.")
