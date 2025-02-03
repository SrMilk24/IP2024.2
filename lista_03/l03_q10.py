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

for golpe in golpes:
    if golpe != "expansão de domínio" and golpe != "black flash":
        contador_golpes.append([golpe, 0])

if reversao_feitico == "False":
    print("Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!")
else:
    print("Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!")

while vida_feiticeiro > 0 or vida_mahoraga > 0:
    mov_feiticeiro = input()
    mov_mahoraga = input()

    if mov_feiticeiro not in golpes and mov_feiticeiro != "black flash" and mov_feiticeiro != "expansão de domínio":
        print("Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!")
    
    if mov_feiticeiro == "expansão de domínio":
        if nome_feiticeiro != "Satoru Gojo":
            if(expansao_dominio == "True"):
                print("Nem mesmo a sua adaptação pode derrotar isto!")
                vida_mahoraga = 0
            else:
                print("Droga. Eu não aprendi a expandir meu domínio ainda!")
        else:
            print("Como assim o Mahoraga já se adaptou ao infinito de Satoru Gojo!?")

    if mov_feiticeiro == "black flash":
        vida_mahoraga -= (ataque_feiticeiro - defesa_mahoraga) + 25
        print("As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!")

    if mov_feiticeiro == "reversão de feitiço" and reversao_feitico == "True":
        print("Eu posso continuar lutando mais um pouco...")
    
    if mov_feiticeiro in golpes and mov_feiticeiro != "black flash" and mov_feiticeiro != "expansão de domínio":
        index_golpe = golpes.index(mov_feiticeiro)
        if contador_golpes[index_golpe][1] == 0:
            vida_mahoraga -= (ataque_feiticeiro - defesa_mahoraga) + 25
            print(f"A roda do Mahoraga girou uma vez! {mov_feiticeiro} só vai funcionar mais duas vezes")
            contador_golpes[index_golpe][1] += 1
        elif contador_golpes[index_golpe][1] == 1:
            vida_mahoraga -= ((ataque_feiticeiro - defesa_mahoraga) + 25) / 2
            print(f"A roda do Mahoraga girou pela segunda vez! {mov_feiticeiro} só vai funcionar mais uma vez")
            contador_golpes[index_golpe][1] += 1
        elif contador_golpes[index_golpe][1] == 2:
            print(f"A roda do Mahoraga girou pela terceira vez! {mov_feiticeiro} não vai funcionar mais")
            vida_mahoraga -= ((ataque_feiticeiro - defesa_mahoraga) + 25) / 4
            contador_golpes[index_golpe][1] += 1
        elif contador_golpes[index_golpe][1] > 3:
            print("Esse ataque é inútil! Melhor tentar outra coisa.")