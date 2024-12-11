membros = int(input())

condição = True

nota = 0


while(condição):
    nome_filme = input()
    nacionalidade = input()
    
    if('natal' in nome_filme.lower() or 'papai noel' in nome_filme.lower() or 'magia' in nome_filme.lower() and nacionalidade.lower() == 'br' or nacionalidade.lower() == 'brasil'):
        for x in range(0, membros):
            nota_filme = int(input())
            nota += nota_filme