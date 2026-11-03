def verificar_senha(senha):
    """
    Valida se a senha tem pelo menos 8 caracteres,
    contém ao menos um número e ao menos uma letra.
    """
    if len(senha) < 8:
        return False
    
    tem_numero = any(c.isdigit() for c in senha)
    tem_letra = any(c.isalpha() for c in senha)
    
    return tem_numero and tem_letra


def criar_conta(nome, senha):
    """
    Tenta criar uma conta validando a senha fornecida.
    """
    if verificar_senha(senha):
        return "Conta criada com sucesso"
    else:
        return "Senha inválida"
