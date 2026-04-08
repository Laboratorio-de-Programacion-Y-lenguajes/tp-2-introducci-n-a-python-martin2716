"""Condicionales simples para el TP.

Función pedida:
- evaluar_numero(n: int) -> str

La salida es simple: "negativo", "cero" o "positivo".
"""

def evaluar_numero(n: int) -> str:
    """Evalúa si un número es negativo, cero o positivo.

    Retorna exactamente una de las cadenas: "negativo", "cero", "positivo".
    """
    if n < 0:
        return "negativo"
    if n == 0:
        return "cero"
    return "positivo"
