"""Módulo de loops simple para el TP.

Contiene `repetir_palabra(palabra: str, cantidad: int) -> list[str]`.
"""


def repetir_palabra(palabra: str, cantidad: int) -> list[str]:
    """Devuelve una lista con la palabra repetida `cantidad` veces.

    Si `cantidad` es menor o igual a 0 devuelve lista vacía.
    """
    if cantidad <= 0:
        return []
    return [palabra] * cantidad
