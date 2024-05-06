def calculo_producto(precio: int, cantidad: int, porcentaje: float)-> (float | int):
    
    if cantidad >= 10:
        descuento = precio * porcentaje
        total = precio - descuento
    else:
        total = precio
        
    
    return total

total = calculo_producto(5000, 10, 0.2)
print(f"El precio final de su producto es: {total}.")


