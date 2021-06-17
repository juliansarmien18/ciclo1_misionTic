def SueldoBruto(horasT,valorH):
    cont = 0
    if horasT <= 40:
        VhorasN = int(horasT*valorH)
        print(VhorasN)
        VhorasExtr = 0
        print(VhorasExtr)
        sueldoBruto = VhorasN+VhorasExtr
    elif horasT > 40:
        VhorasN = int(valorH*40)
        print(VhorasN)
        VhorasExtr = (horasT-40)*1.5*valorH
        print(VhorasExtr)
        sueldoBruto = VhorasN+VhorasExtr
    print(sueldoBruto)
    return float(sueldoBruto)

def Descuentos(sueldobruto):
    Descparafiscal = (sueldobruto/100)*9
    print(Descparafiscal)
    Descsalud = (sueldobruto/100)*4
    print(Descsalud)
    Descpension = (sueldobruto/100)*4
    print(Descpension)
    DescT = Descparafiscal+Descpension+Descsalud
    print(DescT)
    return float(DescT)

def provisiones(sueldobruto):
    prima = (sueldobruto/100)*8.33
    print(prima)
    cesantias = (sueldobruto/100)*8.33
    print(cesantias)
    intcesantia = (sueldobruto/100)
    print(intcesantia)
    vacaciones = (sueldobruto/100)*4.17
    print(vacaciones)
    TotalProvi = prima+cesantias+intcesantia+vacaciones
   # print('Total provisiones: ',TotalProvi)
    return float(TotalProvi)

#datos = input('Digite Nombre y apellido: ')
horasT = int(input())
valorH = float(input())
sueldobruto = SueldoBruto(horasT,valorH)
DescT = Descuentos(sueldobruto)
Sueldoneto = sueldobruto - DescT
print(Sueldoneto)
Totalprovi = provisiones(sueldobruto)