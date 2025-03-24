                     #Bienvenida
print('Bienvenido al Sistema de Tarifas del Metro de Medellín')

#------------------------.Input.------------------------#

         #Nombre del Estudiante
nombre = input('Ingrese Nombre Completo del Usuario ')


        #Viajes al Mes
viajes_mes = int(input('Cuantos Viajes Realiza al Mes '))


        #Uso Hora Valle
uso_hora_valle = int(input('Viajes en Horas Valle '))


        #Pago Anticipado
pago_anticipado = (input('Paga Mes Anticipado (si/no) '))


#-----------------.Calculos y Condiciones.-----------------#

def calcular_puntos_fidelidad(viajes_mes, uso_hora_valle, pago_anticipado):
    puntos_viajes = viajes_mes * 10 
    puntos_hora_valle = uso_hora_valle * 5

    if pago_anticipado == 'si':
        puntos_pago_anticipado = 100
    else: puntos_pago_anticipado = 0

    return puntos_viajes + puntos_hora_valle + puntos_pago_anticipado

#------------------------.Outpot.------------------------#

resultado = calcular_puntos_fidelidad(viajes_mes, uso_hora_valle, pago_anticipado)
print('Sus Puntos de Fidelidad son: ',resultado)









