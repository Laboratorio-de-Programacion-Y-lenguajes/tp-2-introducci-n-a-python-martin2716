import pytest
from src.listas import suma, promedio


def test_suma_valores():
    assert suma([1, 2, 3, 4]) == 10.0
    assert suma([]) == 0.0


def test_promedio_valores():
    assert promedio([2, 4, 6]) == 4.0
    assert promedio([]) == 0.0
