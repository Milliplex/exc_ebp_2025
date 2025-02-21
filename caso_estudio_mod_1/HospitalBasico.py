                     #Bienvenida
print('Bienvenido al Software de registros de Pacientes del Hospital')

#------------------------.Input.------------------------#

         #Nombre del Paciente
nombre = input('Ingrese Nombre Completo del Paciente ')
print('Nombre del Paciente: ' + nombre )


        #La edad del Paciente
edad = int(input('Ingresar la Edad del Paciente '))
print('Edad: ' ,edad, )


        #Duracion de su estancia (dias)
estancia = int(input('Cuantos dias estuvo Ingresado en el Hospital '))
print('Dias Ingresados: ',estancia, )


        #Costo por dia del tratamiento
costoxd = int(input('Costo por dia de Tratamiento '))


#-----------------.Calculos y Condiciones.-----------------#

        #Costo total del Tratamiento
costotot = (estancia * costoxd)
print('Costo total del Tratamiento: ' ,costotot, )

        #Descuento por Edad#
#Formula
costodes = (costotot-((costotot * 10)/100))

#Condicion

if edad > 65:
    print('Costo total con descuento es: ' ,costodes,)
