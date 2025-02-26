def verifica_penguinacci(valor, atual=1, anterior=0):
    if valor == atual or valor == 0:
        return True
    
    if atual > valor:
        return False
    
    return verifica_penguinacci(valor, atual + anterior, atual)

def ler_valores(qnt_valores):
    lista_lida = []
    for _ in range(qnt_valores):
        valor = int(input())
        lista_lida.append(valor)

    return lista_lida

def is_in_penguinacci(lista):
    numeros_penguinacci = []
    for x in lista:
        if verifica_penguinacci(x):
            numeros_penguinacci.append(x)
    
    numeros_penguinacci.sort()
    return numeros_penguinacci

qnt_numeros = int(input())
valores = ler_valores(qnt_numeros)
numeros_penguinacci = is_in_penguinacci(valores)

print(f"Contei um total de {len(numeros_penguinacci)} números que estão na sequência de penguinacci!")

if len(numeros_penguinacci) == 0:
    print("Acho que é melhor revisar a teoria um pouco...")
else:
    if len(numeros_penguinacci) == qnt_numeros:
        print("Boa, Paulo! Todos esses números fazem parte da sequência de penguinacci.")
    else:
        print("Eita, nem todos que você falou fazem parte da sequência de penguinacci. Os que fazem parte são:")
        print(*numeros_penguinacci, sep=', ')

