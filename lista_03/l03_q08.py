gojo_bat = input()
geto_seq = int(input())
geto_sum = int(input())

lista_gojo = []
maior_seq = []
seq = []

gojo = gojo_bat.split("-")

#Idenficiando a maior sequencia de Gojo

for x in range(len(gojo)):
    lista_gojo.append(int(gojo[x]))

for x in range(1,len(lista_gojo)):
    if lista_gojo[x] == lista_gojo[x-1] + 1:
        seq.append(lista_gojo[x])
    else:
        if len(seq) > len(maior_seq):
            maior_seq = seq
        seq = [lista_gojo[x]]

if len(seq) > len(maior_seq):
    maior_seq = seq


if len(maior_seq) > geto_seq:
    print("Uma vitória avassaladora de Satoru Gojo. Nem mesmo o infinito pode pará-lo. Ele realmente é o melhor!")
elif len(maior_seq) < geto_seq:
    print("Inesperado! Suguru Geto domina com maestria. Uma vitória indiscutível!")
else:
    soma_gojo = 0
    for x in maior_seq:
        soma_gojo += x
    
    if soma_gojo > geto_sum:
        print("Gojo vence por pouco. Mesmo com toda a pressão, ele continua no topo!")
    elif soma_gojo < geto_sum:
        print("Geto vence por pouco. Sua estratégia foi impecável nesta batalha!")
    else:
        print("Um empate absoluto! Quem diria que duas lendas podem ser tão iguais em poder?")