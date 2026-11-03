from analisar_texto import analisar_texto

if __name__ == "__main__":
    # Casos de teste baseados nos requisitos do exercício:
    testes = [
        ("Este é um teste válido", 5),                 # Frase com 5 palavras
        ("Python", 1),                                 # Frase com apenas uma palavra
        ("", 0),                                       # Frase vazia
        ("   espaços no início e no final   ", 6),     # Frase com espaços extras nas pontas
        ("Palavras   com   muitos   espaços", 4)       # Frase com vários espaços entre palavras
    ]
    
    print("--- Resultados dos Testes de Análise de Texto ---")
    for frase, esperado in testes:
        resultado = analisar_texto(frase)
        print(f"Texto: '{frase}' ➔ Contagem: {resultado} (Esperado: {esperado})")
        