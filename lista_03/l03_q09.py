qnt_ash, qnt_gary = input().split()
ash_pkm = []
gary_pkm = []
batalhas = []
ash_wins = 0
gary_wins = 0
validador = ""

if qnt_ash == 0 and qnt_gary == 0:
    print("Nenhuma batalha foi concluída.")
else:
    if qnt_ash == 0:
        print("Ash deixou seus pokemons descansando!")
        print("Gary é o grande vencedor!")
    elif qnt_gary == 0:
        print("Gary deixou seus pokemons descansando!")
        print("Ash é o grande vencedor!")
    else:
        for x in range(int(qnt_ash)):
            dados = input()
            pokemon = dados.strip().split(", ")
            ash_pkm.append([pokemon[0], pokemon[1], int(pokemon[2]), int(pokemon[3])])
            
        for x in range(int(qnt_gary)):
            dados = input()
            pokemon = dados.strip().split(", ")
            gary_pkm.append([pokemon[0], pokemon[1], int(pokemon[2]), int(pokemon[3])])

        print("QUE COMECEM AS BATALHAS")
        while validador != "FIM DAS BATALHAS":
            decisao = input()
            if decisao == "FIM DAS BATALHAS" or decisao == "":
                validador = "FIM DAS BATALHAS"
            else:
                num_ash, num_gary = input().split()
                soma = int(num_ash) + int(num_gary)
                nome_pkm_ash = input("").strip().split(' ')[0]
                nome_pkm_gary = input("").strip().split(' ')[0]
                for x in ash_pkm:
                    if x[0] == nome_pkm_ash:
                        pkm_ash = x
                for x in gary_pkm:
                    if x[0] == nome_pkm_gary:
                        pkm_gary = x
                
                if (soma % 2 == 0 and decisao == "par") or (soma % 2 != 0 and decisao == "ímpar"):
                    atk, defs = pkm_ash, pkm_gary
                else:
                    atk, defs = pkm_gary, pkm_ash
                
                batalha = f"{pkm_ash[0]} vs {pkm_gary[0]}"
                batalhas.append(batalha)

                while atk[2] > 0 and defs[2] > 0:
                    dano = atk[3]*2
                    defs[2] -= dano
                    if defs[2] <= 0:
                        if defs[2] <= 0:
                            if atk == pkm_gary:
                                print(f"{pkm_ash[0]} desmaiou e {pkm_gary[0]} venceu esta luta")
                                gary_wins += 1
                            else:
                                print(f"{pkm_gary[0]} desmaiou e {pkm_ash[0]} venceu esta luta")
                                ash_wins += 1
                    atk, defs = defs, atk
                if pkm_ash[2] <= 0:
                    ash_pkm.remove(pkm_ash)
                    if not pkm_ash:
                        validador = "FIM DAS BATALHAS"
                        
                if pkm_gary[2] <= 0:
                    gary_pkm.remove(pkm_gary)
                    if not pkm_gary:
                        validador = "FIM DAS BATALHAS"

                
    print("=============== ===============")

    for x, batalha in enumerate(batalhas):
        winner, loser = batalha.split(" vs ")
        winner = winner.upper()
        loser = loser.lower()
        print(f"{x+1}° Batalha: {winner} vs {loser}")

    if ash_wins > gary_wins:
        print("Ash é o grande vencedor!")
    elif gary_wins > ash_wins:
        print("Gary é o grande vencedor!")
    else:
        print("Depois de todas as batalhas, ainda terminou em empate!")