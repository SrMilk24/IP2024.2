animes_favoritos = [
    'Fullmetal Alchemist: Brotherhood', 
    'Attack On Titan', 
    'Death Note', 
    'Naruto', 
    'One Piece', 
    'Demon Slayer', 
    'Dragon Ball Z', 
    'Jujutsu Kaisen', 
    'Pokemon', 
    'Bleach'
]

amigos = []

animes_votados = [0,0,0,0,0,0,0,0,0,0]

qnt_amigos = int(input())
print(f"{qnt_amigos} amigos participaram da votação!")
for x in range(qnt_amigos):
    amigo_lista = []
    amigo = input()
    print(f"{amigo} é a {x+1}ª pessoa à votar!")
    while len(amigo_lista) < 3:
        anime = input()
        if anime.title() in animes_favoritos:
            if anime.title() not in amigo_lista:

                print(f"{amigo} colocou {anime.title()} em {len(amigo_lista)+1}º lugar do seu ranking!")
                amigo_lista.append(anime.title())

                if anime.title() == animes_favoritos[0]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[0] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[0] += 2
                    else:
                        animes_votados[0] += 1
                elif anime.title() == animes_favoritos[1]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[1] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[1] += 2
                    else:
                        animes_votados[1] += 1
                elif anime.title() == animes_favoritos[2]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[2] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[2] += 2
                    else:
                        animes_votados[2] += 1
                elif anime.title() == animes_favoritos[3]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[3] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[3] += 2
                    else:
                        animes_votados[3] += 1
                elif anime.title() == animes_favoritos[4]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[4] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[4] += 2
                    else:
                        animes_votados[4] += 1
                elif anime.title() == animes_favoritos[5]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[5] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[5] += 2
                    else:
                        animes_votados[5] += 1
                elif anime.title() == animes_favoritos[6]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[6] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[6] += 2
                    else:
                        animes_votados[6] += 1
                elif anime.title() == animes_favoritos[7]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[7] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[7] += 2
                    else:
                        animes_votados[7] += 1
                elif anime.title() == animes_favoritos[8]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[8] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[8] += 2
                    else:
                        animes_votados[8] += 1
                elif anime.title() == animes_favoritos[9]:
                    if amigo_lista[0] == anime.title():
                        animes_votados[9] += 3
                    elif amigo_lista[1] == anime.title():
                        animes_votados[9] += 2
                    else:
                        animes_votados[9] += 1
                
            else:
                print(f"{amigo}, você já votou neste anime! Escolha um outro anime para ocupar a sua {len(amigo_lista)+1}º posição!")
    
        else:
            print(f"O anime {anime.title()} não está presente na votação!")
    amigo_lista = []

aux_lista = sorted(animes_votados, reverse=True)

mais_votado = animes_votados.index(aux_lista[0])

print(f"Com {aux_lista[0]} pontos, {animes_favoritos[mais_votado]} foi votado como o melhor anime!")
if(animes_favoritos[mais_votado] == "Pokemon"):
    print("César - Pokémon é o melhor anime da história!!!")
print("Eita mandaram dúvida no discord, vou lá responder!")