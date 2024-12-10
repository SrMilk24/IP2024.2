nome_sus1 = input()
distancia_sus1 = int(input())
nome_sus2 = input()
distancia_sus2 = int(input())

distancia = (((distancia_sus1 ** 2) + (distancia_sus2 ** 2)) ** 0.5)


if(distancia % 2 == 0):
    print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(nome_sus1, nome_sus2))
else:
    categoria1 = input()
    categoria2 = input()
    
    if(categoria1 == categoria2):
        if(categoria1 == 'Fã'):
            if(distancia_sus1 % 2 == 0 and distancia_sus1 % 3 == 0 and distancia_sus2 % 2 == 0 and distancia_sus2 % 3 == 0):
                print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(nome_sus1, nome_sus2))
            else:
                if(distancia_sus1 % 2 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus2))
                elif(distancia_sus2 % 3 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus1))
                else:
                    print('{} e {} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!'.format(nome_sus1, nome_sus2))
            
        elif(categoria1 == 'Jogador'):
            if(distancia_sus1 % 2 == 0 and distancia_sus1 % 5 == 0 and distancia_sus2 % 2 == 0 and distancia_sus2 % 5 == 0):
                print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(nome_sus1, nome_sus2))
            else:
                if(distancia_sus1 % 2 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus2))
                elif(distancia_sus2 % 5 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus1))
                else:
                    print('{} e {} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!'.format(nome_sus1, nome_sus2))
        elif(categoria1 == 'Jornalista'):
            if(distancia_sus1 % 3 == 0 and distancia_sus1 % 5 == 0 and distancia_sus2 % 3 == 0 and distancia_sus2 % 5 == 0):
                print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(nome_sus1, nome_sus2))
            else:
                if(distancia_sus1 % 3 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus2))
                elif(distancia_sus2 % 5 == 0):
                    print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus1))
                else:
                    print('{} e {} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!'.format(nome_sus1, nome_sus2))
    else:
        if(distancia_sus1 == distancia_sus2):
            print('{} e {} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!'.format(nome_sus1, nome_sus2))
        elif(distancia_sus1 > distancia_sus2):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus2))
        else:
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(nome_sus1))