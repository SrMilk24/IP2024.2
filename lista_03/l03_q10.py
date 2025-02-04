nome_feiticeiro = input()
vida_feiticeiro = int(input())
ataque_feiticeiro = int(input())
defesa_feiticeiro = int(input())
reversao_feitico = input()
expansao_dominio = input()

vida_mahoraga = int(input())
ataque_mahoraga = int(input())
defesa_mahoraga = int(input())
mahoraga_golpes = ["ataque", "regeneração", "adaptação"]

golpes = input().split(', ')
contador_golpes = []
ataque_anterior = ''

for golpe in golpes:
    if golpe != "expansão de domínio" and golpe != "black flash":
        contador_golpes.append([golpe, 0])

if reversao_feitico == "True":
    print("Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!")
else:
    print("Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!")

while vida_feiticeiro > 0 and vida_mahoraga > 0:
    mov_feiticeiro = input()
    mov_mahoraga = input()
    

    ataque_anterior = mov_feiticeiro

    if mov_feiticeiro not in golpes and mov_feiticeiro != "black flash" and mov_feiticeiro != "expansão de domínio" and mov_feiticeiro != "reversão de feitiço":
        print("Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!")
    
    if mov_feiticeiro == "expansão de domínio":
        if nome_feiticeiro != "Satoru Gojo":
            if expansao_dominio == "True":
                print("Nem mesmo a sua adaptação pode derrotar isto!")
                vida_mahoraga = 0
            else:
                print("Droga. Eu não aprendi a expandir meu domínio ainda!")
        else:
            print(f"Como assim o Mahoraga já se adaptou ao infinito de {nome_feiticeiro}!?")

    if mov_feiticeiro == "black flash":
        vida_mahoraga -= ((ataque_feiticeiro + 25) * 2)
        print("As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!")

    if mov_feiticeiro == "reversão de feitiço" and reversao_feitico == "True":
        print("Eu posso continuar lutando mais um pouco...")
        vida_feiticeiro += 25
    
    if mov_feiticeiro in golpes and mov_feiticeiro != "black flash" and mov_feiticeiro != "expansão de domínio" and mov_feiticeiro != "reversão de feitiço":
        index_golpe = golpes.index(mov_feiticeiro)

        full_adaptado = 0

        for x in contador_golpes:
            if x[1] >= 3:
                full_adaptado += 1
            
        if full_adaptado == len(contador_golpes):
            print("Droga... Eu não tenho mais nada pra usar contra o Mahoraga... Essa luta acabou.")
            vida_feiticeiro = 0
        else:
            if contador_golpes[index_golpe][1] == 0:
                vida_mahoraga -= (ataque_feiticeiro - defesa_mahoraga) + 25
                print(f"A roda do Mahoraga girou uma vez! {mov_feiticeiro} só vai funcionar mais duas vezes")
                
                contador_golpes[index_golpe][1] += 1
            elif contador_golpes[index_golpe][1] == 1:
                vida_mahoraga -= ((ataque_feiticeiro - defesa_mahoraga) + 25) // 2
                print(f"A roda do Mahoraga girou pela segunda vez! {mov_feiticeiro} só vai funcionar mais uma vez")
                
                contador_golpes[index_golpe][1] += 1
            elif contador_golpes[index_golpe][1] == 2:
                print(f"A roda do Mahoraga girou pela terceira vez! {mov_feiticeiro} não vai funcionar mais")
                
                vida_mahoraga -= ((ataque_feiticeiro - defesa_mahoraga) + 25) // 4
                contador_golpes[index_golpe][1] += 1
            elif contador_golpes[index_golpe][1] > 3:
                print("Esse ataque é inútil! Melhor tentar outra coisa.")

    
        if vida_mahoraga > 0:

            if mov_mahoraga in mahoraga_golpes:

                if mov_mahoraga == "regeneração":

                    vida_mahoraga += 25

                    print("Ele está se regenerando.")

                elif mov_mahoraga == "adaptação":

                    if ataque_anterior != "reversão de feitiço":

                        if ataque_anterior != "black flash":

                            index_golpe = golpes.index(ataque_anterior)

                            contador_golpes[index_golpe][1] += 1  # Incrementar adaptação corretamente

                            if contador_golpes[index_golpe][1] == 1:

                                print(f"A roda do Mahoraga girou pela segunda vez! {ataque_anterior} só vai funcionar mais uma vez")

                            elif contador_golpes[index_golpe][1] == 2:

                                print(f"A roda do Mahoraga girou pela terceira vez! {ataque_anterior} não vai funcionar mais")

                        else:

                            print("Nem você vai conseguir se adaptar a isso, mahoraga!")

                elif mov_mahoraga == "ataque":

                    vida_feiticeiro -= (ataque_mahoraga - defesa_feiticeiro) + 25

if vida_mahoraga <= 0:
    print(f"{nome_feiticeiro} conseguiu!")

    if nome_feiticeiro != "Sukuna" and nome_feiticeiro != "Satoru Gojo" and nome_feiticeiro != "Megumi Fushiguro":
        print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.")
    else:
        if nome_feiticeiro == "Satoru Gojo":
            print("Nem você sua adaptação é páreo para o infinito, queridinho.")
        elif nome_feiticeiro == "Megumi Fushiguro":
            print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!")
        elif nome_feiticeiro == "Sukuna":
            print("Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!")
else:
    if nome_feiticeiro == "Satoru Gojo":
        print("Magnífico, Satoru Gojo. Lembrarei de você enquanto eu durar nesta vida.")
    else:
        print(f"Parece que nem mesmo {nome_feiticeiro} foi pareo contra o Mahoraga...")