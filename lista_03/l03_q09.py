qnt_ash, qnt_gary = input().split()
ash_pkm = []
gary_pkm = []
batalhas = []
validador = ""

for x in range(int(qnt_ash)):
    dados = input()
    pokemon = []
    for x in dados.split(","):
        pokemon.append(x.strip(' '))
    ash_pkm.append(pokemon)
    
for x in range(int(qnt_gary)):
    dados = input()
    pokemon = []
    for x in dados.split(","):
        pokemon.append(x.strip(' '))
    gary_pkm.append(pokemon)


while validador != "FIM DAS BATALHAS":
    decisao = input()
    num_ash, num_gary = input().split()
    if (int(num_ash) + int(num_gary)) % 2 == 0:
        if(decisao == 'par'):
            escolha_1 = input()
            escolha_2 = input()
            pokemon_1 = escolha_1.split(' ')[0]
            pokemon_2 = escolha_2.split(' ')[0]