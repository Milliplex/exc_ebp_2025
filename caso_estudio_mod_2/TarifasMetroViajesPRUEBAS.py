nombre = input('Ingrese Nombre Completo del Usuario ')


        #La edad del Estudiante
edad = int(input('Ingresar la Edad del Estudiante '))


        #El Estudiante posee Carnet
tiene_carnet = (input('¿El Usuario tiene carnet? (si/no) '))


        #Numero de viajes 
prom_notas = float(input('Promedio de Notas del Estudiante '))


# Llamar a la función desc_tarifa y imprimir el resultado
    # Definir la función desc_tarifa
    
def desc_tarifa(edad, tiene_carnet, prom_notas):
    if edad >= 12 and edad <= 25 and tiene_carnet and prom_notas >= 3.0:
        return print('El estudiante califica para la tarifa especial.')
    else:
        return print('El estudiante no califica para la tarifa especial.')


desc_tarifa(edad, tiene_carnet, prom_notas)
