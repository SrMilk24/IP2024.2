condicao = True
contador = 0
tempo_total = 0
distancia_total = 0
print('Boa noite, Papai Noel! Feliz Natal!')
while(condicao):

    entrada = input()
    if(entrada == 'As renas ainda estão cheias de energia para entregar presentes para mais crianças!'):
        nome = input()
        distancia = float(input())
        medida = input()

        
        contador += 1

        if(medida == 'quilometros'):
            distancia_total += distancia
            tempo = (distancia / 80)
            tempo_min = tempo * 60
            tempo_total += tempo_min
            if(tempo_min >= 60):
                print('Querido Papai Noel, você levará {} horas para chegar até a casa de {}!'.format(int(tempo), nome))
            elif(tempo_min >= 1 and tempo_min < 60):
                print('Querido Papai Noel, você levará {} minutos para chegar até a casa de {}!'.format(int(tempo_min), nome))
            else:
                print('Querido Papai Noel, você chegará em breve na casa de {}!'.format(nome))
        elif(medida == 'metros'):
            distancia_total += distancia/1000
            tempo = ((distancia / 1000) / 80)
            tempo_min = tempo * 60
            tempo_total += tempo_min
            if(tempo_min >= 60):
                print('Querido Papai Noel, você levará {} horas para chegar até a casa de {}!'.format(int(tempo), nome))
            elif(tempo_min >= 1 and tempo_min < 60):
                print('Querido Papai Noel, você levará {} minutos para chegar até a casa de {}!'.format(int(tempo_min), nome))
            else:
                print('Querido Papai Noel, você chegará em breve na casa de {}!'.format(nome))
    elif(entrada == 'Já está amanhecendo, preciso voltar ao Polo Norte! HO HO HO!'):
        condicao = False
        break

print('Querido Papai Noel, a noite de natal foi um sucesso! Você levou apenas {:.2f} horas para entregar todos os {} presentes'.format(distancia_total/80, contador))