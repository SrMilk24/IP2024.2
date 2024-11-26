player_1 =  input()
points_1 = int(input())

player_2 =  input()
points_2 = int(input())

player_3 =  input()
points_3 = int(input())

if (player_1 == 'Lucas Lima') or (player_2 == 'Lucas Lima') or (player_3 == 'Lucas Lima'):
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
else:
    if (points_1 > points_2):
        if (points_1 > points_3):
            print("{} é eleito o bola de ouro!".format(player_1))
        elif(points_1 < points_3):
            print("{} é eleito o bola de ouro!".format(player_3))
    else:
        if(points_2 > points_3):
            print("{} é eleito o bola de ouro!".format(player_2))
        else:
            print("{} é eleito o bola de ouro!".format(player_3))