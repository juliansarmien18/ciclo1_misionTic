from os import read, write


def menu():
    print('Menu Principal')
    print('1. Ver listado')
    print('2. Ver listado filtrado')
    print('3. Agregar beneficiario')
    print('4. Buscar beneficiario')
    print('5. Borrar beneficiario')
    print('6. Salir')
    op = int(input())
    return op

def BuscarNom():
    Datos = input('Digite el nombre y apellido del beneficiario a buscar:')
    f=open("agenda.txt","r")
    lineas = f.readlines()
    for n in lineas:
        if n==(Datos+'\n'):
            cedula=[lineas[lineas.index(n)+1]]
            cel=[lineas[lineas.index(n)+2]]
            print()
            print(n,end="")
            print(cedula[0],end="")
            print(cel[0])
            break
    f.close()

def Adicionar():
    entradaLogico=open('agenda.txt', 'r')
    print('Digite la información del beneficiario a agregar:')
    Nombre=input()
    cedula=input()
    for linea in entradaLogico:
        linea = linea.rstrip()
        while linea == cedula:
            cedula = input('esta cedula ya existe, digite una nueva: ')
    entradaLogico.close()
    tel= input()
    entradaLogico = open('agenda.txt','a')
    entradaLogico.write('\n'+Nombre)
    entradaLogico.write('\n'+cedula)
    entradaLogico.write('\n'+tel)
    entradaLogico.close()
    print('El beneficiario ha sido agregado')

def Borrar():
    cedula = input('Digite la cedula del beneficiario a borrar:')
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
        print()
        print("El usuario ha sido eliminado del listado")

def ListaCompleta():
    entradaLogico = open('agenda.txt', 'r')
    print("Listado de beneficiarios",end="")
    for linea in entradaLogico:
        linea=linea.rstrip()
        print(linea)
    entradaLogico.close()

def PorLetra():
    letra = input('Digite la letra por la que empiezan los beneficiarios:')
    f=open("agenda.txt","r")
    lineas = f.readlines()
    print()
    print("Listado filtrado de beneficiarios:")
    print(end="")
    for n in lineas:
        if n[0]==letra:
            cedula=[lineas[lineas.index(n)+1]]
            cel=[lineas[lineas.index(n)+2]]
            print(end="")
            print(n,end="")
            print(cedula[0],end="")
            print(cel[0],end="")
    f.close()

f = open('agenda.txt','a')
f.close()
op=menu()
while op != 6:
    if op == 1:
        ListaCompleta()
        op=menu()
    elif op == 2:
        PorLetra()
        op=menu()
    elif op == 3:
        Adicionar()
        op=menu()
    elif op == 4:
        BuscarNom()
        op=menu()
    elif op == 5:
        Borrar()
        op=menu()
print("Hasta pronto")