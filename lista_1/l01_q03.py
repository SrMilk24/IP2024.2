name_player_1 = input()
player_1_points = int(input())

name_player_2 = input()
player_2_points = int(input())

name_player_3 = input()
player_3_points = int(input())

winner = ''
winner_points = 0

if(player_1_points > player_2_points):
    if(player_1_points > player_3_points):
        winner = name_player_1
        winner_points = player_1_points
    else:
        winner = name_player_3
        winner_points = player_3_points
else:
    if(player_2_points > player_3_points):
        winner = name_player_2
        winner_points = player_2_points
    else:
        winner = name_player_3
        winner_points = player_3_points


if(name_player_1 == 'Rodri'):
    winner = name_player_1
    winner_points = player_1_points
elif(name_player_2 == 'Rodri'):
    winner = name_player_2
    winner_points = player_2_points
elif(name_player_3 == 'Rodri'):
    winner = name_player_3
    winner_points = player_3_points
    
print('O melhor jogador do mundo é {}, com {} ponto(s).'.format(winner, winner_points))
if(winner == 'Vini Jr.'):
    print('Os brasileiros amaram o resultado! BAILA VINI!')
elif(winner == 'Rodri'):
    print('Os europeus, como sempre, roubaram o nosso ouro!')
else:
    print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')