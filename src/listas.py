"""Funciones sencillas sobre listas para el TP.

Funciones pedidas por la consigna:
- suma(lista: list[float]) -> float
- promedio(lista: list[float]) -> float

Soluciones directas y didácticas.
"""

def suma(lista: list[float]) -> float:
    """Devuelve la suma de los elementos de la lista.

    Una lista vacía retorna 0.0.
    """
    if not lista:
        return 0.0
    total = 0.0
    for v in lista:
        total += float(v)
    return total


def promedio(lista: list[float]) -> float:
    """Devuelve el promedio de la lista.

    Si la lista está vacía devuelve 0.0 para evitar división por cero.
    """
    if not lista:
        return 0.0
    return suma(lista) / len(lista)
