def melhor_empresa(taxa_fixa_1, taxa_variavel_1, taxa_fixa_2, taxa_variavel_2):
    # Verificando quando as empresas possuem a mesma taxa variável
    if taxa_variavel_1 == taxa_variavel_2:
        if taxa_fixa_1 < taxa_fixa_2:
            return "A Empresa 1 é sempre a melhor opção!"
        elif taxa_fixa_1 > taxa_fixa_2:
            return "A Empresa 2 é sempre a melhor opção!"
        else:
            return "As duas empresas possuem o mesmo preço sempre!"
    
    # Calcular a distância crítica k onde os preços se igualam
    k = (taxa_fixa_2 - taxa_fixa_1) / (taxa_variavel_1 - taxa_variavel_2)
    
    # Verificar se a distância crítica k é positiva
    if k <= 0:
        if taxa_variavel_1 < taxa_variavel_2:
            return "A Empresa 1 é sempre a melhor opção!"
        elif taxa_variavel_1 > taxa_variavel_2:
            return "A Empresa 2 é sempre a melhor opção!"
        else:
            return "As duas empresas possuem o mesmo preço sempre!"
    
    # Se k é positiva, então temos a situação com distâncias críticas
    return f"Empresa 1 é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a Empresa 2 é mais barata para distâncias maiores que {k:.2f} km."

# Testando a função com alguns valores de entrada
taxa_fixa_1 = 10
taxa_variavel_1 = 5
taxa_fixa_2 = 15
taxa_variavel_2 = 3

print(melhor_empresa(taxa_fixa_1, taxa_variavel_1, taxa_fixa_2, taxa_variavel_2))