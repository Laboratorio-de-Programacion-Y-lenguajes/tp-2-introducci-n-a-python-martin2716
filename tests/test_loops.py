import pytest
from src.loops import repetir_palabra


def test_repetir_palabra_normal():
    assert repetir_palabra("hola", 3) == ["hola", "hola", "hola"]


def test_repetir_palabra_cero():
    assert repetir_palabra("hola", 0) == []


def test_repetir_palabra_negativo():
    assert repetir_palabra("hola", -2) == []
