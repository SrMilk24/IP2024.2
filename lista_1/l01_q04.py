vote_1 = input()
country_1 = input()

vote_2 = input()
country_2 = input()

registration_1 = True
registration_2 = True
rodri_points = 0
vini_point = 0

if(vote_1 == 'rodri'):
    if(country_1 == 'Espanha'):
        registration_1 = False
    else:
        rodri_points += 1
elif(vote_1 == 'vinijr'):
    if(country_1 == 'Brasil'):
        registration_1 = False
    else:
        vini_point += 1
        
if(vote_2 == 'rodri'):
    if(country_2 == 'Espanha'):
        registration_2 = False
    else:
        rodri_points += 1
elif(vote_2 == 'vinijr'):
    if(country_2 == 'Brasil'):
        registration_2 = False
    else:
        vini_point += 1
        
if(registration_1 == False):
    print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    if(registration_2 == False):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')
else:
    print('Voto registrado!')
    if(registration_2 == False):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')
print('Votos válidos para rodri: {}'.format(rodri_points))
print('Votos válidos para vinijr: {}'.format(vini_point))