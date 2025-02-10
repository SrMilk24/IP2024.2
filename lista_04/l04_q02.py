def calcular_taxa(taxa, piltover, zaun):

    populacoes = piltover + zaun
    taxa_por_pessoa = taxa / populacoes

    return taxa_por_pessoa

    
    
def distribuir_recursos(taxa_por_pessoa, taxa, situacao, zaun):
    distribuicao = 0
    if situacao == "desastre":
        distribuicao = taxa * 0.9
        return distribuicao
    elif  situacao == "crise":
        distribuicao = taxa * 0.8
        return distribuicao
    elif situacao == "critica":
        distribuicao = taxa * 0.7
        return distribuicao
    elif situacao == "normal":
        distribuicao = taxa * 0.6
        return distribuicao
    elif situacao == "tranquilo":
        distribuicao = taxa * 0.5
        return distribuicao
    else:
        distribuicao = taxa_por_pessoa * (zaun)
        return distribuicao
    

def mensagem(distribuicao, taxa):
    piltover = taxa - distribuicao
    print(f"Foi decidido que será {piltover:.1f} para Piltover e {distribuicao:.1f} para Zaun!")
    razao = distribuicao / piltover

    if razao >= 0.9:
        print("Zaun receberá uma bolada!!!")
    elif razao >= 0.8 and razao < 0.9:
        print("Quase que Piltover ficava sem nada, pobrezinhos...")
    elif razao >= 0.7 and razao < 0.8:
        print("O negócio vai ficar bom para Zaun hein.")
    elif razao >= 0.6 and razao < 0.7:
        print("Parece que Zaun ainda precisa de ajuda.")
    elif razao >= 0.5 and razao < 0.6:
        print("As coisas estão meio apertadas para Zaun.")
    elif razao < 0.5:
        print("A situação não está muito favorável para Zaun...")

taxa = int(input())
piltover = int(input())
zaun = int(input())
situacao = input()

calculo_taxa = calcular_taxa(taxa, piltover, zaun)
distribuicao = distribuir_recursos(calculo_taxa, taxa, situacao, zaun)
mensagem(distribuicao, taxa)

