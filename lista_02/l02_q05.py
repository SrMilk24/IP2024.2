primeira_musica = ''
segunda_musica= ''
terceira_musica = ''

maior_stream = 0
menor_stream = 0
media_stream = 0

for x in range(0,3):
    nome_musica = input()
    quantidade_streams = int(input())

    if(maior_stream == 0):
        maior_stream = quantidade_streams
        primeira_musica = nome_musica
    else:
        if(media_stream == 0):
            if(quantidade_streams > maior_stream):
                media_stream = maior_stream
                maior_stream = quantidade_streams
                segunda_musica = primeira_musica
                primeira_musica = nome_musica
            else:
                media_stream = quantidade_streams
                segunda_musica = nome_musica
        elif(menor_stream == 0):
            if(quantidade_streams > maior_stream):
                if(maior_stream > media_stream):
                    menor_stream = media_stream
                    media_stream = maior_stream
                    maior_stream = quantidade_streams
                    terceira_musica = segunda_musica
                    segunda_musica = primeira_musica
                    primeira_musica = nome_musica
                else:
                    menor_stream = maior_stream
                    maior_stream = quantidade_streams
                    terceira_musica = primeira_musica
                    primeira_musica = nome_musica
            else:
                if(quantidade_streams > media_stream):
                    menor_stream = media_stream
                    terceira_musica = segunda_musica
                    media_stream = quantidade_streams
                    segunda_musica = nome_musica
                else:
                    menor_stream = quantidade_streams
                    terceira_musica = nome_musica

print('1º: {} teve {} de streams e foi a música mais ouvida de Simone!'.format(primeira_musica, maior_stream))
print('2º: {} teve {} de streams e foi a segunda música mais ouvida de Simone!'.format(segunda_musica, media_stream))
print('3º: {} teve {} de streams e completou o top 3 das músicas mais ouvidas da artista!'.format(terceira_musica, menor_stream))
                

if(maior_stream > 10000000):
    print('Uau! {} foi um hit certeiro da rainha do Natal!'.format(primeira_musica))
elif(maior_stream < 1000000):
    print('Bom… a música {} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.'.format(primeira_musica))

if(media_stream > 10000000):
    print('Uau! {} foi um hit certeiro da rainha do Natal!'.format(segunda_musica))
elif(media_stream < 1000000):
    print('Bom… a música {} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.'.format(segunda_musica))    

if(menor_stream > 10000000):
    print('Uau! {} foi um hit certeiro da rainha do Natal!'.format(terceira_musica))
elif(menor_stream < 1000000):
    print('Bom… a música {} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.'.format(terceira_musica))
    

if(maior_stream - media_stream > 5000000):
    print('{} foi disparada a mais ouvida neste ano! Nenhuma outra música natalina chega aos pés dela!'.format(primeira_musica))
if(maior_stream - media_stream < 1000000):
    print('{} foi a mais ouvida, mas não podemos esquecer da música {}! Fez bonito nesse feriado!'.format(primeira_musica, segunda_musica))