def analisar_numero(numero):
    # Verifica se o número é positivo, negativo ou zero
    if numero > 0:
        sinal = "Positivo"
    elif numero < 0:
        sinal = "Negativo"
    else:
        return "Zero e par"  # O zero é considerado par

    # Verifica se é par ou ímpar
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    return f"{sinal} e {paridade}"
