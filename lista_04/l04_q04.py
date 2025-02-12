alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#nome_alvo = input()
#precisao = int(input())
#resistencia = int(input())
#poder = int(input())
menssagem_cifrada = input()
deslocamento = int(input())



def descriptografar(palavra_cifrada, deslocamento):
    cifra_to_list = list(palavra_cifrada)
    for letra in range(len(cifra_to_list)):
        index_atual = alfabeto.index(cifra_to_list[letra])
        novo_index = (index_atual - deslocamento) % 26
        cifra_to_list[letra] = alfabeto[novo_index]

    print(f"Decifrando: {''.join(cifra_to_list)}")

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
    danos.sort(key=lambda item: item[0])
    for x in len(danos):
        print(f"{danos[x][1]}: {danos[x][0]} de dano calculado.")
        if danos[x][0] >= 100:
            print(f"{danos[x][1]} será destruído!")
        else:
            print(f"{danos[x][1]} resistirá ao ataque.")
        
descriptografia = descriptografar(menssagem_cifrada, deslocamento)
