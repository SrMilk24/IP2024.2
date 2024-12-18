tamanho = int(input())

for x in range(1, tamanho):
    print('⠀' * (tamanho - x), end='')
    print('*', end='')
    if x > 1:
        print('⠀' * (2 * x - 3), end='')
        print('*', end='')

    print('⠀' * (tamanho - x))

meio = '{}'.format('*⠀'*tamanho)
meio = meio[:-1]
print(meio)

for i in range(tamanho - 1, 0, -1):
    print('⠀' * (tamanho - i), end='')
    print('*', end='')

    if i > 1:
        print('⠀' * (2 * i - 3), end='')
        print('*', end='')
    
    print('⠀' * (tamanho - i))
