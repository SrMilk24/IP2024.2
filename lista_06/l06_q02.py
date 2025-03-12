def pontua_status(status):
    if status == "APROVA":
        return 5
    elif status == "TANTO FAZ":
        return 2
    elif status == "DESAPROVA":
        return 0

def pontua_orcamento(orcamento):
    if orcamento > 1000000:
        return 3
    elif orcamento >= 500000 and orcamento <= 1000000:
        return 4
    elif orcamento < 500000:
        return 5
    else:
        return 0

def pontua_objetivo(objetivo):
    if objetivo == "Defesa":
        return 5
    elif objetivo == "Ciencia":
        return 4
    elif objetivo == "Lazer":
        return 3
    else:
        return 0
    

def adicionar_obra(obras, obra, status, orcamento, objetivo):

    pontuacao = 0
    pontuacao += pontua_status(status)
    pontuacao += pontua_orcamento(orcamento)
    pontuacao += pontua_objetivo(objetivo)

    obras[obra] = {
        "status": status,
        "orcamento": orcamento,
        "objetivo": objetivo,
        "pontuacao" : pontuacao
    }

    return obras

obras = {}

for x in range(3):
    obra = input()
    status = input()
    orcamento = int(input())
    objetivo = input()

    adicionar_obra(obras, obra, status, orcamento, objetivo)

obras_ordenadas = dict(sorted(obras.items(), key=lambda item: (-item[1]['pontuacao'], item[1]['orcamento'])))

x = 1
print("")
for obra in obras_ordenadas:
    if x == 1:
        print(f"O primeiro estabelecimento construído deve ser {obra}, com um orçamento de {obras_ordenadas[obra]['orcamento']} e com a funcionalidade de {obras_ordenadas[obra]['objetivo']}.")
        x += 1
    elif x == 2:
        print(f"O segundo estabelecimento construído deve ser {obra}, com um orçamento de {obras_ordenadas[obra]['orcamento']} e com a funcionalidade de {obras_ordenadas[obra]['objetivo']}.")
        x += 1    
    elif x == 3:
        print(f"O terceiro estabelecimento construído deve ser {obra}, com um orçamento de {obras_ordenadas[obra]['orcamento']} e com a funcionalidade de {obras_ordenadas[obra]['objetivo']}.")
    
for obra in obras_ordenadas:
    if obras_ordenadas[obra]['objetivo'] == "Defesa":
        print("Oba, agora a cidade estará mais segura.")
    elif obras_ordenadas[obra]['objetivo'] == "Ciencia":
        print("Agora sim vou poder ter uma vida intelectual.")
    elif obras_ordenadas[obra]['objetivo'] == "Lazer":
        print("Vamooo, agora posso curtir meu final de semana descansando na bela cidade do Recife.")
