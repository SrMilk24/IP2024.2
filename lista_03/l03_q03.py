qnt_monitores = int(input())

aprimoradores = []
emissores = []
transmutadores = []
manipuladores = []
conjuradores = []
especialistas = []

for x in range(qnt_monitores):
    nome = input()
    mudanca = input()

    if nome in aprimoradores:
        aprimoradores.remove(nome)
    elif nome in emissores:
        emissores.remove(nome)
    elif nome in transmutadores:
        transmutadores.remove(nome)
    elif nome in manipuladores:
        manipuladores.remove(nome)
    elif nome in conjuradores:
        conjuradores.remove(nome)
    elif nome in especialistas:
        especialistas.remove(nome)
    
    if(mudanca == "O volume da água foi alterado."):
        aprimoradores.append(nome)
    elif(mudanca == "A cor da água foi alterada."):
        emissores.append(nome)
    elif(mudanca == "O gosto da água foi alterado."):
        transmutadores.append(nome)
    elif(mudanca == "A folha se moveu."):
        manipuladores.append(nome)
    elif(mudanca == "Impurezas apareceram na água."):
        conjuradores.append(nome)
    else:
        especialistas.append(nome)

if(len(aprimoradores) > 0):
    monitores = ', '.join(aprimoradores)
    print(f"Temos um total de {len(aprimoradores)} aprimoradores entre os monitores! Eles são: {monitores}")
if(len(emissores) > 0):
    monitores = ', '.join(emissores)
    print(f"Temos um total de {len(emissores)} emissores entre os monitores! Eles são: {monitores}")
if(len(transmutadores) > 0):
    monitores = ', '.join(transmutadores)
    print(f"Temos um total de {len(transmutadores)} transmutadores entre os monitores! Eles são: {monitores}")
if(len(manipuladores) > 0):
    monitores = ', '.join(manipuladores)
    print(f"Temos um total de {len(manipuladores)} manipuladores entre os monitores! Eles são: {monitores}")
if(len(conjuradores) > 0):
    monitores = ', '.join(conjuradores)
    print(f"Temos um total de {len(conjuradores)} conjuradores entre os monitores! Eles são: {monitores}")
if(len(especialistas) > 0):
    monitores = ', '.join(especialistas)
    print(f"Temos um total de {len(especialistas)} especialistas entre os monitores! Eles são: {monitores}")

