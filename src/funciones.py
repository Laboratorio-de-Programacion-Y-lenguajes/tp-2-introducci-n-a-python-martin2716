"""Módulo de funciones simples para el TP.

Contiene la función `contar_palabra` solicitada en la consigna.
"""

import string


def contar_palabra(texto: str, palabra: str) -> int:
    """Cuenta ocurrencias exactas de `palabra` en `texto`.

    El conteo es case-insensitive y compara palabras separadas por
    espacios. Los signos de puntuación al principio o final de cada
    token se eliminan antes de comparar.

    Ejemplo: contar_palabra("Hola, hola mundo", "hola") -> 2
    """
    if not texto or not palabra:
        return 0
    palabra = palabra.lower()
    # eliminar puntuación simple en tokens
    tokens = texto.split()
    contador = 0
    for t in tokens:
        t_clean = t.strip(string.punctuation).lower()
        if t_clean == palabra:
            contador += 1
    return contador
