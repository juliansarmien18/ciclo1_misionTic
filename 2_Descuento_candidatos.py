'''Reto Semana 3
Julian Sarmiento'''
#funcion para definir los decuentos
def Descuento(edad, salarios, puntaje):
#seccion para descuentos por edad
    if edad >= 15 and edad <= 18:
        desc_edad = 25
    elif edad >= 19 and edad <= 21:
        desc_edad = 15
    elif edad >= 22 and edad <= 25:
        desc_edad = 10
    elif edad > 25:
        desc_edad = 0
#seccion para descuentos por salario
    if salarios <= 1 :
        desc_sal = 30
    elif salarios > 1 and salarios <=2:
        desc_sal = 20
    elif salarios > 2 and salarios <=3:
        desc_sal = 10
    elif salarios > 3 and salarios <=4:
        desc_sal = 5
    elif salarios > 4:
        desc_sal = 0
#seccion para descuentos por puntaje
    if puntaje >= 96:
        desc_punt = 45
    elif puntaje >= 91 and puntaje < 96:
        desc_punt = 40
    elif puntaje >= 86 and puntaje < 91:
        desc_punt = 35
    elif puntaje >= 80 and puntaje < 86:
        desc_punt = 30
    elif puntaje < 80:
        desc_punt = 0
#se retorna la suma del porcentaje total
    print('descuento por edad:',desc_edad)
    print('descuento por salario:', desc_sal)
    print('descuento por puntaje:', desc_punt)
    return(desc_punt+desc_edad+desc_sal)

print(' BIENVENIDO AL SISTEMA DE DESCUENTOS')
#ingreso de variables
nom_ap = input('Digite nombre y apellido del candidato: ')
edad = int(input('Digite edad del candidato: '))
puntaje = int(input('digite puntaje obtenido: '))
dec_salarios = float(input('Digite numero de salarios minimos con decimales: '))
#se almacenan los datos de la funcion de calculo en una unica variable, es opcional ya que dentro del print se puede llamar a la funcion
desc_total = Descuento(edad, dec_salarios, puntaje)
print('El candidato '+nom_ap+' recibirá un decuento total del', desc_total, '%')