# Práctica de docstrings

Documentación de un pequeño módulo para gestionar alumnos, notas y aulas.

## Qué contiene

- **Funciones** para calcular medias y clasificar notas.
- **`Alumno`**: guarda las notas de un alumno y calcula su media.
- **`Aula`**: agrupa alumnos, permite buscarlos y encontrar al mejor.

## Uso rápido

```python
from ejercicio_solucion import Alumno, Aula

aula = Aula("2 DAM")
aula.matricular(Alumno("Ana", [9, 10]))
aula.matricular(Alumno("Luis", [5, 6]))

print(aula.mejor_alumno().nombre)  # Ana
```

## Más información

Consulta la [referencia completa](referencia.md), generada a partir de los docstrings del código.
