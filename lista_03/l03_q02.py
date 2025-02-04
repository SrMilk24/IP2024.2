entrada = input()
nomes = []
for x in entrada.split("-"):
    nomes.append(x)

validador = ""
nomes_trocados = []

while validador != "Acabou!":
    troca = input()
    if troca == "Acabou!":
        validador = "Acabou!"
    else:
        troca_separada = troca.split("-")
        if troca_separada[0] not in nomes or troca_separada[1] not in nomes:
            print("Essa dupla não esta na lista!")
        else:
            nome_1 = nomes.index(troca_separada[0])
            nome_2 = nomes.index(troca_separada[1])

            nomes[nome_1] = troca_separada[1]
            nomes[nome_2] = troca_separada[0]
            for x in troca_separada:
                nomes_trocados.append(x)
            
print("Fila do almoço:")
for nome in nomes:
    count = nomes_trocados.count(nome)
    if count > 1:
        print(f"{nome}: {count} teleportes!")
    elif count <= 1:
        print(f"{nome}: {count} teleporte!")
