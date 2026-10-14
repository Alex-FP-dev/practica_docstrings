# Diagramas

Los diagramas se escriben como texto con [Mermaid](https://mermaid.js.org/) y se dibujan al generar la web. Al ser texto, se versionan con Git igual que el código.

## Diagrama de clases

Muestra las clases del módulo, sus atributos, métodos y cómo se relacionan.

```mermaid
classDiagram
    class Alumno {
        +str nombre
        +list~float~ notas
        +agregar_nota(nota)
        +media() float
        +esta_aprobado() bool
    }
    class Aula {
        +str nombre
        +list~Alumno~ alumnos
        +matricular(alumno)
        +buscar_alumno(nombre) Alumno
        +mejor_alumno() Alumno
    }
    Aula "1" o-- "*" Alumno : contiene
```

## Diagrama de flujo: `clasificar_nota`

Describe la lógica de decisión de la función.

```mermaid
flowchart TD
    A["nota"] --> B{"¿entre 0 y 10?"}
    B -- No --> C["ValueError"]
    B -- Sí --> D{"¿nota < 5?"}
    D -- Sí --> E["Suspenso"]
    D -- No --> F{"¿nota < 7?"}
    F -- Sí --> G["Aprobado"]
    F -- No --> H{"¿nota < 9?"}
    H -- Sí --> I["Notable"]
    H -- No --> J["Sobresaliente"]
```

## Diagrama de secuencia: `mejor_alumno`

Muestra qué objetos intervienen y en qué orden cuando se pide el mejor alumno del aula.

```mermaid
sequenceDiagram
    participant P as main.py
    participant AU as Aula
    participant AL as Alumno
    P->>AU: mejor_alumno()
    loop por cada alumno matriculado
        AU->>AL: media()
        AL-->>AU: float
    end
    AU-->>P: alumno con la media más alta
```
