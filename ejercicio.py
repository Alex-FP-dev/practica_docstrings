# EJERCICIO: documentar código Python
#
# Tareas:
#   1. Añade type hints a todas las funciones y métodos.
#   2. Escribe un docstring estilo Google en el módulo, en cada función,
#      en cada clase y en cada método público.
#   3. Incluye una sección Example con doctest en al menos 3 funciones/métodos.
#   4. Comprueba tu trabajo:
#        - Pasa el ratón sobre una función en VS Code.
#        - python -c "import ejercicio; help(ejercicio.Alumno)"
#        - python -m doctest -v ejercicio.py


def calcular_media(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return round(sum(notas) / len(notas), 2)


def es_aprobado(nota, minimo=5.0):
    return nota >= minimo


def clasificar_nota(nota):
    if not 0 <= nota <= 10:
        raise ValueError("La nota debe estar entre 0 y 10")
    if nota < 5:
        return "Suspenso"
    if nota < 7:
        return "Aprobado"
    if nota < 9:
        return "Notable"
    return "Sobresaliente"


class Alumno:
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        self.notas = notas if notas is not None else []

    def agregar_nota(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.notas.append(nota)

    def media(self):
        return calcular_media(self.notas)

    def esta_aprobado(self):
        return es_aprobado(self.media())


class Aula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def matricular(self, alumno):
        self.alumnos.append(alumno)

    def buscar_alumno(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre.lower() == nombre.lower():
                return alumno
        return None

    def mejor_alumno(self):
        if not self.alumnos:
            return None
        return max(self.alumnos, key=lambda alumno: alumno.media())
