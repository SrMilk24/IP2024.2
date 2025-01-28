lim_animes = int(input())
qnt_animes = int(input())
animes = []

for indicacao in range(qnt_animes):
    entrada = input()
    
    indicado = entrada.split("-")
    if len(animes) < lim_animes:
        if indicado[2].strip() == "Walter":
            animes.append(indicado[0].strip())
            print(f"O {indicado[0].strip()} foi adicionado à lista de animes para assistir.")
        elif(indicado[2].strip() == "Internet"):
            if(int(indicado[1].strip()) <= 16):
                animes.append(indicado[0].strip())
                print(f"O {indicado[0].strip()} foi adicionado à lista de animes para assistir.")
            else:
                print(f"O {indicado[0].strip()} é muito longo, fica pra próxima.")
    else:
        print(f"A lista de animes está cheia. O {indicado[0].strip()} não foi adicionado.")
print(f"Lista final para assistir:{animes}")