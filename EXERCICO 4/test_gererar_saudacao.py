import unittest
from unittest.mock import patch
from gerar_saudacao import buscar_nome, gerar_saudacao


class TestGerarSaudacao(unittest.TestCase):

    def test_buscar_nome_direto(self):
        # Testa a função base diretamente
        self.assertEqual(buscar_nome(1), "Carlos")

    @patch('gerar_saudacao.buscar_nome')
    def test_gerar_saudacao_com_mock(self, mock_buscar_nome):
        # Simula o retorno do Mock para diferentes nomes
        mock_buscar_nome.return_value = "Carlos"

        resultado = gerar_saudacao(42)

        # Valida se a função foi chamada com o ID correto e se a saudação está certa
        mock_buscar_nome.assert_called_once_with(42)
        self.assertEqual(resultado, "Olá, Carlos! Seja bem-vindo.")

    @patch('gerar_saudacao.buscar_nome')
    def test_gerar_saudacao_outro_nome(self, mock_buscar_nome):
        # Testa o Mock simulando outro nome de usuário
        mock_buscar_nome.return_value = "Mariana"

        resultado = gerar_saudacao(7)

        mock_buscar_nome.assert_called_once_with(7)
        self.assertEqual(resultado, "Olá, Mariana! Seja bem-vindo.")


if __name__ == "__main__":
    unittest.main()