"""Convierte archivos Markdown en páginas HTML autocontenidas.

Uso:
    python md2html.py guia.md                 # genera guia.html
    python md2html.py guia1.md guia2.md       # convierte varios archivos
    python md2html.py *.md                    # en Linux/macOS; en Windows, ver la guía

El estilo (estilo.css) se incrusta dentro del HTML, de modo que cada
archivo resultante se puede abrir o subir sin depender de ningún otro.
"""

import sys
from pathlib import Path

import markdown

CARPETA = Path(__file__).parent
EXTENSIONES = [
    "tables",       # tablas con barras verticales
    "fenced_code",  # bloques de código con ```
    "codehilite",   # colores en el código (necesita pygments)
    "toc",          # genera el índice y los identificadores de los títulos
    "sane_lists",   # listas más predecibles
]
CONFIGURACION = {
    "codehilite": {"noclasses": True, "guess_lang": False},
    "toc": {"toc_depth": "2-3"},
}

PLANTILLA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<style>
{css}
</style>
</head>
<body>
{cuerpo}
</body>
</html>
"""


def extraer_titulo(texto: str, por_defecto: str) -> str:
    """Obtiene el título de la página a partir del primer encabezado `# `.

    Args:
        texto: Contenido del archivo Markdown.
        por_defecto: Título a usar si no hay ningún encabezado de nivel 1.

    Returns:
        El texto del primer encabezado de nivel 1, o el valor por defecto.

    Example:
        >>> extraer_titulo("# Mi guía", "sin título")
        'Mi guía'
        >>> extraer_titulo("Solo texto", "sin título")
        'sin título'
    """
    for linea in texto.splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return por_defecto


def convertir(origen: Path) -> Path:
    """Convierte un archivo Markdown en un HTML con el estilo incrustado.

    Args:
        origen: Ruta del archivo `.md` a convertir.

    Returns:
        Ruta del archivo `.html` generado, junto al original.

    Raises:
        FileNotFoundError: Si el archivo no existe.
    """
    texto = origen.read_text(encoding="utf-8")
    cuerpo = markdown.markdown(
        texto,
        extensions=EXTENSIONES,
        extension_configs=CONFIGURACION,
    )
    css = (CARPETA / "estilo.css").read_text(encoding="utf-8")
    pagina = PLANTILLA.format(
        titulo=extraer_titulo(texto, origen.stem),
        css=css,
        cuerpo=cuerpo,
    )
    destino = origen.with_suffix(".html")
    destino.write_text(pagina, encoding="utf-8")
    return destino


def main() -> None:
    """Convierte todos los archivos indicados por línea de comandos."""
    archivos = sys.argv[1:]
    if not archivos:
        print("Uso: python md2html.py archivo.md [otro.md ...]")
        sys.exit(1)
    for nombre in archivos:
        destino = convertir(Path(nombre))
        print(f"OK  {nombre} -> {destino.name}")


if __name__ == "__main__":
    main()
