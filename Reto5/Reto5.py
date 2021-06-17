def menu():
    print('BIENVENIDO/A'+'\n'+'Elija Una de las Siguiente Opciones')
    print('1. Buscar numero de telefono segun nombre y apellido')
    print('2. Adicionar un nuevo beneficiario')
    print('3. Borrar un beneficiario de la lista')
    print('4.Listar total de beneficiarios')
    print('5.Listar beneficiarios segun letra determinada')
    print('0.Salir')

def ListaCompleta():
    entradaLogico = open('agenda.txt', 'r')
    for linea in entradaLogico:
        print(linea, end="")
    print()
    entradaLogico.close()

menu()
op = int(input('Usted escoge la opcion:'))
if op == 1:
    print('holi')
elif op == 2:
    entradaLogico = open('agenda.txt', 'a')
elif op == 3:
    print('holi')
elif op == 4:
    ListaCompleta()
elif op == 5:
    print('holi')
else:
    exit()