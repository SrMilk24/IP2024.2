def registrar_conexoes(n):
    conexoes = []
    for i in range(n):
        entrada = input().strip()
        partes = entrada.split(", ")
        conexao = [None, None]
        for parte in partes:
            bit, estado = parte.split(" - ")
            conexao[int(bit)] = estado
        conexoes.append(conexao)
    return conexoes

def imprimir_conexoes(conexoes):
    for i in range(len(conexoes)):
        conexao = conexoes[i]
        print(f"q{i+1}: {{0 -> {conexao[0]}, 1 -> {conexao[1]}}}")

def processar_cadeia(cadeia, estado_inicial, conexoes, estado_aceitacao):
    caminho = [estado_inicial]
    estado_atual = estado_inicial

    if cadeia == "ε" or cadeia == "": 
        if estado_atual == estado_aceitacao:
            print("Caramba, essa cadeia é abençoada! Nem precisei trabalhar!")
        else:
            print("Nossa, que maldição! Nem começou e já deu errado…")
        return caminho

    for bit in cadeia:
        if bit not in {'0', '1'}:
            print(f"Só pode estar de brincadeira comigo! Como vou lidar com {bit} dentro da máquina?")
            caminho.append("ERROR")
            return caminho

        bit = int(bit)
        proximo_estado = conexoes[int(estado_atual[1:]) - 1][bit]

        if proximo_estado != estado_atual:
            caminho.append(proximo_estado)
        estado_atual = proximo_estado

    if estado_atual == estado_aceitacao:
        print("Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!")
    else:
        print("Que tristeza, todo esse arrudeio pra nada…")

    return caminho



n = int(input())
if n == 1:
    print("É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(")
else:
    estado_aceitacao = input().strip()
    conexoes = registrar_conexoes(n)
    imprimir_conexoes(conexoes)

    m = int(input()) 

    cadeias_aceitas = 0

    for _ in range(m):
        cadeia = input().strip() 
        estado_inicial = input().strip()
        caminho = processar_cadeia(cadeia, estado_inicial, conexoes, estado_aceitacao)
        caminho_formatado = " -> ".join(caminho)
        print(f"{{{caminho_formatado}}}")

        if caminho[-1] == estado_aceitacao:
            cadeias_aceitas += 1

    precisao = (cadeias_aceitas / m) * 100

    if precisao == 100:
        print("Sensacional :)! Com certeza vamos voltar pra casa com esse autômato, até Alan Turing teria inveja!")
    elif precisao >= 75:
        print("Show de bola! Se fizermos alguns ajustes nesse autômato, temos muitas chances de voltar pra casa!")
    elif precisao >= 50:
        print("Até que esse autômato da pro gasto, mas vamos precisar de uns bons ajustes…")
    elif precisao >= 25:
        print("Nossa, que situação horrível, não faço a mínima ideia de como concertar esse autômato")
    else:
        print("Nossas expectativas já eram baixas, mas não sabia que seria tão catastrófico assim :/")