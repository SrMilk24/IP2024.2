membros = int(input())

condição = True

nota = 0
contador_br = 0
contador_ext = 0

print('MARATONA DE NATAL: PAVÊ, RABANADA E FILMES')
while(condição):
    nome_filme = input()
    if(nome_filme == 'chega de filmes por hoje'):
        condição = False
        break
    nacionalidade = input()
    
    
    if('natal' in nome_filme.lower() or 'papai noel' in nome_filme.lower() or 'magia' in nome_filme.lower()):
        if(nacionalidade.lower() == 'br' or nacionalidade.lower() == 'brasil'):
            for x in range(0, membros):
                nota_filme = int(input())
                nota += nota_filme
            contador_br += 1
            print('{}º filme: {}'.format(contador_br, nome_filme))
            print('Média de votos para {}: {:.1f}'.format(nome_filme, nota/membros))
            nota = 0
    elif('natal' in nome_filme.lower() or 'papai noel' in nome_filme.lower() or 'magia' in nome_filme.lower()):
        if(nacionalidade.lower() != 'br' and nacionalidade.lower() != 'brasil'):
            contador_ext += 1

print('{} Filmes BR X {} Filmes FORA'.format(contador_br, contador_ext))

if(contador_br == 0):
    print('Infelizmente esse ano não será nem pa vê e nem pa comer, sua lista não possui um filme bom, ops… nacional')
elif(contador_br == 1):
    print('De toda sua lista, apenas UM filme de natal é nacional, melhore suas escolhas e tente novamente!')
else:
    print('A ceia está servida? Porque aqui estão os filmes brasileiros que vão dar o toque especial da sua maratona no Natal!')