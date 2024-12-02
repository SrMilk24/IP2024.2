proj_desempenho = input()
proj_gols = int(input())
desenpenho_final = input()
pontos = 0
pontos_parciais = 0

print('Está aberta a revisão da premiação!')

if(proj_desempenho == 'Decepção'):
    pontos_parciais += 100
    print('Parece que não estão colocando muitas expectativas para a temporada do nosso Vini Jr., não... Sempre subestimado!')
elif(proj_desempenho == 'Oscilação'):
    pontos_parciais += 200
    print('Os jornalistas acreditam que Vini Jr. terá atuações irregulares nesta temporada, mas quem sabe ele não supera as projeções?')
elif(proj_desempenho == 'Importante'):
    pontos_parciais += 300
    print('Em um elenco tão forte como o do Real Madrid, é normal as atenções serem divididas mesmo. O que importa é que ele não vai se esconder!')
elif(proj_desempenho == 'Estrela'):
    pontos_parciais += 400
    print('Vini Jr. será o craque do Real Madrid na temporada de 2023/2024! Será que ele consegue a tão sonhada Bola de Ouro?')
    
pontos = ((proj_gols * 2) + (pontos_parciais / 2))
pontos += pontos_parciais

if(desenpenho_final == 'Decepção'):
    pontos += 150
    print('Vini Jr. decepcionou os torcedores em 2024, não era o ano dele.')
elif(desenpenho_final == 'Oscilação'):
    pontos += 250
    print('A temporada não foi das melhores, mas Vini Jr. conseguiu mostrar, em alguns momentos, que ele de fato é craque.')
elif(desenpenho_final == 'Importante'):
    pontos += 350
    print('Vini Jr. mostrou que é crucial para o elenco do Real Madrid e da Seleção.')
elif(desenpenho_final == 'Estrela'):
    pontos += 500
    print('Ele é demais! Herói do título da Champions, ele conseguiu mostrar ao mundo que é uma estrela do futebol!')
    
if(proj_desempenho == 'Estrela'):
    if(desenpenho_final == 'Estrela'):
        pontos += 100
        print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
    else:
        print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif(proj_desempenho == 'Importante'):
    if(desenpenho_final == 'Estrela'):
        pontos += 300
        print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
    elif(desenpenho_final == 'Importante'):
        pontos += 100
        print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
    else:
        print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif(proj_desempenho == 'Oscilação'):
    if(desenpenho_final == 'Estrela' or desenpenho_final == 'Importante'):
        pontos += 300
        print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
    elif(desenpenho_final == 'Oscilação'):
        pontos += 100
        print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
    else:
        print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif(proj_desempenho == 'Decepção'):
    if(desenpenho_final == 'Estrela' or desenpenho_final == 'Importante' or desenpenho_final == 'Oscilação'):
        pontos += 300
        print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
    elif(desenpenho_final == 'Decepção'):
        pontos += 100
        print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
    else:
        print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
        
if(proj_gols < 37):
    print('Vini Jr. foi muito decisivo para sua equipe este ano, superando sua previsão de participações em gols!')
else:
    print('É, Vini Jr. não conseguiu provar que estavam errados, mas ainda assim ele segue vivo para a premiação.')
    
pontos = int(pontos)

if(pontos > 1170):
    print('O mundo estava certo! Com {} pontos, Vini Malvadeza é o verdadeiro melhor do mundo! Chega dessa injustiça!'.format(pontos))
elif(pontos == 1170):
    print('Empate! Vamos ao critério de desempate.')
    if(desenpenho_final == 'Estrela'):
        print('Foi uma premiação apertada, mas a justiça foi feita! Vini Jr. é, sim, o melhor do mundo.')
    else:
        print('Bom, é isso. Ainda tivemos esperanças, mas o Rodri é, mesmo, o Bola de Ouro.')
else:
    print('Infelizmente, teremos que nos contentar com o Rodri sendo o melhor do mundo mesmo.')