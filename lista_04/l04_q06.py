numero_estados = int(input())
#estado_aceitacao = input()
numero_binarios = int(input())


def gera_estados(numero_estados):
    estados = []
    for x in range(numero_estados):
        estados.append(f'q{x+1}')

    return estados

def gera_conexoes(estados):
    conexoes = []
    for _ in range(estados):
        conexoes.append(input())

    return conexoes
