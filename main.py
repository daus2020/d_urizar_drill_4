from vehiculo import *
# from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

# import re


# option 1:
def part_1():
    instances = []

    qty_ins = int(input('Cuántos Vehículos desea insertar: '))
    print('')

    for i in range(qty_ins):
        print(f'Datos del automóvil {i + 1}')
        marca = input('Inserte la marca del automóvil: ')
        modelo = input('Inserte el modelo: ')
        nro_ruedas = int(input('Inserte el número de ruedas: '))
        velocidad = int(input('Inserte la velocidad en km/h: '))
        cilindrada = int(input('Inserte el cilindraje en cc: '))
        print('')
        car = Automovil(velocidad, cilindrada, marca, modelo, nro_ruedas)
        instances.append(car)

    print('\nImprimiendo por pantalla los vehículos:\n')

    for i, item in enumerate(instances):
        print(f'Datos del automóvil {i + 1} : {item}')

    # 1 : Marca Toyota, Modelo Yaris, 4 ruedas 120 Km/h, 800 cc
    # 2 : Marca Fiat, Modelo Palio, 4 ruedas 95 Km/h, 1200 cc
    # 3 : Marca Ford, Modelo Fiesta, 4 ruedas 125 Km/h, 1500 cc


# option 2:
def part_2():
    particular = Particular(5,  "180", "500", "Ford", "Fiesta", 4)
    # Particular(nro_puestos, velocidad, cilindrada, marca, modelo, nro_ruedas)

    carga = Carga("20000", 120, "10000", "Daft Trucks", "G 38", 10)
    # Carga(carga, velocidad, cilindrada, marca, modelo, nro_ruedas)

    bicicleta = Bicicleta("Carrera", "Shimano", "MT Ranger", 2)
    # Bicicleta(tipo, marca, modelo, nro_ruedas)

    motocicleta = Motocicleta("2T", "Doble Viga", 21,
                              "Deportiva", "BMW", "F800s", 2)
    # Motocicleta(motor, marco, nro_radios, tipo, marca, modelo, nro_ruedas)

    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    print('\nMotocicleta es instancia con relación a Vehículo: ',
          isinstance(motocicleta, Vehiculo))
    print('Motocicleta es instancia con relación a Automovil: ',
          isinstance(motocicleta, Automovil))
    print('Motocicleta es instancia con relación a Vehículo particular: ',
          isinstance(motocicleta, Particular))
    print('Motocicleta es instancia con relación a Vehículo de Carga: ',
          isinstance(motocicleta, Carga))
    print('Motocicleta es instancia con relación a Bicicleta: ',
          isinstance(motocicleta, Bicicleta))
    print('Motocicleta es instancia con relación a Motocicleta: ',
          isinstance(motocicleta, Motocicleta))


# option 3.1 guardar_datos_csv:
def part_3_1():
    # instance = Particular(nro_puestos, velocidad, cilindrada, marca, modelo, nro_ruedas)
    particular = Particular(5,  "180", "500", "Ford", "Fiesta", 4)

    # inst = Carga(carga, velocidad, cilindrada, marca, modelo, nro_ruedas)
    carga = Carga("20000", 120, "10000", "Daft Trucks", "G 38", 10)

    bicicleta = Bicicleta("Carrera", "Shimano", "MT Ranger", 2)
    # Bicicleta(tipo, marca, modelo, nro_ruedas)

    motocicleta = Motocicleta("2T", "Doble Viga", 21,
                              "Deportiva", "BMW", "F800s", 2)
    # Motocicleta(motor, marco, nro_radios, tipo, marca, modelo, nro_ruedas)

    particular.guardar_datos_csv()
    carga.guardar_datos_csv()
    bicicleta.guardar_datos_csv()
    motocicleta.guardar_datos_csv()


# option 3.2 leer_datos_csv:
def part_3_2():
    # instance = Particular(nro_puestos, velocidad, cilindrada, marca, modelo, nro_ruedas)
    particular = Particular(5,  "180", "500", "Ford", "Fiesta", 4)

    # inst = Carga(carga, velocidad, cilindrada, marca, modelo, nro_ruedas)
    carga = Carga("20000", 120, "10000", "Daft Trucks", "G 38", 10)

    bicicleta = Bicicleta("Carrera", "Shimano", "MT Ranger", 2)
    # Bicicleta(tipo, marca, modelo, nro_ruedas)

    motocicleta = Motocicleta("2T", "Doble Viga", 21,
                              "Deportiva", "BMW", "F800s", 2)
    # Motocicleta(motor, marco, nro_radios, tipo, marca, modelo, nro_ruedas)

    leer_datos_csv()

    # Vehiculo.leer_datos_csv()  --> if static method is inside class Vehiculo

    # Alt. 2 (profe) uncomment to use it and comment line 100 and 117 to 146 in vehiculo.py
    # particular.leer_datos_csv()
    # carga.leer_datos_csv()
    # bicicleta.leer_datos_csv()
    # motocicleta.leer_datos_csv()

    # Alt. 3 (variacion profe usando list comprehension)
    # instances = [particular, carga, bicicleta, motocicleta]
    # [item .leer_datos_csv() for item in instances]


def menu():
    print("\n              \033[4mMENU\033[0m")
    print("  1 > Parte 1 - Ingreso de vehiculos")
    print("  2 > Parte 2 - Muestra instancias")
    print("  3 > Parte 3.1 - Guardar datos csv")
    print("  4 > Parte 3.2 - Leer datos csv")
    print("  5 > Salir")


def get_option():
    while True:
        menu()
        options = tuple(range(1, 6))
        my_option = int(input("Ingrese una opción del 1 al 5: "))

        if my_option in options:
            break
        else:
            print("Opción ingresada no válida (1 al 5). Intente nuevamente")

    return my_option


while True:
    my_option = get_option()
    print("\n")
    choices = [my_option, part_1, part_2, part_3_1, part_3_2, exit]
    choices[my_option]()
