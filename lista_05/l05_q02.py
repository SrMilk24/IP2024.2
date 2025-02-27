#entrada = input().split(',')

def caca_tesouro(sequencia, posicao = 0, energia = 4, tesouro = 0, moeda = 0):
    valores = sequencia.split(', ')
    if len(valores) > 0:
        if energia > 0:
            if len(valores) > posicao:
                print(valores[1])

                if valores[posicao] == "X":
                    caca_tesouro(sequencia, posicao+1, energia-1, tesouro, moeda)
                elif valores[posicao].isnumeric():
                    caca_tesouro(sequencia, posicao+1, energia-1, tesouro, moeda+1)
                else:
                    caca_tesouro(sequencia, posicao+1, energia+1, tesouro+1, moeda)
        else:
            print("Ah, cansei. Vou descansar.")
            return [tesouro, moeda]

    return [tesouro, moeda]

print(caca_tesouro("X, 5, 5 X, 2, 9, X "))