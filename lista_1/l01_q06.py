tf_1 = float(input())
tv_1 = float(input())
tf_2 = float(input())
tv_2 = float(input())

k = 1

if(tv_1 != tv_2):
    k = (tf_2 - tf_1) / (tv_1 - tv_2)

if(tv_1 == tv_2):
    if(tf_1 > tf_2):
        print('A Empresa 1 é sempre a melhor opção!')
    elif(tf_2 > tf_1):
        print('A Empresa 2 é sempre a melhor opção!')
    else:
        print('As duas empresas possuem o mesmo preço sempre!')
elif (k <= 0):
    if(tv_1 < tv_2):
        print('A Empresa 1 é sempre a melhor opção!')
    elif(tv_1 > tv_2):
        print('A Empresa 2 é sempre a melhor opção!')
    else:
        print('As duas empresas possuem o mesmo preço sempre!')
else:
    print('Empresa 1 é mais barata para distâncias menores que {:.2f} km, ambas têm o mesmo preço para {:.2f} km e a Empresa 2 é mais barata para distâncias maiores que {:.2f} km.'.format(k, k, k))