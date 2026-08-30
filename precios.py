def calcular_total(precio, cantidad):
    return precio * cantidad

def mostrar_total(precio, cantidad):
    total = calcular_total(precio, cantidad)
    print(f"Total compra: ${total}")
