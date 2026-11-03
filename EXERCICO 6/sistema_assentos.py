def verificar_assento(numero_assento):
    """
    Verifica se o assento está disponível.
    """
    # Na implementação real consultaria uma base de dados.
    return True


def reservar_assento(numero_assento):
    """
    Efetua a reserva do assento.
    """
    return "Assento reservado"


def confirmar_reserva(numero_assento):
    """
    Valida a disponibilidade e faz a reserva se estiver livre.
    """
    if verificar_assento(numero_assento):
        return reservar_assento(numero_assento)
    else:
        return "Assento indisponível"
    