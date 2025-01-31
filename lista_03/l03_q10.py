feiticeito = []
mahoraga = []
ataques_realizados = []
ataque_anterior = ""
turno = 0

# Variaveis feiticeito
nome = input()
vida = int(input())
ataque = int(input())
defesa = int(input())
reversao = bool(input())
expansao = bool(input())

feiticeito.extend((nome, vida, ataque, defesa, reversao, expansao))

# Variaveis Marohaga
vida_maho = int(input())
atk_maho = int(input())
def_maho = int(input())
mahoraga.extend((vida_maho, atk_maho, def_maho))
# Black Flash - Incapaz de se adaptar; Dano = (atk + 25) * 2
# Expansão de Dominio = Acerto Garantido se Feiticeiro != Gojo
# Cada Ataque só causa dano 3x;
    # 1º - Dano = (ataque - defesa) + 25
    # 2º - Dano = ((ataque - defesa) + 25) / 2
    # 3º - Dano = ((ataque - defesa ) + 25) / 4
# Regen de Vida = +25

#Gerando a lista de golpes do feiticeiro
golpes_feiticeiro = []
mov_mahoraga = ['ataque', 'regeneração', 'adaptação']

golpes = input().split(', ')
for x in golpes:
    golpes_feiticeiro.append(x)
golpes_feiticeiro.append("black flash")
golpes_feiticeiro.append("expansão de domínio")

if(feiticeito[4] == True):
    print("Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!")
else:
    print("Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!")
    
while feiticeito[1] > 0 or vida_maho[0] > 0:
    acao = input()
    ataque_anterior = acao
    if turno % 2 == 0:
        if acao not in golpes_feiticeiro:
            if acao == "reversao de feitiço":
                if feiticeito[4] == True:
                    feiticeito[1] += 25
                    print("Eu posso continuar lutando mais um pouco...")
                else:
                    print("Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!")
        else:
            if acao == "expansão de domínio" and feiticeito[0] != "Satoru Gojo" and feiticeito[5] == True:
                if(feiticeito[5] == True):
                    if(feiticeito[0] != "Satoru Gojo"):
                        print("Nem mesmo a sua adaptação pode derrotar isto!")
                        mahoraga[0] = 0
                    else:
                        print("Como assim o Mahoraga já se adaptou ao infinito de Satoru Gojo!?")
                else:
                    print("Droga. Eu não aprendi a expandir meu domínio ainda!")
            elif acao == "black flash":
                dano = (feiticeito[2] + 25) * 2
                mahoraga[0] -= dano
                print("As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!")
            else:
                if acao not in ataques_realizados:
                    ataques_realizados.append(acao)
                    dano = (feiticeito[2] - mahoraga[2]) + 25
                    mahoraga[0] -= int(dano)
                    print(f"A roda do Mahoraga girou uma vez! {acao} só vai funcionar mais duas vezes")
                else:
                    contador = ataques_realizados.count(acao)
                    if contador == 1:
                        ataques_realizados.append(acao)
                        dano = ((feiticeito[2] - mahoraga[2]) + 25) / 2
                        mahoraga[0] -= int(dano)
                        print(f"A roda do Mahoraga girou pela segunda vez! {acao} só vai funcionar mais uma vez")
                    elif contador == 2:
                        ataques_realizados.append(acao)
                        dano = ((feiticeito[2] - mahoraga[2]) + 25) / 4
                        mahoraga[0] -= int(dano)
                        print(f"A roda do Mahoraga girou pela terceira vez! {acao} não vai funcionar mais")
                    elif contador == 3:
                        print("Esse ataque é inútil! Melhor tentar outra coisa.")