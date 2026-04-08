import pytest
from src.operaciones import operaciones


def test_operaciones_basicas():
    r = operaciones(10, 2)
    assert r["suma"] == 12
    assert r["resta"] == 8
    assert r["multiplicacion"] == 20
    assert r["division"] == 5


def test_operaciones_division_por_cero():
    r = operaciones(5, 0)
    assert r["suma"] == 5
    assert r["resta"] == 5
    assert r["multiplicacion"] == 0
    assert r["division"] == "Error: división por cero"
