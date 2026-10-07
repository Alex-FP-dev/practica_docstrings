def calcular_descuento(precio: float, porcentaje: float) -> float:
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)


def calcular_total(precios: list[float], iva: float = 21.0) -> float:
    return round(sum(precios) * (1 + iva / 100), 2)

def prueba ():
    pass
    
