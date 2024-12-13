tamanho = int(input())

altura = (tamanho * 2) - 1
print('{}{}{}'.format('⠀'*(altura//2), '*', '⠀'*(altura//2))) #Its Working

for x in range(1, tamanho+1):
    print('{}*{}*{}'.format('⠀'*(tamanho-x-1),'⠀'*(x), '⠀'*(tamanho-(x+1))))
meio = '{}'.format('*⠀'*tamanho)
meio = meio[:-1]
print(meio)

for x in range(tamanho-1, 0, -1):
    print('{}{}{}'.format('⠀'*(tamanho-x),'*''⠀'*(x-1), '⠀'*((tamanho-(x+1)))))
