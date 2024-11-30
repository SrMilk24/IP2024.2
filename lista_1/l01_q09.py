suspect_1 = input()
dist_susp_1 = int(input())
suspect_2 = input()
dist_susp_2 = int(input())

distance = (dist_susp_1 ** 2 + dist_susp_2 ** 2) ** 0.5

if(distance % 2 == 0):
    print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(suspect_1, suspect_2))
else:
    category_1 = input()
    category_2 = input()

    if(category_1 == 'Fã' and category_2 == 'Fã'):
        if(dist_susp_1 % 2 == 0) and (dist_susp_1 % 3 == 0) and (dist_susp_2 % 2 == 0) and (dist_susp_2 % 3 == 0):
            print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(suspect_1, suspect_2))
        elif(dist_susp_1 % 2 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_2))
        elif(dist_susp_2 % 3 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_1))
            
    elif(category_1 == 'Jogador') and (category_2 == 'Jogador'):
        if(dist_susp_1 % 2 == 0) and (dist_susp_1 % 5 == 0) and (dist_susp_2 % 2 == 0) and (dist_susp_2 % 5 == 0):
            print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(suspect_1, suspect_2))
        elif(dist_susp_1 % 2 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_2))
        elif(dist_susp_2 % 5 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_1))
        

    elif(category_1 == 'Jornalista') and (category_2 == 'Jornalista'):
        if(dist_susp_1 % 3 == 0) and (dist_susp_1 % 5 == 0) and (dist_susp_2 % 3 == 0) and (dist_susp_2 % 5 == 0):
            print('{} e {} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!'.format(suspect_1, suspect_2))
        elif(dist_susp_1 % 3 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_2))
        elif(dist_susp_2 % 5 == 0):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_1))
            
    else:
        if(dist_susp_1 == dist_susp_2):
            print('{} e {} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!'.format(suspect_1, suspect_2))
        elif(dist_susp_1 > dist_susp_2):
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_2))
        else:
            print('{} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!'.format(suspect_1))
