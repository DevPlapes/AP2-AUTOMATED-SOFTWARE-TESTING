from analisar_numero import analisar_numero

if __name__ == "__main__":
    testes = [
        (10, "Positivo e par"),
        (7, "Positivo e ímpar"),
        (-4, "Negativo e par"),
        (-3, "Negativo e ímpar"),
        (0, "Zero e par")
    ]
    
    print("--- Testes do Exercício 3 ---")
    for num, esperado in testes:
        resultado = analisar_numero(num)
        print(f"Número {num:>3} ➔ {resultado} (Esperado: {esperado})")
        