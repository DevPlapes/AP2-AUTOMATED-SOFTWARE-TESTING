import unittest
from unittest.mock import patch
from gerenciar_conta import verificar_senha, criar_conta


class TestGerenciarConta(unittest.TestCase):

    def test_validacao_senha_direta(self):
        # Testa senhas diretamente nas regras criadas
        self.assertTrue(verificar_senha("SenhaForte123"))
        self.assertFalse(verificar_senha("curta1"))
        self.assertFalse(verificar_senha("somentetags"))

    @patch('gerenciar_conta.verificar_senha')
    def test_criar_conta_com_senha_valida(self, mock_verifica):
        # Simula o comportamento da função de verificar senha retornando True
        mock_verifica.return_value = True
        
        resultado = criar_conta("Arthur", "SenhaValida123")
        
        # Garante que a função foi chamada corretamente e retornou a mensagem esperada
        mock_verifica.assert_called_once_with("SenhaValida123")
        self.assertEqual(resultado, "Conta criada com sucesso")

    @patch('gerenciar_conta.verificar_senha')
    def test_criar_conta_com_senha_invalida(self, mock_verifica):
        # Simula o comportamento da função de verificar senha retornando False
        mock_verifica.return_value = False
        
        resultado = criar_conta("Arthur", "123")
        
        # Garante que a verificação foi executada e tratou o erro
        mock_verifica.assert_called_once_with("123")
        self.assertEqual(resultado, "Senha inválida")


if __name__ == "__main__":
    unittest.main()
    