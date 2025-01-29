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

qnt_amigos = int(input())
print(f"{qnt_amigos} amigos participaram da votação!")
for x in range(qnt_amigos):
    amigo_lista = []
    amigo = input()
    print(f"{amigo} é a {x}ª pessoa à votar!")
    while len(amigo_lista) < 3:
        anime = input()
        if anime in animes_favoritos:
            if anime not in amigo_lista:
                print(f"{amigo} colocou {anime} em {len(amigo_lista)+1}º lugar do seu ranking!")
                amigo_lista.append(anime)
        else:
            print(f"{amigo}, você já votou neste anime! Escolha um outro anime para ocupar a sua {len(amigo_lista)+1}º posição!")

