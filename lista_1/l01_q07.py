player_1 = input()
gols_1 = int(input())
jogos_1 = int(input())
velocidade_1 = float(input())

player_2 = input()
gols_2 = int(input())
jogos_2 = int(input())
velocidade_2 = float(input())

player_3 = input()
gols_3 = int(input())
jogos_3 = int(input())
velocidade_3 = float(input())

points_1 = ((gols_1 * 5) + (jogos_1 * 2) + (velocidade_1 * 3)) / 10 + (len(player_1) % 3)
points_2 = ((gols_2 * 5) + (jogos_2 * 2) + (velocidade_2 * 3)) / 10 + (len(player_2) % 3)
points_3 = ((gols_3 * 5) + (jogos_3 * 2) + (velocidade_3 * 3)) / 10 + (len(player_3) % 3)


if(points_1 > points_2):
    if(points_1 > points_3):
        if(points_2 > points_3):
            print('1 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
            print('2 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
            print('3 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
            print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_1, points_1))
        else:
            print('1 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
            print('2 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
            print('3 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
            print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_1, points_1))
    else:
        print('1 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
        print('2 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
        print('3 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
        print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_3, points_3))
else:
    if(points_2 > points_3):
        if(points_3 > points_1):
            print('1 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
            print('2 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
            print('3 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
            print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_2, points_2))
        else:
            print('1 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
            print('2 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
            print('3 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
            print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_2, points_2))
    else:
        print('1 - {} obteve {:.2f} pontos.'.format(player_3, points_3))
        print('2 - {} obteve {:.2f} pontos.'.format(player_2, points_2))
        print('3 - {} obteve {:.2f} pontos.'.format(player_1, points_1))
        print('{} é o verdadeiro ganhador da Bola de Ouro com um total de {:.2f} pontos.'.format(player_3, points_3))