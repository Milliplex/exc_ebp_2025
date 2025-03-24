                     #Bienvenida
print('Bienvenido al Sistema de Tarifas del Metro de Medellín')

#------------------------.Input.------------------------#

         #Nombre del Estudiante
nombre = input('Ingrese Nombre Completo del Usuario ')

        #Hora
hora = int(input('Que hora es? '))

        #Dia
dia_semana = input('Que dia es? ')

#-----------------.Calculos y Condiciones.-----------------#


def es_horario_especial(hora, dia_semana):

    if dia_semana == "Lunes" "Martes" "Miercoles" "Jueves" "Viernes" and hora <= 22 and hora >= 4: 
        return True
    elif dia_semana == "Sabado" and hora >= 14 and hora <=24:
        return True
    elif dia_semana == "Domingo":
        return True
    else: 'None'
    return False

aplica = es_horario_especial(hora, dia_semana)
print('Aplica a la tarifa especal?', aplica)
