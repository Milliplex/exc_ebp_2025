                     #Bienvenida
print('Bienvenido al Software de registros de Pacientes del Hospital')

#------------------------.Input.------------------------#

         #Nombre del Paciente
nombre = input('Ingrese Nombre Completo del Paciente ')


        #La edad del Paciente
edad = int(input('Ingresar la Edad del Paciente '))


        #Duracion de su estancia (dias)
estancia = int(input('Cuantos dias estuvo Ingresado en el Hospital '))


        #Costo por dia del tratamiento
costoxd = int(input('Costo por dia de Tratamiento '))


#-----------------.Calculos y Condiciones.-----------------#

          #Costo total del Tratamiento
costotot = (estancia * costoxd)

          #Descuento por Edad#
#Formula
costodes = (costotot-((costotot * 10)/100))

                #Condicion

#if edad > 65:
    #print('Costo total con descuento es: ' ,costodes,)


#------------------------.Outpot.------------------------#

        #Nombre Paciente
print('Nombre del Paciente: ' + nombre )

        #CostoTOT & Descuento(if)
print('Costo total del Tratamiento: ' ,costotot, )

if edad > 65:
    print('Costo total con Descuento es: ' ,costodes,)
    print('Al ser adulto mayor, el paciente accedio a un descuento del 10%')