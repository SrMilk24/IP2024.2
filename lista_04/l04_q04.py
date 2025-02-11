alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def descifra_ataque(nome_alvo, precisao, resistencia, poder, formula, deslocamento):
    dano = precisao * (poder / resistencia) * formula



num_ataques = int(input())

if num_ataques == 0:
    print("Piltover em paz... por enquanto.")