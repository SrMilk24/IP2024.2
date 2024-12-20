print('Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!')
print('Quantos materiais mágicos estão trancados nos baús?')
print('Vamos começar desbloqueando os materiais!')
qtd_materiais = int(input())
encontradas = 0
for x in range(qtd_materiais):
    chute = ''
    acertos = 0
    nome_item = input()
    print('Material {} de {}'.format(x+1, qtd_materiais))
    print('Senha mágica:',end = ' ')
    for letra in nome_item:
        if letra.isalpha():
                print('_',end='')
                if letra not in chute:
                    chute += letra
        if letra == ' ':
             print(' ',end= '')
    if len(nome_item) <= 5:
        tentativa = 7
    elif len(nome_item) <= 10:
        tentativa = 9
    elif len(nome_item) <= 13:
        tentativa = 13
    else:
        tentativa = 16
    temp = ''
    repetida =''
    for y in range(tentativa):
        vezes = 0  
        if y == 0:
            letra = input('\n')
        else:
            letra = input()
        if letra not in temp:
            if letra in chute:
                vezes = 0
                temp += letra
                for a in (nome_item):
                    if letra == a:
                        vezes +=1
                if vezes == 1:
                    print('Acertamos uma letra! Ela aparece um total de 1 vez na senha')
                    acertos += 1
                if vezes > 1:
                    print('Acertamos uma letra! Ela aparece um total de {} vezes na senha'.format(vezes))
                    acertos += 1
                chute.replace(letra,'')
            else:
                if y != (tentativa -1):
                    print('Erramos a letra! Porém ainda temos mais tentativas.')    
                else:
                    print('Infelizmente não conseguimos descobrir a senha.')
            if acertos == len(chute):
                print("Parabéns! Você desbloqueou o material mágico '{}'!".format(nome_item))
                encontradas += 1
                break
        else:
            repetida += letra
            
        if letra in repetida:
            if acertos != len(chute):
                if y == (tentativa - 1):
                    print('Infelizmente não conseguimos descobrir a senha.')       
                                     
    if acertos != len(chute):
        print("Você não conseguiu desbloquear o material. O nome correto era '{}'.".format(nome_item))
                
print('Você desbloqueou {} de {} materiais mágicos!'.format(encontradas, qtd_materiais))
print('Os duendes precisam decifrar os códigos perdidos para montar o trenó!')

print(f'Quantas partes o trenó possui?')
qtd_partes = int(input())
certo = 0
for x in range(qtd_partes):
    print('Parte {} de {}'.format(x+1, qtd_partes))
    numeros = input()+' '
    num = ''
    maior = 0
    menor = 10000000000
    for y in numeros:
        if y.isnumeric():
            num += y
        else:
            if int(num) < menor:
                menor = int(num)
            if int(num) > maior:
                maior = int(num)
            num = ''
    print('Dica: O menor número é {} e o maior número é {}.'.format(menor, maior))
    print('Descubra o número mágico (soma de {} e {})'.format(menor, maior))
    exito = 0
    for i in range(2):
        soma = int(input())
        if soma == (menor+maior):
            print('Você decifrou o código da parte {}! O trenó está mais próximo de ficar completo!'.format(x+1))
            exito +=1
            certo += 1
            break
        else:
            if i ==0:
                print('Número incorreto! Tente novamente.')
                print('Descubra o número mágico (soma de {} e {})'.format(menor, maior))
            else:
                print('Número incorreto! Tente novamente.')
    if exito == 0:
        print('Você não conseguiu decifrar o código. O número mágico era {}.'.format(menor + maior))
print('Você montou {} de {} partes do trenó!'.format(certo, qtd_partes))
if certo == qtd_partes:
    print(f'Parabéns! O trenó está completo e pronto para voar!')
else:
    if certo >= (qtd_partes//2):
        print('Bom trabalho! O trenó quase ficou completo!')
    else:
        print('Parece que o trenó ficou incompleto. Tente novamente na próxima missão!')