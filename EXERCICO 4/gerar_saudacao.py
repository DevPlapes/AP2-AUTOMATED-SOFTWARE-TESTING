def buscar_nome(usuario_id):
    """
    Busca o nome do usuário com base no ID.
    (Em produção viria de uma base de dados).
    """
    return "Carlos"


def gerar_saudacao(usuario_id):
    """
    Recebe o ID, busca o nome correspondente e retorna a saudação formatada.
    """
    nome = buscar_nome(usuario_id)
    return f"Olá, {nome}! Seja bem-vindo."