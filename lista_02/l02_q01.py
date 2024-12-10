bonecos = 0
videogame = 0
bicicletas = 0
outros = 0

condicao = True

while(condicao):
    entrada = input()

    if(entrada == 'FIM'):
        condicao = False
        break
    elif(entrada == 'Boneco'):
        bonecos += 1
        print('Mais um presente saindo!')
    elif(entrada == 'Videogame'):
        videogame += 1
        print('Mais um presente saindo!')
    elif(entrada == 'Bicicleta'):
        bicicletas += 1
        print('Mais um presente saindo!')
    else:
        outros += 1
        print('Esse presente não está sendo fabricado nesse momento')

print('Vamos agora ao relatório dos presentes!\n')

total = bonecos + videogame + bicicletas + outros

print('Boneco - {} unidades - {:.2f}%'.format(bonecos, (bonecos/total)*100))
print('Videogame - {} unidades - {:.2f}%'.format(videogame, (videogame/total)*100))
print('Bicicleta - {} unidades - {:.2f}%'.format(bicicletas, (bicicletas/total)*100))
print('Outros - {} unidades - {:.2f}%'.format(outros, (outros/total)*100))

if(outros == 0):
    print('A demanda está muito alta! Teremos que fazer mais uma fábrica!')
else:
    if((outros/total)*100 > 50):
        print('Parece que o Papai Noel terá que fechar a fábrica :(')
    elif((bonecos/total)*100 > 50 or (bicicletas/total)*100 > 50 or (videogame/total)*100 > 50):
        if((bonecos/total)*100 > 50):
            print('Boneco está sendo muito desejado! A fábrica terá que ser expandida!')
        elif((videogame/total)*100 > 50):
            print('Videogame está sendo muito desejado! A fábrica terá que ser expandida!')
        elif((bicicletas/total)*100 > 50):
            print('Bicicleta está sendo muito desejado! A fábrica terá que ser expandida!')
    else:
        print('A fábrica está cumprindo seu papel, porém não precisa ser expandida')
