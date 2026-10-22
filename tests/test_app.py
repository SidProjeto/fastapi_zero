from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_raiz_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT)
    - A: Assert - Garanta que A é A
    """

    # Arrange
    cliente = TestClient(app)

    # Act
    resposta = cliente.get('/')

    # Assert
    assert resposta.json() == {'mensagem': 'olá mundo!'}
    assert resposta.status_code == HTTPStatus.OK
