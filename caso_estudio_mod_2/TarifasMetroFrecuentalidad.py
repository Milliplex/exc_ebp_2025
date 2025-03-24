                     #Bienvenida
print('Bienvenido al Sistema de Tarifas del Metro de Medellín')

#------------------------.Input.------------------------#

         #Nombre del Pasajero
nombre = input('Ingrese Nombre Completo del Usuario ')

        #Numero de viajes Al Mes
viajes_mes = int(input('Cuantos Viajes Realiza Al Mes '))

    #Tarifa Fija (Base)
tarifa_base = 4000

#-----------------.Calculos y Condiciones.-----------------#

    # Definir la función calcular_descuento
def calcular_descuento(viajes_mes, tarifa_base):
    if viajes_mes <= 10:
        descuento = 0
    elif viajes_mes <= 20:
        descuento = 0.05 * tarifa_base 
    elif viajes_mes <= 30:
        descuento = 0.10 * tarifa_base
    else: descuento = 0.15 * tarifa_base
    return descuento

#------------------------.Outpot.------------------------#

descuento = calcular_descuento(viajes_mes, tarifa_base)
print('El descuento es de' ,descuento)

    # Calculo de la Tarifa Final
tarifa_final = tarifa_base - descuento
print('La Tarifa Final es de' ,tarifa_final)




