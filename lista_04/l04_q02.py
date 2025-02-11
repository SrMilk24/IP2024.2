def calcular_taxa(taxa, piltover, zaun):
    populacoes = piltover + zaun
    taxa_por_pessoa = taxa / populacoes
    return taxa_por_pessoa

def distribuir_recursos(taxa_por_pessoa, taxa, situacao, zaun):
    if situacao == "desastre":
        return taxa * 0.9
    elif situacao == "crise":
        return taxa * 0.8
    elif situacao == "critica":
        return taxa * 0.7
    elif situacao == "normal":
        return taxa * 0.6
    elif situacao == "tranquilo":
        return taxa * 0.5
    else:
        return taxa_por_pessoa * zaun

def mensagem(distribuicao, taxa):
    piltover = taxa - distribuicao
    print(f"Foi decidido que será {piltover:.1f} para Piltover e {distribuicao:.1f} para Zaun!")
    if piltover == 0:
        print("Zaun receberá uma bolada!!!")
        return
    
    razao = distribuicao / piltover
    
    if razao >= 0.9:
        print("Zaun receberá uma bolada!!!")
    elif 0.8 <= razao < 0.9:
        print("Quase que Piltover ficava sem nada, pobrezinhos...")
    elif 0.7 <= razao < 0.8:
        print("O negócio vai ficar bom para Zaun hein.")
    elif 0.6 <= razao < 0.7:
        print("Parece que Zaun ainda precisa de ajuda.")
    elif 0.5 <= razao < 0.6:
        print("As coisas estão meio apertadas para Zaun.")
    else:
        print("A situação não está muito favorável para Zaun...")

taxa = int(input())
piltover = int(input())
zaun = int(input())
situacao = input()

calculo_taxa = calcular_taxa(taxa, piltover, zaun)

distribuicao = distribuir_recursos(calculo_taxa, taxa, situacao, zaun)

mensagem(distribuicao, taxa)