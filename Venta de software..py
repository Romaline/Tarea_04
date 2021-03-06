#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°4 de la tarea 4 

print("tabla de descuentos:")
print("de 10 a 19 paquetes se aplica un 20% de descuento")
print("de 29 a 49 paquetes se aplica un 30% de descuento")
print("de 50 a 99 paquetes se aplica un 40% de descuento")
print("de 100 o más paquetes se aplica un 50% de descuento")
def calcularDescuentos(numeroDePaquetes, paquetesTotales):
    if numeroDePaquetes < 10:
        descuento = paquetesTotales
    elif numeroDePaquetes >= 10 and numeroDePaquetes <= 19:
        descuento = paquetesTotales - (paquetesTotales * 20 / 100)
    elif numeroDePaquetes >= 20 and numeroDePaquetes <= 49:
        descuento = paquetesTotales - (paquetesTotales * 30 / 100)
    elif paquetesTotales >= 50 and numeroDePaquetes <= 99:
        descuento = paquetesTotales - (paquetesTotales * 40 / 100)
    elif numeroDePaquetes <= 100:
        descuento = paquetesTotales - (paquetesTotales * 50 / 100)
    return descuento
    
def main():
    numeroDePaquetesComprados= int(input("¿Cúantos paquetes comprará?"))
    numeroDePaquetesTotales = numeroDePaquetesComprados * 1500
    if numeroDePaquetesComprados <= 0:
        print("No puedo introducir números negativos ni valores cero")
    else:
        total=calcularDescuentos(numeroDePaquetesComprados, numeroDePaquetesTotales)
        print("Usted compra:",numeroDePaquetesComprados,"paquetes, El total de su compra es:$" ,format(total), sep="")
main()  
        