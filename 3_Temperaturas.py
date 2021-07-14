
min = 1
max = 1
diast = 0
diasb = 0
errormin = 0
errormax = 0
error2 = 0
mediamin = 0
mediamax = 0
porcentaje = 0
while min != 0 or max != 0 :
    max = float(input('Ingrese temperatura maxima registrada: '))
    min = float(input('Ingrese temperatura minima registrada: '))
    if min != 0 or max != 0 :
        diast = diast+1
        if min < 5 and max <= 35:
            errormin = errormin+1
            porcentaje = porcentaje+1
           # print('errormin:',errormin)
        elif max > 35 and min >= 5:
            errormax = errormax+1
           # print('errormax:',errormax)
            porcentaje = porcentaje+1
        elif min < 5 and max > 35:
            error2 = error2+1
            #print('error2:',error2)
            porcentaje = porcentaje+1
        else:
            mediamin = mediamin + min
            mediamax = mediamax + max
            diasb=diasb+1
    elif diast == 0:
        quit("No se ingresaron datos")       
mediamin = mediamin/diasb
mediamax = mediamax/diasb
print("dias totales de la salida:",diast)
print("dias totales con errores:",porcentaje)
print("dias con errores en temperatura minimas",errormin,)
print("dias con errores en temperatura maxima",errormax,)
print("dias con errores en ambas temperatura",error2,)
print("la el promedio de temperatura maxima es igual a:",mediamax)
print("la el promedio de temperatura minima es igual a:",mediamin)
porcentaje = (porcentaje*100)/diast
print("los dias que se presentaron errores equivalen al",porcentaje,"%")