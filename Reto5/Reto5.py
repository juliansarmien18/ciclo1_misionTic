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

def Adicionar():
    entradaLogico=open('agenda.txt', 'r')
    Nombre=input('digite nombre del nuevo usuario:')
    cedula=input('Digite cedula del nuevo beneficiario:')
    for linea in entradaLogico:
        while linea == cedula+'\n':
            cedula = input('esta cedula ya existe, digite una nueva: ')
    entradaLogico.close()
    tel= input('Digite numero de telefono del nuevo beneficiario: ')
    entradaLogico = open('agenda.txt','a')
    entradaLogico.write('\n'+'\n'+Nombre)
    entradaLogico.write('\n'+cedula)
    entradaLogico.write('\n'+tel)
    entradaLogico.close()
    print('se adiciono el nuevo beneficiario')

def ListaCompleta():
    entradaLogico = open('agenda.txt', 'r')
    for linea in entradaLogico:
        print(linea, end="")
    print()
    entradaLogico.close()

op=menu()
while op != 0:
    if op == 1:
        print('holi')
        op=menu()
    elif op == 2:
        Adicionar()
        print()
        op=menu()
    elif op == 3:
        print('holi')
        op=menu()
    elif op == 4:
        ListaCompleta()
        print()
        op=menu()
    elif op == 5:
        print('holi')
        op=menu()
    else:
        exit()