nome, vida, distancia, velocidade, defesa = input().split(' - ')

vida = int(vida)
distancia = int(distancia)
velocidade = int(velocidade)
defesa = int(defesa)

inimigo = [nome, vida, distancia, velocidade, defesa]

def use_zap(inimigo):
    
    if inimigo[4] == 1:
        inimigo[3] -= 1
    elif inimigo[4] == 0:
        inimigo[1] -= 5
        inimigo[3] -= 1 
               
    return inimigo

def use_powpow(inimigo):
    if inimigo[4] == 0:
        inimigo[1] -= 15
        
    return inimigo

def use_fishbones(inimigo):
    if inimigo[4] == 1:
        inimigo[4] = 0 
    elif inimigo[4] == 0:
        inimigo[1] -= 30
        
    return inimigo

def use_ultimate(inimigo):
    if inimigo[4] == 0:
        inimigo[1] -= 100
        
    return inimigo

def calcula_distancia(inimigo):
    inimigo[2] -= inimigo[3]
    
    return inimigo

def verifica_distancia(inimigo):
    if inimigo[2] >= 1:
        return True
    else:
        return False

    