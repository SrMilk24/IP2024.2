def calcula_energia(tempo, potencia, ineficiencia, preco):
    energia_inicial = potencia * tempo
    energia_inicial += energia_inicial * ineficiencia
    consumo_total = energia_inicial
    return consumo_total