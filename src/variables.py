"""Módulo de variables - funciones simples para el TP.

Funciones pedidas por la consigna:
- armar_mensaje(nombre: str, edad: int, ciudad: str) -> str

El código está escrito de forma clara y elemental para un alumno.
"""

def armar_mensaje(nombre: str, edad: int, ciudad: str) -> str:
    """Arma un mensaje con los datos personales.

    Ejemplo: armar_mensaje("Ana", 20, "Ushuaia") ->
    "Soy Ana, tengo 20 años y vivo en Ushuaia."
    """
    return f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}."
