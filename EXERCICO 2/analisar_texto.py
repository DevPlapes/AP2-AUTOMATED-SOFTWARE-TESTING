def analisar_texto(texto):
    """
    Recebe uma frase, conta e devolve a quantidade de palavras.
    Retorna 0 se a frase estiver vazia ou composta apenas por espaços.
    """
    # O método .split() divide o texto pelos espaços e retorna uma lista de palavras.
    # Se a string estiver vazia ou só tiver espaços, retorna uma lista vazia.
    palavras = texto.split()
    
    return len(palavras)
