def desmembrar_expressao(expressao):
    termos = []
    termo_atual = ""

    for caractere in expressao:
       
        if (caractere == '+' or caractere == '-') and termo_atual:
            termos.append(termo_atual)
            termo_atual = caractere 
        else:
            termo_atual += caractere 
    
    if termo_atual:
        termos.append(termo_atual)

    return termos

def derivar_monomio(monomio):
    
    if 'x' in monomio:
        if '^' in monomio:
            coeficiente, expoente = monomio.split('x^')
            coeficiente = int(coeficiente) if coeficiente not in ['+', '-', ''] else int(coeficiente + '1')
            expoente = int(expoente)
            
            novo_coeficiente = coeficiente * expoente
            novo_expoente = expoente - 1

            
            if novo_coeficiente == 0:
                return "0"
            elif novo_expoente == 0:
                return str(novo_coeficiente)
            elif novo_expoente == 1:
                return f"{novo_coeficiente}x"
            else:
                return f"{novo_coeficiente}x^{novo_expoente}"
        else:
            coeficiente = monomio.replace('x', '')
            coeficiente = int(coeficiente) if coeficiente not in ['+', '-', ''] else int(coeficiente + '1')
            return str(coeficiente) 
    else:
        return "0"

def calcula_derivada(expressao, ordem):
    if ordem == 0:
        return expressao  
    
    lista_termos = desmembrar_expressao(expressao)
    nova_expressao = ""

    for i, monomio in enumerate(lista_termos):
        termo_derivado = derivar_monomio(monomio)
        if termo_derivado != "0": 
            if i > 0 and termo_derivado[0] != '-':
                nova_expressao += "+"
            nova_expressao += termo_derivado

    if not nova_expressao:
        return "0"

    return calcula_derivada(nova_expressao, ordem - 1)


polinomio = input()
ordem = int(input())
novo_polinomio = calcula_derivada(polinomio, ordem)

print(f"A derivada de ordem {ordem} da função {polinomio} é:")
print(novo_polinomio)

