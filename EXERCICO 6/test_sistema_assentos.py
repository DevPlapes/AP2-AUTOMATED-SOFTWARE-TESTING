import unittest
from unittest.mock import patch
from sistema_assentos import verificar_assento, reservar_assento, confirmar_reserva


class TestSistemaAssentos(unittest.TestCase):

    @patch('sistema_assentos.reservar_assento')
    @patch('sistema_assentos.verificar_assento')
    def test_reserva_com_sucesso(self, mock_verificar, mock_reservar):
        # Simula assento disponível e reserva bem-sucedida
        mock_verificar.return_value = True
        mock_reservar.return_value = "Assento reservado"

        resultado = confirmar_reserva(10)

        # Confirma as chamadas e o resultado esperado
        mock_verificar.assert_called_once_with(10)
        mock_reservar.assert_called_once_with(10)
        self.assertEqual(resultado, "Assento reservado")

    @patch('sistema_assentos.reservar_assento')
    @patch('sistema_assentos.verificar_assento')
    def test_assento_ocupado(self, mock_verificar, mock_reservar):
        # Simula assento indisponível (ocupado)
        mock_verificar.return_value = False

        resultado = confirmar_reserva(10)

        # Confirma que verificou, mas nem chegou a chamar a função de reservar
        mock_verificar.assert_called_once_with(10)
        mock_reservar.assert_not_called()
        self.assertEqual(resultado, "Assento indisponível")


if __name__ == "__main__":
    unittest.main()
    