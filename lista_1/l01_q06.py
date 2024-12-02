tf_1 = float(input())
tv_1 = float(input())
tf_2 = float(input())
tv_2 = float(input())

emp_1 = 'Empresa 1'
emp_2 = 'Empresa 2'



if(tv_1 == tv_2):
    if(tf_1 == tf_2):
        print('As duas empresas possuem o mesmo preço sempre!')
    elif(tf_1 > tf_2):
        print('A {} é sempre a melhor opção!'.format(emp_2))
    else:
        print('A {} é sempre a melhor opção!'.format(emp_1))
else:
    k = (tf_2 - tf_1) / (tv_1 - tv_2)
    if(k <= 0):
        if(tv_1 < tv_2):
            print('A {} é sempre a melhor opção!'.format(emp_1))
        elif(tv_1 > tv_2):
            print('A {} é sempre a melhor opção!'.format(emp_2))
    else:
        if(tv_1 > tv_2):
            print('{} é mais barata para distâncias menores que {:.2f} km, ambas têm o mesmo preço para {:.2f} km e a {} é mais barata para distâncias maiores que {:.2f} km.'.format(emp_1, k, k, emp_2, k))
        else:
            print('{} é mais barata para distâncias menores que {:.2f} km, ambas têm o mesmo preço para {:.2f} km e a {} é mais barata para distâncias maiores que {:.2f} km.'.format(emp_2, k, k, emp_1, k))
        