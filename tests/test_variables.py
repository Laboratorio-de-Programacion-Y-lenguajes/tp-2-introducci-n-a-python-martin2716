import pytest
from src.variables import armar_mensaje


def test_armar_mensaje_simple():
    assert (
        armar_mensaje("Ana", 20, "Ushuaia")
        == "Soy Ana, tengo 20 años y vivo en Ushuaia."
    )


def test_armar_mensaje_valores_distintos():
    assert (
        armar_mensaje("Juan", 30, "Rio Grande")
        == "Soy Juan, tengo 30 años y vivo en Rio Grande."
    )
