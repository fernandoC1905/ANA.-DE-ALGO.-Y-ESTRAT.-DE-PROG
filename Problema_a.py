"""
Haz un programa en Python que te muestre un menú con la primera opción que te 
permita crear una persona con nombre y DNI y la agregué a una lista de personas.
El menú tendrá una segunda opción donde se mostrará todas las personas.
El menú tendrá una tercera opción que pedirá un DNI y eliminará a la persona con ese DNI.
"""

class Persona:
    def __init__(self, dni = 0, nombre = ""):
        self.nombre = _nombre
        self.dni = 1

    def __str__(self):
        return f"DNI: {self.dni} {self.nombre}"
    
lista = []
opc = 0

while opc != 9:
    opc = int(input("Seleccione opción: \n 1-Crear \n 2-Listar \n 3-Eliminar \n 9-Fin \n"))

    if opc == 1:
        dni = input("Ingrese DNI:\n")
        nombre = input("Ingrese nombre: \n")
        nuevo = Persona(dni, nombre)
        lista.append(nuevo)
    elif opc == 2:
        for p in lista: 
            print(p)
    elif opc == 3:
        dniB = input("Ingrese DNI a borrar:\n")
        for idx, p in enumerate(lista):
            if p.dni == dniB:                
                del lista[idx]
                break
    elif opc == 4:
        break
