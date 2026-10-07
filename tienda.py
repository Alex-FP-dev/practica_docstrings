"""Utilidades básicas para calcular precios de una tienda."""


def calcular_descuento(precio: float, porcentaje: float) -> float:
    """Calcula el precio final tras aplicar un descuento.

    Args:
        precio: Precio original del producto, en euros.
        porcentaje: Descuento a aplicar, entre 0 y 100.

    Returns:
        Precio con el descuento aplicado.

    Raises:
        ValueError: Si el porcentaje está fuera del rango 0-100.

    Example:
        >>> calcular_descuento(100.0, 20)
        80.0
    """
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)


def calcular_total(precios: list[float], iva: float = 21.0) -> float:
    """Calcula el total de una compra con IVA.

    Args:
        precios: Precio de cada producto, sin IVA.
        iva: Porcentaje de IVA a aplicar. Por defecto 21.

    Returns:
        Total de la compra con IVA, redondeado a 2 decimales.

    Example:
        >>> calcular_total([10.0, 20.0])
        36.3
    """
    return round(sum(precios) * (1 + iva / 100), 2)
