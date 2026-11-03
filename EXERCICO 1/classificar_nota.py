def classificar_nota(nota):
    """
    Avalia a nota de um aluno e devolve o seu estado académico.
    
    Critérios:
    - Aprovado: nota maior ou igual a 7
    - Recuperação: nota entre 5 e 6.9
    - Reprovado: nota inferior a 5
    - Nota inválida: valores fora do intervalo [0, 10]
    """
    if not (0 <= nota <= 10):
        return "Nota inválida"
    
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

    