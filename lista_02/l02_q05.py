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

print(primeira_musica, segunda_musica, terceira_musica)
                
if(maior_stream > 10000000 or menor_stream > 10000000  or media_stream > 10000000):
    if(maior_stream > 10000000):
        print('Uau! {} foi um hit certeiro da rainha do Natal!'.format(primeira_musica))
    