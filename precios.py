def calcular_total(precio, cantidad):
    return precio * cantidad


def aplicar_descuento(total, porcentaje):
    descuento = total * porcentaje / 100
    return total - descuento


def mostrar_total(precio, cantidad):
    total = calcular_total(precio, cantidad)

    total = aplicar_descuento(total, 10)

    print(f"Total con descuento: ${total}")


mostrar_total(5000, 3)
