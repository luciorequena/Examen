import statistics

vec = []

i = 0
borrar = 1
sumar = 2
opcion = 1

if not vec:
    for i in range(3):
        valor = int(input("Escriba el valor {0}:".format(i+1)))
        vec.append(valor)
else:
    print("El vector ya está lleno.")

print(vec)

while opcion != 0:
    print("Para borrar el primer dato ingresado ingrese 1.")
    print("Para mostrar el valor anterior y posterior ingrese 2.")
    print("Para ordenar el vector de menor a mayor ingrese 3.")
    print("Para calcular el promedio de los vectores ingrese 4.")
    print("Para mostrar el valor menor y el valor mayor ingrese 5.")
    print("Para cerrar el programa ingrese 0.")
    opcion = int(input())

    if opcion == 1:
        if not vec:
            print("El vector está vacio")
        else:
            del vec[0]
            print("Valor eliminado.")
            print(vec)

    if opcion == 2:
        print("Posicion anterior:",vec[0])
        print("Posicion posterior:",vec[2]) 

    if opcion == 3:
        vec.sort()
        print(vec)

    if opcion == 4:
        prom = statistics.mean(vec)
        print(prom)
        if vec[0] < prom:
            print("El primer valor es menor al promedio.")
        else:
            print("El primer valor es mayor al promedio.")

        if vec[2] < prom:
            print("El tercer valor es menor al promedio.")
        else:
            print("El tercer valor es mayor al promedio.")

    if opcion == 5:
        if vec[0] > vec[1] and vec[0] > vec[2]:
            print("El número mayor es: ",vec[0])

        if vec[1] > vec[0] and vec[1] > vec[2]:
            print("El número mayor es: ",vec[1])

        if vec[2] > vec[0] and vec[2] > vec[1]:
            print("El número mayor es: ",vec[2])