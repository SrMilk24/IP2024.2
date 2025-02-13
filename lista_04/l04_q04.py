alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def descriptografar(palavra_cifrada, deslocamento):
    cifra_to_list = list(palavra_cifrada)
    for letra in range(len(cifra_to_list)):
        index_atual = alfabeto.index(cifra_to_list[letra])
        novo_index = (index_atual - deslocamento) % 26
        cifra_to_list[letra] = alfabeto[novo_index]

    return ''.join(cifra_to_list)

def calcular_dano(precisao, poder, resistencia, fator):
    dano = precisao * (poder / resistencia)

    if fator == "ALTO":
        dano *= 2
    elif fator == "MEDIO":
        dano *= 1.5
    elif fator == "BAIXO":
        dano *= 1
    return round(dano)

def resultado(danos):

    for dano, nome_alvo, formula in danos:
        print(f"Decifrando: {formula}")
        print(f"{nome_alvo}: {dano} de dano calculado.")
        if dano >= 100:
            print(f"{nome_alvo} será destruído!")
        else:
            print(f"{nome_alvo} resistirá ao ataque.")
        print()
        
    danos.sort(key=lambda item: item[0], reverse=True)

    print("Prioridade de ataques:")
    for dano, nome_alvo, _ in danos:
        print(f"{nome_alvo} - {dano} de dano")

ataques = int(input())



if ataques == 0:
    print("Piltover em paz... por enquanto.")
else:
    danos = []
    for x in range(ataques):
        nome_alvo, precisao, resistencia, poder, menssagem_cifrada, deslocamento = input().split(", ")
    
        precisao = int(precisao)
        resistencia = int(resistencia)
        poder = int(poder)
        deslocamento = int(deslocamento)

        descriptografia = descriptografar(menssagem_cifrada, deslocamento)
        dano = calcular_dano(precisao, poder, resistencia, descriptografia)
        danos.append([dano, nome_alvo, descriptografia])
    resultado(danos)