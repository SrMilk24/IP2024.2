nome, vida, distancia, velocidade, defesa = input().split(' - ')

vida = int(vida)
distancia = int(distancia)
velocidade = int(velocidade)
defesa = int(defesa)

inimigo = [nome, vida, distancia, velocidade, defesa]

def use_zap(inimigo):
    
    if inimigo[4] == 1:
        print("Ele está com defesa e está muito perto!")
    else:
        inimigo[1] -= 5
        print("Você foi zapeado hahaha.")
        
    inimigo[3] = max(1, inimigo[3] - 1)
    return inimigo
               

def use_powpow(inimigo):
    if inimigo[4] == 1:
        print("Ele está com defesa e está muito perto!")
    else:
        inimigo[1] -= 15
        print("Jinx vai encher esse cara de buracos agora.")
    return inimigo

def use_fishbones(inimigo):
    if inimigo[4] == 1:
        inimigo[4] = 0 
        print("A defesa dele foi destruída com o poder da Fishbones!")
    elif inimigo[4] == 0:
        inimigo[1] -= 30
        print("Vamos derretê-lo com a Fishbones!")
        
    return inimigo

def use_ultimate(inimigo):
    if inimigo[4] == 1:
        print("Ele está com defesa e está muito perto!")
    else:
        inimigo[1] -= 100
        print("Ele vai ser transformado em cinzas pelo SUPER MÍSSIL!")
    return inimigo

def aproximar(inimigo):
    inimigo[2] = max(0, inimigo[2] - inimigo[3])
    
    return inimigo

def jinx_pega(inimigo):
    if inimigo[2] >= 1:
        return False
    else:
        return True
    
resultado_captura = ''
ultimate_status = False
print(f"Andando pelas ruas de Zaun, jinx dá de cara com um {nome} e agora vão lutar.")

while resultado_captura != "finalizada":
    status_captura = jinx_pega(inimigo)

    if status_captura:
        print("Ah não, A Jinx foi PEGA!")
        resultado_captura = "finalizada"
        break
    
    if inimigo[1] <= 0:
        print("Ninguem é capaz de derrotar a Jinx!!!")
        resultado_captura = "finalizada"
        break

    #Movimentos possíveis da jinx
    if inimigo[4] == 1:
        if inimigo[2] >= 30:
            use_fishbones(inimigo)
        else:
            use_zap(inimigo)
    else:
        if inimigo[2] >= 50 and not ultimate_status:
            use_ultimate(inimigo)
            ultimate_status = True
        elif inimigo[2] >= 30:
            use_fishbones(inimigo)
        elif inimigo[2] >= 15:
            use_powpow(inimigo)
        else:
            use_zap(inimigo)

    aproximar(inimigo)
