"""Gestión sencilla de alumnos, notas y aulas.

Este módulo permite calcular medias, clasificar notas y organizar
alumnos dentro de un aula.

Example:
    >>> aula = Aula("2 DAM")
    >>> aula.matricular(Alumno("Ana", [9, 10]))
    >>> aula.mejor_alumno().nombre
    'Ana'
"""

from collections.abc import Sequence


def calcular_media(notas: Sequence[float]) -> float:
    """Calcula la nota media de una secuencia de notas.

    Args:
        notas: Lista o tupla de notas, cada una entre 0 y 10.

    Returns:
        Media aritmética redondeada a 2 decimales.

    Raises:
        ValueError: Si la lista de notas está vacía.

    Example:
        >>> calcular_media([6, 8, 10])
        8.0
        >>> calcular_media([5, 6])
        5.5
    """
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return round(sum(notas) / len(notas), 2)


def es_aprobado(nota: float, minimo: float = 5.0) -> bool:
    """Indica si una nota alcanza el mínimo para aprobar.

    Args:
        nota: Nota a evaluar.
        minimo: Nota mínima para aprobar. Por defecto 5.0.

    Returns:
        True si la nota es igual o superior al mínimo, False en caso contrario.

    Example:
        >>> es_aprobado(4.9)
        False
        >>> es_aprobado(5)
        True
    """
    return nota >= minimo


def clasificar_nota(nota: float) -> str:
    """Convierte una nota numérica en su calificación textual.

    Args:
        nota: Nota entre 0 y 10.

    Returns:
        Una de estas calificaciones: "Suspenso", "Aprobado", "Notable"
        o "Sobresaliente".

    Raises:
        ValueError: Si la nota no está entre 0 y 10.

    Example:
        >>> clasificar_nota(7.5)
        'Notable'
        >>> clasificar_nota(3)
        'Suspenso'
    """
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
    """Representa a un alumno con sus notas.

    Attributes:
        nombre: Nombre del alumno.
        notas: Lista de notas registradas, cada una entre 0 y 10.

    Example:
        >>> alumno = Alumno("Ana", [7, 9])
        >>> alumno.agregar_nota(8)
        >>> alumno.media()
        8.0
    """

    def __init__(self, nombre: str, notas: Sequence[float] | None = None) -> None:
        """Crea un alumno.

        Args:
            nombre: Nombre del alumno.
            notas: Notas iniciales. Si no se indica, empieza sin notas.
        """
        self.nombre = nombre
        self.notas: list[float] = list(notas) if notas is not None else []

    def agregar_nota(self, nota: float) -> None:
        """Registra una nueva nota.

        Args:
            nota: Nota a añadir, entre 0 y 10.

        Raises:
            ValueError: Si la nota no está entre 0 y 10.
        """
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.notas.append(nota)

    def media(self) -> float:
        """Calcula la nota media del alumno.

        Returns:
            Media de todas sus notas, redondeada a 2 decimales.

        Raises:
            ValueError: Si el alumno todavía no tiene notas.
        """
        return calcular_media(self.notas)

    def esta_aprobado(self) -> bool:
        """Indica si el alumno aprueba con su media actual.

        Returns:
            True si la media es 5.0 o superior.

        Raises:
            ValueError: Si el alumno todavía no tiene notas.

        Example:
            >>> Alumno("Luis", [4, 5]).esta_aprobado()
            False
        """
        return es_aprobado(self.media())


class Aula:
    """Grupo de alumnos matriculados en una misma clase.

    Attributes:
        nombre: Nombre del aula o grupo.
        alumnos: Alumnos matriculados.
    """

    def __init__(self, nombre: str) -> None:
        """Crea un aula vacía.

        Args:
            nombre: Nombre del aula o grupo, por ejemplo "2 DAM".
        """
        self.nombre = nombre
        self.alumnos: list[Alumno] = []

    def matricular(self, alumno: Alumno) -> None:
        """Añade un alumno al aula.

        Args:
            alumno: Alumno que se matricula.
        """
        self.alumnos.append(alumno)

    def buscar_alumno(self, nombre: str) -> Alumno | None:
        """Busca un alumno por su nombre, sin distinguir mayúsculas.

        Args:
            nombre: Nombre del alumno a buscar.

        Returns:
            El alumno encontrado o None si no existe.

        Example:
            >>> aula = Aula("2 DAM")
            >>> aula.matricular(Alumno("Ana"))
            >>> aula.buscar_alumno("ana").nombre
            'Ana'
            >>> aula.buscar_alumno("Pedro") is None
            True
        """
        for alumno in self.alumnos:
            if alumno.nombre.lower() == nombre.lower():
                return alumno
        return None

    def mejor_alumno(self) -> Alumno | None:
        """Obtiene el alumno con mejor nota media.

        Returns:
            El alumno con la media más alta, o None si el aula está vacía.

        Raises:
            ValueError: Si algún alumno matriculado no tiene notas.

        Example:
            >>> aula = Aula("2 DAM")
            >>> aula.matricular(Alumno("Ana", [9, 10]))
            >>> aula.matricular(Alumno("Luis", [5, 6]))
            >>> aula.mejor_alumno().nombre
            'Ana'
        """
        if not self.alumnos:
            return None
        return max(self.alumnos, key=lambda alumno: alumno.media())
