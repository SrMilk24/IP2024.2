def add_lider(lideres, nome, cargo, cidade, data):
    lideres[nome] = {
        'cargo': cargo,
        'cidade': cidade,
        'data': data
    }

    return lideres

def add_acontecimentos(acontecimentos, acontecimento, data, local):
    acontecimentos[acontecimento] = {
        'data': data,
        'local': local
    }

    return acontecimentos

def get_lideres(lideres):
    if lideres:
        print("Consegui encontrar os seguintes líderes da Revolução Pernambucana de 1817:")
        for lider in lideres:
            print(f"{lider}:")
            print(f"- Cargo/Papel: {lideres[lider]['cargo']}")
            print(f"- Cidade de Origem: {lideres[lider]['cidade']}")
            print(f"- Data de Nascimento: {lideres[lider]['data']}")
    else:
        print("Aff, pelo jeito nessa época não tinha LinkedIn pra facilitar encontrar os tais líderes dessa tal Revolução... Desisto.")
    print()
    return

def get_acontecimentos(acontecimentos):
    if acontecimentos:
        print("Vivenciei os seguintes acontecimentos históricos da Revolução Pernambucana de 1817:")
        for acontecimento in acontecimentos:
            local = acontecimentos[acontecimento]['local']
            data = acontecimentos[acontecimento]['data']
            print(f"({data}): {acontecimento}, {local}")
    else:
        print("Ter que ler todos esses jornais não é legal, e ainda não encontrei nenhum acontecimento... saudade do Pernambuco Extraordinário pra me manter informado.")
    return

condicional = ""
lideres = {}
acontecimentos = {}
while condicional != "FIM":
    entrada = input()

    if entrada == "FIM":
        condicional = "FIM"
    elif entrada == "REGISTRAR LÍDER":
        nome = input()
        cargo = input()
        cidade = input()
        data = input()
        add_lider(lideres, nome, cargo, cidade, data)
    elif entrada == "REGISTRAR ACONTECIMENTO":
        data = input()
        acontecimento = input()
        local = input()
        add_acontecimentos(acontecimentos, acontecimento, data, local)

get_lideres(lideres)
get_acontecimentos(acontecimentos)

if lideres and acontecimentos:
    print()
    print("Pronto, agora CIn tô preparado pra lutar e tornar Pernambuco o melhor país em linha reta do mundo!!!")
