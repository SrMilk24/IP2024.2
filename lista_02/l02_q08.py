rodadas = int(input())
pontos = 0
duendes = 0
elfos = 0
duendes_dificuldade = 0
elfos_dificuldade = 0

print('O Torneio de Natal começa agora! Que vençam os melhores!')
for x in range(1, rodadas+1):
    print('RODADA {}'.format(x))
    equipe = input()
    desafio = input()
    dificuldade = input()
    
    if(desafio == 'Prepararam as roupas do Papai Noel.' or desafio == 'Alimentaram as renas.'):
        pontos += 10
    elif(desafio == 'Arrumaram os estoques de doces.' or desafio == 'Guardaram os presentes no trenó.'):
        pontos += 20
    elif(desafio == 'Ajudaram a carregar os presentes.' or desafio == 'Embrulharam os presentes.' or desafio == 'Decoraram a árvore de Natal.'):
        pontos += 30
    elif(desafio == 'Planejaram a rota do Papai Noel.'):
        pontos += 50
    elif(desafio == 'Testaram os brinquedos.'):
        quantidade = int(input())
        pontos += quantidade * 2
        
    if(dificuldade == 'Fácil'):
        pontos = pontos
    elif(dificuldade == 'Médio'):
        pontos *=  1.2
    elif(dificuldade == 'Difícil'):
        pontos *= 1.5
        if(equipe == 'Duendes'):
            duendes_dificuldade += 1
        elif(equipe == 'Elfos'):
            elfos_dificuldade += 1
        
    surpresa = input()
    
    if(surpresa == 'Dia de Sorte'):
        print('É um Dia de Sorte! Vocês ganharam 30 meias bônus!')
        pontos += 30
    elif(surpresa == 'Dia de Azar'):
        print('É um Dia de Azar! Vocês perderam 30 meias!')
        pontos -= 30
        if(pontos < 0):
            pontos = 0
    elif(surpresa == 'Grinch'):
        print('O Grinch está sabotando o Torneio!')
        condicao = ''
        while(condicao != '{}, protejam as meias!'.format(equipe)):
            condicao = input()
            
            if(condicao == 'Amarelas'):
                pontos -= 5
            elif(condicao == 'Verdes'):
                pontos -= 10
            elif(condicao == 'Vermelhas'):
                pontos -= 20
            else:
                continue
        if(pontos < 0):
            pontos = 0
    
    if(equipe == 'Duendes'):
        duendes += pontos
    elif(equipe == 'Elfos'):
        elfos += pontos
    if(pontos != 0):
        print('A equipe dos {} ganhou {} meias nesta rodada.'.format(equipe, int(pontos)))
    else:
        print('Infelizmente, a equipe dos {} não ganhou meias nessa rodada.'.format(equipe))
    pontos = 0
    
print('TORNEIO ENCERRADO!')
print('Segurem seus gorros que o Noel já vai entregar o Prêmio da Estrela Natalina.')

if(elfos > duendes):
    print('Os Elfos venceram o Torneio de Natal com um total de {} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.'.format(int(elfos)))
elif(duendes > elfos):
    print('Os Duendes venceram o Torneio de Natal com um total de {} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.'.format(int(duendes)))
else:
    if(elfos_dificuldade > duendes_dificuldade):
        print('Os Elfos venceram o Torneio de Natal com um total de {} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.'.format(int(elfos)))
    else:
        print('Os Duendes venceram o Torneio de Natal com um total de {} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.'.format(int(duendes)))
        
        