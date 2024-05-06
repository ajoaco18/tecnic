
# 1.9 Ejercicio Integrador | UTN TECHNOLOGIES
# Joaquin Aguero 111-1
#https://onlinegdb.com/WAMC7TtWS

contador_masculino_iot_oi = 0
contador_femenino_ai = 0
bandera_mayor_masculino = True
nombre_mayor_masculino = " "
tecnologia_mayor_masculino = ""

for i in range(1,11):
    nombre = input("Nombre de empleado: ")
    edad = int(input("Edad de empleado(No -18): "))
    while edad <= 18:
        edad = int(input("Edad de empleado(No -18): "))
    
    genero = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    
    tecnologia = input("Eliga una tecnologia (IA - RV/RA - IOT): ")
    while tecnologia != "IA" and tecnologia != "RV" and tecnologia != "RA" and tecnologia != "IOT":
        tecnologia = input("Eliga una tecnologia (IA - RV/RA - IOT): ")

    if genero == "Masculino":
        if tecnologia == "IOT" and "IO":
            
                contador_masculino_iot_oi += 1
        
    match genero:
        case "Masculino":
            if tecnologia == "IA" or tecnologia == "IOT":
                if edad < 25 and edad > 50:
                    contador_masculino_iot_oi += 1
            if bandera_mayor_masculino:
                mayor = edad
                tecnologia_mayor_masculino = tecnologia
                bandera_mayor_masculino = False
            elif mayor < edad:
                mayor = edad
                nombre_mayor_masculino = nombre
                tecnologia_mayor_masculino = tecnologia
        case "Femenino":
            if tecnologia != "IA":
                if 33 <= edad <= 40:
                    contador_femenino_ai += 1
porcentaje_no_ia = contador_femenino_ai /10 * 100
print(f"La cantidad de empleados de genero masculino que votaron por IOT o IA, de 25 a 50 años inclusive fue:{contador_masculino_iot_oi}.\n"
      f"Cantidad de empleados que no votaron por ia, (No genero Femenino) y su edad se encuentra entre los 33 y 40 fue de {porcentaje_no_ia}%.\n"
      f"El nombre y la tecnologia que voto el hombre de mayor edad es: {nombre_mayor_masculino}, la tecnologia: {tecnologia_mayor_masculino}.")


                

        
                

             

    
    








