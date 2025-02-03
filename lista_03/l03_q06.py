num_feiticieros = int(input())
feiticeiros = []
contador = 1

for x in range(num_feiticieros):
    nome = input()
    nivel = int(input())
    feiticeiros.append([nome, nivel])

remanescentes = []

while len(feiticeiros) > 1:
    print(f"\n--- Rodada {contador} ---")

    if len(feiticeiros) % 2 == 0:
        for luta in range(0, len(feiticeiros) - 1, 2):
            print(f"Confronto: {feiticeiros[luta][0]} vs {feiticeiros[luta+1][0]}")
            if feiticeiros[luta][1] > feiticeiros[luta+1][1]:
                print(f"{feiticeiros[luta][0]} vence!")
                remanescentes.append(feiticeiros[luta])
            elif feiticeiros[luta][1] < feiticeiros[luta+1][1]:
                print(f"{feiticeiros[luta+1][0]} vence!")
                remanescentes.append(feiticeiros[luta+1])
            else:
                print(f"{feiticeiros[luta][0]} vence!")
                remanescentes.append(feiticeiros[luta])

        feiticeiros = remanescentes
        remanescentes = []
    else:
        for luta in range(0, len(feiticeiros) - 1, 2):
            print(f"Confronto: {feiticeiros[luta][0]} vs {feiticeiros[luta+1][0]}")
            if feiticeiros[luta][1] > feiticeiros[luta+1][1]:
                print(f"{feiticeiros[luta][0]} vence!")
                remanescentes.append(feiticeiros[luta])
            elif feiticeiros[luta][1] < feiticeiros[luta+1][1]:
                print(f"{feiticeiros[luta+1][0]} vence!")
                remanescentes.append(feiticeiros[luta+1])
            else:
                print(f"{feiticeiros[luta][0]} vence!")
                remanescentes.append(feiticeiros[luta])
        print(f"{feiticeiros[-1][0]} avança automaticamente!")
        remanescentes.append(feiticeiros[-1])

        feiticeiros = remanescentes
        remanescentes = []
    contador += 1

print(f"\nO campeão do torneio é {feiticeiros[0][0]} com nível de energia amaldiçoada {feiticeiros[0][1]}!")
if feiticeiros[0][0] == "Itadori":
    if feiticeiros[0][1] > 90:
        print("\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###")
        print("Uma aura de destruição toma conta, não há escapatória.")
        print("Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!")
    else:
        print("\nItadori vence com honra e bravura!")
