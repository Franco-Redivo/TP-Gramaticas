## Se requiere la creación de un sistema que permita realizar el control de residuos peligrosos, para lo cual debe generar el código de evaluación de residuos para incorporar al sistema. El bloque procesará la siguiente información: Nivel de peligrosidad Cantidad en kilos Destino Se debe considerar validar que la cantidad de kilos a procesar no supero los 450 kilos.

def generar_codigo_residuo(nivel_peligrosidad, cantidad_kilos, destino):
    if cantidad_kilos > 450:
        return "Error: La cantidad de kilos a procesar no puede superar los 450 kilos."
    
    codigo_residuo = f"{nivel_peligrosidad[:3].upper()}-{cantidad_kilos}-{destino[:3].upper()}"
    return codigo_residuo

# Ejemplo de uso
nivel_peligrosidad = "Alto"
cantidad_kilos = 300
destino = "Planta de tratamiento"
codigo = generar_codigo_residuo(nivel_peligrosidad, cantidad_kilos, destino)
print(codigo)
# ALT-300-PLA

# Ejemplo con cantidad superior a 450 kilos
cantidad_kilos_exceso = 500
codigo_exceso = generar_codigo_residuo(nivel_peligrosidad, cantidad_kilos_exceso, destino)
print(codigo_exceso)
