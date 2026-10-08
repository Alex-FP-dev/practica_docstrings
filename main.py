"""Programa de prueba para ejercicio_solucion.py.

Sirve para ejecutar el código y para comprobar el hover de VS Code:
pasa el ratón por encima de cualquier función, clase o método.
"""

from ejercicio_solucion import (
    Alumno,
    Aula,
    calcular_media,
    clasificar_nota,
    es_aprobado,
)


def main() -> None:
    """Ejecuta una demostración de todas las funciones y clases."""
    # --- Funciones sueltas ---
    print("=== Funciones ===")
    notas = [6, 8, 10]
    print(f"Media de {notas}: {calcular_media(notas)}")
    print(f"¿4.9 aprueba? {es_aprobado(4.9)}")
    print(f"¿5 aprueba? {es_aprobado(5)}")
    print(f"Clasificación de 7.5: {clasificar_nota(7.5)}")

    # --- Clase Alumno ---
    print("\n=== Alumno ===")
    ana = Alumno("Ana", [9, 10])
    ana.agregar_nota(8)
    print(f"{ana.nombre}: notas={ana.notas}, media={ana.media()}")
    print(f"¿{ana.nombre} aprobada? {ana.esta_aprobado()}")

    # --- Clase Aula ---
    print("\n=== Aula ===")
    aula = Aula("2 DAM")
    aula.matricular(ana)
    aula.matricular(Alumno("Luis", [4, 5]))
    aula.matricular(Alumno("Marta", [7, 6, 8]))

    mejor = aula.mejor_alumno()
    if mejor is not None:
        print(f"Mejor alumno de {aula.nombre}: {mejor.nombre} ({mejor.media()})")

    encontrado = aula.buscar_alumno("luis")
    if encontrado is not None:
        print(f"Encontrado: {encontrado.nombre}, media {encontrado.media()}")
    print(f"¿Existe Pedro? {aula.buscar_alumno('Pedro') is not None}")

    # --- Errores controlados (los documentados en Raises) ---
    print("\n=== Errores esperados ===")
    try:
        calcular_media([])
    except ValueError as error:
        print(f"calcular_media([]) -> ValueError: {error}")

    try:
        clasificar_nota(11)
    except ValueError as error:
        print(f"clasificar_nota(11) -> ValueError: {error}")

    try:
        Alumno("Sin notas").media()
    except ValueError as error:
        print(f"Alumno sin notas -> ValueError: {error}")


if __name__ == "__main__":
    main()