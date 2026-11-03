from classificar_nota import classificar_nota

if __name__ == "__main__":
    casos_de_teste = [8, 6, 4, 10, -1, 11]
    
    print("--- Resultados da Classificação ---")
    for nota in casos_de_teste:
        status = classificar_nota(nota)
        print(f"Nota {nota:>3} ➔ {status}")