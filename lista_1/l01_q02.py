chooser_1 = input()
chooser_2 = input()
winner = input()

if (winner == "Palé" or ((chooser_1 == 'Gavião Bonito' or chooser_2 == 'Gavião Bonito') and (chooser_1 == 'Ronaldinho Paulisa' or chooser_2 == 'Ronaldinho Paulista'))):
    print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
elif (winner == "Mãodona"):
    if(chooser_1 == 'Gavião Bonito' or chooser_2 == 'Gavião Bonito'):
        if(chooser_1 == 'Ronaldinho Paulista' or chooser_2 == 'Ronaldinho Paulista'):
            print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
        else:
            print('Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…')
    else:
        if(chooser_1 == 'Ronaldinho Paulista' or chooser_2 == 'Ronaldinho Paulista'):
            print('Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…')
        else:
            print('PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.')
else:
    print("Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.")