import pytest
from src.funciones import contar_palabra


def test_contar_palabra_simple():
    assert contar_palabra("hola mundo hola", "hola") == 2


def test_contar_palabra_puntuacion_case():
    assert contar_palabra("Hola, hola!", "hola") == 2


def test_contar_palabra_vacio():
    assert contar_palabra("", "hola") == 0
