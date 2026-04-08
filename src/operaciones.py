"""Operaciones numéricas sencillas para el TP.

Contiene `operaciones(a: float, b: float) -> dict` que retorna
las operaciones básicas entre `a` y `b`.
"""


def operaciones(a: float, b: float) -> dict:
    """Retorna un diccionario con resultados de operaciones básicas.

    Claves devueltas: 'suma', 'resta', 'multiplicacion', 'division'.
    Si la división no es posible (b == 0) la clave 'division'
    contendrá la cadena "Error: división por cero".
    """
    resultado = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
    }
    if b == 0:
        resultado["division"] = "Error: división por cero"
    else:
        resultado["division"] = a / b
    return resultado
