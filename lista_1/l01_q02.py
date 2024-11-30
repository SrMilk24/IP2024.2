chooser_1 = input()
chooser_2 = input()
winner = input()

if (winner == "Palé"):
        print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
elif (winner == "Mãodona"):
    if (chooser_1 == "Gavião Bonito" and chooser_2 != "Ronaldinho Paulista"):
        print("Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…")
    elif (chooser_1 != "Gavião Bonito" and chooser_2 == "Ronaldinho Paulista"):
        print("Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…")
    elif (chooser_1 == "Gavião Bonito" and chooser_2 == "Ronaldinho Paulista"):
        print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
    else:
        print("PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.")
else:
    print("Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.")