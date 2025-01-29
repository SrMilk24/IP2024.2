validador = ""
armas = [[], [], [], [], []]
objetos = [[], [], [], [], []]
lista_vazia = []
while validador != "Catalogação encerrada!":
    tipo_item = input()
    if tipo_item == "Catalogação encerrada!":
        validador = "Catalogação encerrada!"
    else:
        item = input()
        if tipo_item == "arma":
            arma = item.split("-")
            if(int(arma[1]) == 0):
                armas[0].append(arma[0].strip())
            elif(int(arma[1]) == 1):
                armas[1].append(arma[0].strip())
            elif(int(arma[1]) == 2):
                armas[2].append(arma[0].strip())
            elif(int(arma[1]) == 3):
                armas[3].append(arma[0].strip())
            elif(int(arma[1]) == 4):
                armas[4].append(arma[0].strip())
            print(f"A arma {arma[0].strip()} foi catalogada com sucesso!")

        elif tipo_item == "objeto":
            objeto = item.split("-")
            if(int(objeto[1]) == 0):
                objetos[0].append(objeto[0].strip())
            elif(int(objeto[1]) == 1):
                objetos[1].append(objeto[0].strip())
            elif(int(objeto[1]) == 2):
                objetos[2].append(objeto[0].strip())
            elif(int(objeto[1])  == 3):
                objetos[3].append(objeto[0].strip())
            elif(int(objeto[1])  == 4):
                objetos[4].append(objeto[0].strip())
            print(f"O objeto {objeto[0].strip()} foi catalogado com sucesso!")
    

print("Processando lista de itens…\n")
print("ITENS AMALDIÇOADOS DA TOKYO JUJUTSU HIGH")
print()
print("Objetos")
if len(objetos[0]) > 0:
    print("Categoria Especial: " + ", ".join(objetos[0]))
if len(objetos[1]) > 0:
    print("Nível 1: " + ", ".join(objetos[1]))
if len(objetos[2]) > 0:
    print("Nível 2: " + ", ".join(objetos[2]))
if len(objetos[3]) > 0:
     print("Nível 3: " + ", ".join(objetos[3]))
if len(objetos[4]) > 0:
    print("Nível 4: " + ", ".join(objetos[4]))

print("\nArmas")
if len(armas[0]) > 0:
    print("Categoria Especial: " + ", ".join(armas[0]))
if len(armas[1]) > 0:
    print("Nível 1: " + ", ".join(armas[1]))
if len(armas[2]) > 0:
    print("Nível 2: " + ", ".join(armas[2]))
if len(armas[3]) > 0:
    print("Nível 3: " + ", ".join(armas[3]))
if len(armas[4]) > 0:
    print("Nível 4: " + ", ".join(armas[4]))