def caca_tesouro(sequencia, posicao = 0, energia = 4, tesouro = 0, moeda = 0):
    if len(sequencia) > 0:
        if energia > 0:
            if len(sequencia) > posicao:
                if sequencia[posicao] == "X":
                    return caca_tesouro(sequencia, posicao+1, energia-1, tesouro, moeda)
                elif sequencia[posicao].isnumeric():
                    return caca_tesouro(sequencia, posicao+1, energia-1, tesouro, moeda+int(sequencia[posicao]))
                else:
                    print(f"Oba! Encontrei um {sequencia[posicao]} 🐧🎉")
                    return caca_tesouro(sequencia, posicao+1, energia+1, tesouro+1, moeda)
                    
        else:
            print("Ah, cansei. Vou descansar.")
            return [tesouro, moeda]

    return [tesouro, moeda]

entrada = input().split(',')
entrada = [item.strip() for item in entrada]

resultado = caca_tesouro(entrada)

if resultado[0] == 0 and resultado[1] == 0:
    print("Essa caminhada não foi nada produtiva. É melhor ir pescar.")
elif resultado[0] != 0 and resultado[1] == 0:
    print(f"Dinheiro? Não temos. Mas temos {resultado[0]} itens raros.")
elif resultado[0] == 0 and resultado[1] != 0:
    print(f"Estamos ricos!! Encontrei {resultado[1]} moedas.")
else:
    print(f"Quem diria!! {resultado[1]} moedas e {resultado[0]} itens raros. Hoje eu mereço bolo, não aqueles puffitos de sempre.")
