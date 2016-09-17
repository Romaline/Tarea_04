#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°5 de la tarea 4 

def calcularImc(pesoEnKg ,estatura):
    imc = pesoEnKg / estatura**2
    return imc
    
def main():
    pesoDeLaPersona = float(input("Ingrese el peso en Kg"))
    alturaDeLaPersona = float(input("ingrese la altura en metros"))
    if pesoDeLaPersona <= 0:
        print("No puede poner numeros negativos ni valores 0")
    else:
        imcDeLaPersona = calcularImc(pesoDeLaPersona, alturaDeLaPersona)
        print("Usted tiene un IMC de", imcDeLaPersona)
        if imcDeLaPersona < 18.5:
            print("Usted entra en la categoria de bajo peso")
        elif imcDeLaPersona > 18.5 and imcDeLaPersona < 25:
            print("Usted entra en la categoria de peso normal")
        else:
            print("Usted entra en la categoria de sobrepeso")
        
main()
    
    

 