from os import read, write

def menu():
    print('BIENVENIDO/A'+'\n'+'Elija Una de las Siguiente Opciones')
    print('1. Buscar numero de telefono segun nombre y apellido')
    print('2. Adicionar un nuevo beneficiario')
    print('3. Borrar un beneficiario de la lista')
    print('4.Listar total de beneficiarios')
    print('5.Listar beneficiarios segun letra determinada')
    print('0.Salir')
    op = int(input('Usted escoge la opcion:'))
    return op

def BuscarNom():
    Datos = input('Digite el nombre y el apellido de la persona  buscar el numero:')
    entradaLogico = open('agenda.txt','r')
    for linea in entradaLogico:
        linea = linea.rstrip()
        if linea == Datos:
            cel = entradaLogico.readlines()[1]
            entradaLogico.close
            print('El telefono de',Datos,'es: ',cel)
    entradaLogico.close()

def Adicionar():
    entradaLogico=open('agenda.txt', 'r')
    Nombre=input('digite nombre del nuevo usuario:')
    cedula=input('Digite cedula del nuevo beneficiario:')
    #comparar variable con archivo txt
    for linea in entradaLogico:
        linea = linea.rstrip()
        while linea == cedula:
            cedula = input('esta cedula ya existe, digite una nueva: ')
    entradaLogico.close()
    tel= input('Digite numero de telefono del nuevo beneficiario: ')
    entradaLogico = open('agenda.txt','a')
    entradaLogico.write('\n'+'\n'+Nombre)
    entradaLogico.write('\n'+cedula)
    entradaLogico.write('\n'+tel)
    entradaLogico.close()
    print('se adiciono el nuevo beneficiario')

def Borrar():
    cedula = input('Digite la cedula del beneficiario a Borrar:')
    with open("agenda.txt","r") as f:
        lineas = f.readlines()
        numero = [lineas[lineas.index(n)+1]for n in lineas if n==(cedula+'\n')]
        Nombre = [lineas[lineas.index(n)-1]for n in lineas if n==(cedula+'\n')]
        f.close()

        f=open("agenda.txt","w")
        for linea in lineas:
            linea.rstrip()
            if linea != (Nombre[0]) and linea != (numero[0]) and linea != (cedula+'\n'):
                f.write(linea)
        f.close()
        print('Se ha borrado con exito el Beneficiario')

def ListaCompleta():
    entradaLogico = open('agenda.txt', 'r')
    for linea in entradaLogico:
        print(linea,end="")
    print()
    entradaLogico.close()

def PorLetra():
    letra = input('Digite por favor la letra mayuscula a filtrar: ')
    f=open("agenda.txt","r")
    lineas = f.readlines()
    for n in lineas:
        if n[0]==letra:
            cedula=[lineas[lineas.index(n)+1]]
            cel=[lineas[lineas.index(n)+2]]
            
            print(n,end="")
            print(cedula[0],end="")
            print(cel[0])
    f.close()

op=menu()
while op != 0:
    if op == 1:
        BuscarNom()
        op=menu()
    elif op == 2:
        Adicionar()
        print()
        op=menu()
    elif op == 3:
        Borrar()
        op=menu()
    elif op == 4:
        ListaCompleta()
        print()
        op=menu()
    elif op == 5:
        PorLetra()
        op=menu()
    else:
        exit()