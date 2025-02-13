nome, vida, distancia, velocidade, defesa = input().split(' - ')

vida = int(vida)
distancia = int(distancia)
velocidade = int(velocidade)
defesa = int(defesa)

inimigo = [nome, vida, distancia, velocidade, defesa]

def use_zap(inimigo):
    
    if inimigo[4] == 1:
        if inimigo[2] > 1:
            inimigo[3] -= 1
            inimigo[2] -= inimigo[3]
    elif inimigo[4] == 0:
        if inimigo[2] > 1:
            inimigo[1] -= 5
            inimigo[3] -= 1
            inimigo[2] -= inimigo[3]
            
    return inimigo