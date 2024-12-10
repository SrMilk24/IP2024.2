name = input()
games = int(input())
gols = int(input())
assistences = int(input())
desarms = int(input())
league = input()


score = ((gols * 2) + assistences + (desarms * 0.4))
final_score = 0

if(league == 'Premier League'):
    final_score = score
elif(league == 'La Liga'):
    final_score = score * 0.95
elif(league == 'Serie A'):
    final_score = score * 0.9
elif(league == 'Brasileirão'):
    final_score = score * 0.8
    
if(league == 'Premier League' or league == 'La Liga' or league == 'Serie A' or league == 'Brasileirão'):
    if((gols / games) >= 0.3):
        if((assistences / games) >= 0.15):
            if((desarms / games) >= 1.25):
                if(games >= 50):
                    if(final_score >= 80):
                        print('Promissor! {} é um potencial ganhador da Bola de Ouro!'.format(name))
                    elif(final_score >= 70 and final_score < 80):
                        print('{} tem chances médias de ganhar o prêmio.'.format(name))
                    elif(final_score < 70):
                        print('{} dificilmente ganhará a premiação, apesar de ser apto.'.format(name))
                else:
                    print('O atleta não jogou partidas o suficiente para concorrer à premiação.')
            else:
                print('{} não desarmou jogadores o suficiente, portanto está fora.'.format(name))
        else:
            print('Infelizmente não teve assistências o suficiente, portanto não concorre ao prêmio.')
    else:
        print('O jogador está fora, não possui a média de gols necessária.')
else:
    print('A liga informada não é válida ou o jogador não pertence a nenhuma das ligas elegíveis para a premiação.')