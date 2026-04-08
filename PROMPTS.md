## PROMPTS - 7 ejercicios (uno por módulo)

Cada sección contiene: nombre del ejercicio, patrón usado y el prompt completo
que un estudiante podría usar para generar la solución básica.

1) Variables — Patrón: Persona
--------------------------------
Nombre del ejercicio: armar_mensaje
Prompt:
Actuá como un profesor de programación. Escribí una función Python llamada
`armar_mensaje(nombre: str, edad: int, ciudad: str) -> str` que devuelva el
texto: "Soy {nombre}, tengo {edad} años y vivo en {ciudad}.". No uses librerías.

2) Condicionales — Patrón: Template
------------------------------------
Nombre del ejercicio: evaluar_numero
Prompt:
Usá este template para crear la función `evaluar_numero(n: int) -> str`:
- si n < 0 -> "negativo"
- si n == 0 -> "cero"
- si n > 0 -> "positivo"
Escribí la función en Python con una docstring corta.

3) Listas — Patrón: Recipe
---------------------------
Nombre del ejercicio: suma, promedio
Prompt:
Dame una receta paso a paso (comentarios breves) y el código para dos funciones
en Python:
- `suma(lista: list[float]) -> float` que devuelva 0.0 para lista vacía,
- `promedio(lista: list[float]) -> float` que use `suma` y devuelva 0.0 si
	la lista está vacía.

4) Funciones — Patrón: Question Refinement
------------------------------------------
Nombre del ejercicio: contar_palabra
Prompt:
Primero preguntame si el conteo debe ser case-insensitive y si debe
ignorar la puntuación. Luego, con mis respuestas, escribí la función
`contar_palabra(texto: str, palabra: str) -> int` que cuente coincidencias
exactas (case-insensitive) y limpie puntuación simple.

5) Diccionarios — Patrón: Cognitive Verifier
-------------------------------------------
Nombre del ejercicio: mostrar_datos
Prompt:
Como verificador, listá casos de prueba para una función `mostrar_datos(dic)`
que reciba un diccionario con claves `nombre`, `apellido`, `edad`, `mail` y
devuelva "{nombre} {apellido} ({edad}) - {mail}". Luego escribí la función
en código simple.

6) Loops — Patrón: Flipped Interaction
---------------------------------------
Nombre del ejercicio: repetir_palabra
Prompt:
En vez de dar el código primero, indicá por qué devolver `[]` si `cantidad` <
0 es razonable para un TP. Luego escribí la función
`repetir_palabra(palabra: str, cantidad: int) -> list[str]` que implemente eso.

7) Operaciones — Patrón: Context Manager
-----------------------------------------
Nombre del ejercicio: operaciones
Prompt:
Contextualizá: estamos escribiendo funciones para alumnos. Implementá
`operaciones(a: float, b: float) -> dict` que retorne suma/resta/multiplicaci\u00f3n
y división. Si `b` es 0, la división debe ser la cadena
"Error: división por cero". Escribí el código y un breve comentario justificando
la decisión.

---

Estos prompts son simples, académicos y fáciles de adaptar por un estudiante.
