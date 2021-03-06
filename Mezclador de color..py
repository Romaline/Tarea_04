#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n3 de la tarea 4 

def mezclarColor(colorX, colorY):
    if (colorX == "ROJO" and colorY == "ROJO"):
        mezcla = "ROJO"
    elif (colorX == "ROJO" and colorY == "AMARILLO") or (colorX == "AMARILLO" and colorY == "ROJO"):
        mezcla = "NARANJA"
    elif (colorX == "ROJO" and colorY == "AZUL") or (colorX == "AZUL" and colorY == "ROJO"):
        mezcla = "MORADO"
    elif (colorX == "AMARILLO" and colorY == "AMARILLO"):
        mezcla = "AMARILLO"
    elif (colorX == "AMARILLO" and colorY == "AZUL") or (colorX == "AZUL" and colorY == "AMARILLO"):
        mezcla = "VERDE"
    elif (colorX == "AZUL" and colorY == "AZUL"):
        mezcla = "AZUL"    
    return mezcla
    
def main():
    ingrediente1 = str( input("Elija un color para mezclar, este debe ser un color primario"))
    ingrediente1 = ingrediente1.upper()
    ingrediente2 = str( input("Elija otro color, este tambien debe ser un color primario"))
    ingrediente2 = ingrediente2.upper()
    mezclaFinal=mezclarColor(ingrediente1, ingrediente2)
    
    if (ingrediente1 == "ROJO" or ingrediente1 == "AMARILLO" or ingrediente1 == "AZUL") and (ingrediente2 == "ROJO" or ingrediente2 == "AMARILLO" or ingrediente2 == "AZUL"):
        print("El resultado de mezclar estos colores es:",mezclaFinal)
    else:
        print("El programa solo soporta los colores primarios, Rojo, Azul y Amarillo")
        
main()