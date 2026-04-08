"""Funciones simples con diccionarios para el TP.

Contiene `mostrar_datos(dic: dict) -> str` que formatea datos
personales esperados en el diccionario.
"""


def mostrar_datos(dic: dict) -> str:
    """Devuelve una cadena formateada con los datos de la persona.

    Usa las claves esperadas: 'nombre', 'apellido', 'edad', 'mail'.
    Si alguna clave falta, usa una cadena vacía en su lugar.

    Formato resultante: "{nombre} {apellido} ({edad}) - {mail}"
    """
    nombre = dic.get("nombre", "")
    apellido = dic.get("apellido", "")
    edad = dic.get("edad", "")
    mail = dic.get("mail", "")
    return f"{nombre} {apellido} ({edad}) - {mail}"
