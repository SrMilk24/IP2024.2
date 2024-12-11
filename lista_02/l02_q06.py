quant_renas = int(input())
quant_voltas = int(input())
renas = ''

nome_primeira = ''
nome_segunda = ''
nome_terceira = ''

ponto_primeira = 0
ponto_segunda = 0
ponto_terceira = 0


if(quant_renas < 3):
    print('Meu senhor, com essa quantidade de rena vai ter que entregar os presentes a pé, viu?!')
elif(quant_renas == 3):
    
    for x in range(0, quant_renas):
        nome = input()
        if(x == 0):
            nome_primeira = nome
        elif(x == 1):
            nome_segunda = nome
        elif(x == 2):
            nome_terceira = nome
    print('Como só temos 3 renas aptas pro serviço esse ano, não adianta muito querer ficar escolhendo')
    print('As três únicas renas capazes de participar esse ano são:')
    print('{}, {} e {}.'.format(nome_primeira, nome_segunda, nome_terceira))
    print('Não haverá teste de desempenho entre elas!')
else:
    for x in range(quant_renas):
        ponto = 0
        nome = input()
        for x in nome:
            if(x.upper() == 'A'):
                ponto += 8
            elif(x.upper() == 'E'):
                ponto += 5
            elif(x.upper() == 'I'):
                ponto += 4
            elif(x.upper() == 'O'):
                ponto += 3
            elif(x.upper() == 'U'):
                ponto += 2

        ponto_final = ponto

        for x in range(1, quant_voltas+1):
            mod = ponto % x
            if(mod == 0):
                ponto_final += 2
            elif(mod % 2 == 0):
                ponto_final += 1
        
        if(ponto_final > ponto_primeira) :
            ponto_terceira = ponto_segunda
            nome_terceira = nome_segunda
            ponto_segunda = ponto_primeira
            nome_segunda = nome_primeira
            ponto_primeira = ponto_final
            nome_primeira = nome
        elif(ponto_final > ponto_segunda):
            ponto_terceira = ponto_segunda
            nome_terceira = nome_segunda
            ponto_segunda = ponto_final
            nome_segunda = nome
        elif(ponto_final > ponto_terceira):
            ponto_terceira = ponto_final
            nome_terceira = nome
    
    print('As três renas mais atléticas pra temporada de Natal são:')
    print('{}, {} e {}.'.format(nome_primeira, nome_segunda, nome_terceira))