def calcular_total(precio, cantidad):
    return precio * cantidad


def aplicar_descuento(total, porcentaje):
    if porcentaje <= 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe ser mayor a 0 y no mayor a 100")
    descuento = total * porcentaje / 100
    return total - descuento


def mostrar_total(precio, cantidad, descuento):
    total = calcular_total(precio, cantidad)

    total = aplicar_descuento(total, descuento)

    print(f"Total con descuento: ${total}")


mostrar_total(5000, 3, 10)
