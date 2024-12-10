condicao = True
musicas = 0
ultima_musica = ''
viloes = 0
print('PLAYLIST DO PAPAI NOEL')
while(condicao):
    entrada = input()
    tamanho = len(entrada) - entrada.count(' ')

    if(entrada == 'FIM'):
        if(musicas != 0):
            print('Ufa! Conseguimos criar a playlist perfeita, tomara que o Papai Noel goste das {} músicas.'.format(musicas))
            condicao = False
            break
        else:
            print('Infelizmente não conseguimos encontrar nenhuma música para a playlist do Papai Noel...')
            condicao = False
            break


    if(entrada.isnumeric()):
        viloes += 1
        if(viloes < 3):
            musicas = 0
            print('ABORTAR! OS VILÕES OBTIVERAM ACESSO, TEREMOS QUE RECOMEÇAR.')
            print('PLAYLIST DO PAPAI NOEL')
        else:
            print('NAAÃO! Já está na hora do Papai Noel sair e não conseguimos construir sua playlist perfeita.')
            condicao = False
            break        
    elif(tamanho >= 15 and entrada.replace(' ', '').isalpha()):
        print('{} foi adicionada à playlist!'.format(entrada))
        musicas += 1
        ultima_musica = entrada
    else:
        if(musicas == 0):
            print('{} não pôde ser adicionada e a playlist continua vazia. Papai Noel precisa da sua ajuda!'.format(entrada))
        else:
            print('{} não pôde ser adicionada à playlist! A última música adicionada foi {}.'.format(entrada, ultima_musica))
    
