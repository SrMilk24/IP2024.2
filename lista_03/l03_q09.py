batalhas = []
pkm_ash = []
pkm_gary = []
gary = 0
ash = 0

qnt_pkm = list(map(int, input().split()))

for x in range(2):
    for z in range(qnt_pkm[x]):
        pokemon = input().split(', ')
        if x == 0:
            pkm_ash.append(pokemon)
        elif x == 1:
            pkm_gary.append(pokemon)

validador = ""
print(f"QUE COMECEM AS BATALHAS")
if qnt_pkm[0] > 0 and qnt_pkm[1] > 0:
    while validador != "FIM DAS BATALHAS":
        decisao = input() 
        vencedor = ''
        
        if decisao != "FIM DAS BATALHAS":
            numeros = input().split(' ')
            numeros = list(map(int, numeros))
            
            if decisao == 'par':
                vencedor = 'ash' if sum(numeros) % 2 == 0 else 'gary'
            else:
                vencedor = 'ash' if sum(numeros) % 2 != 0 else 'gary'
            
            a = input().split(' ')
            escolha_pokemon_ash = a[0]
            g = input().split(' ')
            escolha_pokemon_gary = g[0]
            
            ash_escolha = ''
            gary_escolha = ''
            
            for x in range(len(pkm_ash)):
                if pkm_ash[x][0] == escolha_pokemon_ash:
                    ash_escolha = int(x)
                    
            for y in range(len(pkm_gary)):
                if pkm_gary[y][0] == escolha_pokemon_gary:
                    gary_escolha = int(y)
            
            ash_hp = int(pkm_ash[x][2])
            ash_atk = int(pkm_ash[x][3]) * 2
            
            gary_hp = int(pkm_gary[y][2])
            gary_atk = int(pkm_gary[y][3]) * 2
            
            while ash_hp > 0 and gary_hp > 0:
                if ash_hp > 0 and gary_hp > 0:
                    if vencedor == 'ash':
                        gary_hp -= ash_atk
                        if gary_hp > 0:
                            ash_hp -= gary_atk
                    else:
                        ash_hp -= gary_atk
                        if ash_hp > 0:
                            gary_hp -= ash_atk
            
            if ash_hp > 0:
                print(f'{escolha_pokemon_gary} desmaiou e {escolha_pokemon_ash} venceu esta luta')
                ash += 1
                batalhas.append([escolha_pokemon_ash.upper(), escolha_pokemon_gary.lower()])
            elif ash_hp < 0 and gary_hp > 0:
                print(f'{escolha_pokemon_ash} desmaiou e {escolha_pokemon_gary} venceu esta luta')
                gary += 1
                batalhas.append([escolha_pokemon_ash.lower(), escolha_pokemon_gary.upper()])
        else:
            validador = "FIM DAS BATALHAS"
print('=============== ===============')
for n in range(len(batalhas)):
    print(f'{n + 1}° Batalha: {batalhas[n][0]} vs {batalhas[n][1]}')

if ash > gary:
    print('Ash é o grande vencedor!')
elif ash < gary:
    print('Gary é o grande vencedor!')
elif qnt_pkm[0] > 0 and qnt_pkm[1] > 0:
    if ash == gary:
        print('Depois de todas as batalhas, ainda terminou em empate!')
elif qnt_pkm[0] == 0 and qnt_pkm[1] == 0:
    print('Nenhuma batalha foi concluída.')
elif qnt_pkm[0] == 0:
    print(f'Ash deixou seus pokemons descansando!')
    print('Gary é o grande vencedor!')
elif qnt_pkm[1] == 0:
    print(f'Gary deixou seus pokemons descansando!')
    print('Ash é o grande vencedor!')