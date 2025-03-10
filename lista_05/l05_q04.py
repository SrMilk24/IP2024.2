def encontrar_senha(lista, K):

    def backtrack(ordem, sublista_atual, soma_atual):
        if soma_atual == K and len(sublista_atual) >= 4:
            return sublista_atual
        if ordem >= len(lista):
            return None
        
        resultado_com_atual = backtrack(ordem + 1, sublista_atual + [lista[ordem]], soma_atual + lista[ordem])

        resultado_sem_atual = backtrack(ordem + 1, sublista_atual, soma_atual)

        if resultado_com_atual is not None and resultado_sem_atual is not None:
            return resultado_com_atual if len(resultado_com_atual) > len(resultado_sem_atual) else resultado_sem_atual
        elif resultado_com_atual is not None:
            return resultado_com_atual
        else:
            return resultado_sem_atual
    return backtrack(0, [], 0)


def validar_senha(senha):

    return len(senha) >= 4 and '0' not in senha

def formata_senha(lista):
    senha = ""
    for num in lista:
        num_str = str(abs(num))
        for digito in num_str:
            if digito != '0':
                senha += digito
    return senha


entrada = int(input())

for porta in range(1, entrada + 1):

    num_portas = input()
    lista = [int(x) for x in num_portas.replace(" ", "").split(",")]

    K = int(input())
    
    sublista = encontrar_senha(lista, K)
    
    if sublista is not None:
        senha = formata_senha(sublista)
        if validar_senha(senha):
                print(f"A senha da porta {porta} é: {senha}")
        else:
            print("Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!")
            break 
    else:
        print("Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!")
        break 
