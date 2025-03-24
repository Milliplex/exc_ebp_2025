                     #Bienvenida
print('Bienvenido al Sistema de Tarifas del Metro de Medellín')

#------------------------.Input.------------------------#

         #Nombre del Estudiante
nombre = input('Ingrese Nombre Completo del Usuario ')


        #La edad del Estudiante
edad = int(input('Ingresar la Edad del Estudiante '))


        #El Estudiante posee Carnet
tiene_carnet = (input('¿El Usuario tiene carnet? (si/no) '))


        #Numero de viajes 
prom_notas = float(input('Promedio de Notas del Estudiante '))


#-----------------.Calculos y Condiciones.-----------------#


# Definir la función desc_tarifa
def desc_tarifa(edad, tiene_carnet, prom_notas):
    if edad >= 12 and edad <= 25 and tiene_carnet == "si" and prom_notas >= 3.0:
         return True
    else:
         return False

aplica = desc_tarifa(edad, tiene_carnet, prom_notas)
print('Aplica a la tarifa especal?', aplica)

#------------------------.Outpot.------------------------#
