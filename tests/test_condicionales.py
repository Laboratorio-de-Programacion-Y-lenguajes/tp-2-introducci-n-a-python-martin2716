import pytest
from src.condicionales import evaluar_numero


def test_evaluar_numero_negativo():
    assert evaluar_numero(-5) == "negativo"


def test_evaluar_numero_cero():
    assert evaluar_numero(0) == "cero"


def test_evaluar_numero_positivo():
    assert evaluar_numero(10) == "positivo"
