personagens_da_serie = ["Jinx", "Vi", "Heimerdinger", "Ekko", "Caitlyn", "Jayce", "Viktor", "Silco", "Claggor", "Vander", "Mylo"]
tamanho_lista = int(input())
personagens = [""] * tamanho_lista
lista_preenchida = False

def adicionar(lista, persona):
    for indice in range(len(lista)):
        if lista[indice] == "":
            lista[indice] = persona
            break
    print(f"Personagem {persona} adicionado")    
    return lista

def remover(lista, persona):
    for indice in range(len(lista)):
        if lista[indice] == persona:
            lista[indice] = ""
    print(f"Personagem {persona} removido")    

    for indice in range(len(lista)-1):
        if lista[indice] == "" and lista[indice+1] != "":
            lista[indice] = lista[indice+1]
            lista[indice+1] = ""
    return lista

def validar_resultado(personagens_serie, meus_personagens):
    validacao = all(personagem in personagens_serie for personagem in meus_personagens)
    
    return validacao

while not lista_preenchida:
    acao = input()
    personagem = input()
    
    if acao == "Adiciona":
        adicionar(personagens, personagem)
        
    elif acao == "Remove":
        remover(personagens, personagem)
        
    count = 0
    
    for x in personagens:
        if x != "":
            count += 1
    
    if count == len(personagens):
        lista_preenchida = True
        
        
print("Lista final de personagens:")
for personagem in personagens:
    print(personagem)

validacao = validar_resultado(personagens_da_serie, personagens)
    
if validacao:
    print("Parabéns!! Você conseguiu acertar todos os nomes.")
    print("UAUUU! Acho que estamos preparados para ver a segunda temporada.")
else:
    print("Infelizmente você perdeu...")
    print("Eita... Vamos precisar assistir novamente.")