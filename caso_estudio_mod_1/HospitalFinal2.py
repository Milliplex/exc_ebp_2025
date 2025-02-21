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
#if edad > 65 
   

#------------------------.Outpot.------------------------#

print(f'El nombre del Paciente es: {nombre}, Costo total del tratamiento: {costotot}, ')

if edad > 65:
    print('Costo total con Descuento es:',costodes, 'Al ser adulto mayor, el paciente accedio a un descuento del 10%')
    
else:
    print('Al no ser adulto mayor, el paciente no accede a un descuento del 10%')