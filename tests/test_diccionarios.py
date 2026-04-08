import pytest
from src.diccionarios import mostrar_datos


def test_mostrar_datos_completo():
    persona = {"nombre": "Ana", "apellido": "Perez", "edad": 22, "mail": "ana@example.com"}
    assert mostrar_datos(persona) == "Ana Perez (22) - ana@example.com"


def test_mostrar_datos_faltan_claves():
    persona = {"nombre": "Luis"}
    assert mostrar_datos(persona) == "Luis  () - "
