performance_expectation = input()
gols = int(input())
final_performance = input()
points = 0
better = False
same = False

if(performance_expectation == 'Decepção'):
    points += 100
elif(performance_expectation == 'Oscilação'):
    points += 200
elif(performance_expectation == 'Importante'):
    points += 300
elif(performance_expectation == 'Estrela'):
    points += 400

points += (gols * 2) + (points / 2)

if(final_performance == 'Decepção'):
    points += 150
elif(final_performance == 'Oscilação'):
    points += 250
elif(final_performance == 'Importante'):
    points += 350
elif(final_performance == 'Estrela'):
    points += 500

if(final_performance == 'Estrela'):
    if(performance_expectation != 'Estrela'):
        points += 300
        better = True
    else:
        points += 100
        same = True
       
elif(final_performance == 'Importante'):
    if(performance_expectation == 'Estrela'):
        points = points
        better = True
    elif(performance_expectation == 'Importante'):
        points += 100
        same = True
    else:
        points += 300
        
elif(final_performance == 'Oscilação'):
    if(performance_expectation == 'Estrela' or performance_expectation == 'Importante'):
        points = points
        better = True
    elif(performance_expectation == 'Oscilação'):
        points += 100
        same = True
    else:
        points += 300

elif(final_performance == 'Decepção'):
    if(performance_expectation == 'Decepção'):
        points += 100
        same = True

print('Está aberta a revisão da premiação!')

if(performance_expectation == 'Decepção'):
    print('Parece que não estão colocando muitas expectativas para a temporada do nosso Vini Jr., não... Sempre subestimado!')
elif(performance_expectation == 'Oscilação'):
    print('Os jornalistas acreditam que Vini Jr. terá atuações irregulares nesta temporada, mas quem sabe ele não supera as projeções?')
elif(performance_expectation == 'Importante'):
    print('Em um elenco tão forte como o do Real Madrid, é normal as atenções serem divididas mesmo. O que importa é que ele não vai se esconder!')
elif(performance_expectation == 'Estrela'):
    print('Vini Jr. será o craque do Real Madrid na temporada de 2023/2024! Será que ele consegue a tão sonhada Bola de Ouro?')

if(final_performance == 'Decepção'):
    print('Vini Jr. decepcionou os torcedores em 2024, não era o ano dele.')
elif(final_performance == 'Oscilação'):
    print('A temporada não foi das melhores, mas Vini Jr. conseguiu mostrar, em alguns momentos, que ele de fato é craque.')
elif(final_performance == 'Importante'):
    print('Vini Jr. mostrou que é crucial para o elenco do Real Madrid e da Seleção.')
elif(final_performance == 'Estrela'):
    print('Ele é demais! Herói do título da Champions, ele conseguiu mostrar ao mundo que é uma estrela do futebol!')

if(better == True):
    print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
elif(same == True):
    print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
else:
    print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')

if(gols < 37):
    print('Vini Jr. foi muito decisivo para sua equipe este ano, superando sua previsão de participações em gols!')
else:
    print('É, Vini Jr. não conseguiu provar que estavam errados, mas ainda assim ele segue vivo para a premiação.')

if(points > 1170):
    print('O mundo estava certo! Com {} pontos, Vini Malvadeza é o verdadeiro melhor do mundo! Chega dessa injustiça!'.format(int(points)))
elif(points < 1170):
    print('Infelizmente, teremos que nos contentar com o Rodri sendo o melhor do mundo mesmo.')
else:
    print('Empate! Vamos ao critério de desempate.')
    if(final_performance == 'Estrela'):
        print('Foi uma premiação apertada, mas a justiça foi feita! Vini Jr. é, sim, o melhor do mundo.')
    else:
        print('Bom, é isso. Ainda tivemos esperanças, mas o Rodri é, mesmo, o Bola de Ouro.')

