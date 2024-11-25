chooser_1 = input()
chooser_2 = input()
winner = input()

if winner != 'Palé' and winner != 'Mãodona':
    print('Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.')
else:
    if(winner == "Mãodona"):
        if(chooser_1 == 'Gavião Bonito') or (chooser_2 == 'Gavião Bonito'):
            if(chooser_1 == 'Ronaldinho Paulista') or (chooser_2 == 'Ronaldinho Paulista'):
                print('Lutamos e conseguimos! Nosso trio maravilha subiu no palco e garantiram o merecido troféu! É DO BRASIL!!!')
            else:
                print('Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…')
        else:
            if(chooser_1 == 'Ronaldinho Paulista') or (chooser_2 == 'Ronaldinho Paulista'):
                print('Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…')
            else:
                print('PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.')
    elif(winner == 'Palé'):
        print('Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!')
    else:
        print('Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.')