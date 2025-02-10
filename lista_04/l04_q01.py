def calcula_energia(tempo, potencia, ineficiencia):
    energia_inicial = potencia * tempo
    energia_inicial += energia_inicial * (ineficiencia/100)
    return energia_inicial

def calcula_preco(consumo, preco_unidade):
    return consumo * preco_unidade

maquinas = int(input())
custo_total = 0
maquina_custosa = 0

for x in range(maquinas):
    tempo = int(input())
    potencia = float(input())
    ineficiencia = int(input())
    preco = float(input())

    cal_energia = calcula_energia(tempo, potencia, ineficiencia)
    cal_custo = calcula_preco(preco, cal_energia)

    if cal_custo > maquina_custosa:
        maquina_custosa = cal_custo
    custo_total += cal_custo

    if cal_energia == 0:
        print("Parece que essa coisa nem ao menos funciona")
    elif cal_energia > 0 and cal_energia <= 100:
        print(f"Temos aqui uma máquina formidável, seu consumo de energia é {cal_energia:.2f}")
    elif cal_energia > 100 and cal_energia <= 300:
        print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {cal_energia:.2f}")
    elif cal_energia > 300:
        print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")

print(f"Os gastos totais com as maquinas foi de {custo_total:.2f}")
print(f"A máquina mais cara gasta um total de {maquina_custosa:.2f} para os cofres de Piltover")