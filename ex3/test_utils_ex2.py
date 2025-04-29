import pytest
from utils_ex2 import pega_numero

def test_return_number():
    mensagem: str = "2"
    assert pega_numero(mensagem, '') == 2

def test_return_error_message():
    mensagem: str = "a"
    with pytest.raises(ValueError):
        pega_numero(mensagem, 'Digite um número válido')