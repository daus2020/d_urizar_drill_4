import csv
import re


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = int(nro_ruedas)

    def guardar_datos_csv(self):
        try:
            with open('vehiculos.csv', 'a') as archivo:
                # with open('vehiculos.csv', 'a', newline='') as archivo:
                data = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(data)

        except FileNotFoundError:
            print('Archivo vehiculos.csv no existe')

        except Exception as e:
            print('Error: ', e)

    def leer_datos_csv(self):
        try:
            with open('vehiculos.csv', 'r') as archivo:
                vehiculos = csv.reader(archivo)
                print(f'Lista de Vehiculos {type(self).__name__}')

                for item in vehiculos:
                    # obs.: class_name is between . and '
                    class_name = re.match(
                        r"^.*\.(.*)'.*$", item[0]).group(1)
                    if class_name == type(self).__name__:
                        print(item[1])
                print('')

        except FileNotFoundError:
            print('Archivo vehiculos.csv no existe')
        except Exception as e:
            print('Error: ', e)

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas'


class Automovil(Vehiculo):
    def __init__(self, velocidad, cilindrada, *args):
        super(Automovil, self).__init__(*args)
        self.velocidad = int(velocidad)
        self.cilindrada = int(cilindrada)

    def __str__(self):
        return super().__str__() + f', {self.velocidad} Km/h, ' + f'{self.cilindrada:,} cc'.format(self.cilindrada).replace(',', '.')


class Particular(Automovil):
    def __init__(self, nro_puestos, *args):
        super(Particular, self).__init__(*args)
        self.nro_puestos = int(nro_puestos)

    def get_nro_puestos(self):
        return self.nro_puestos

    def set_nro_puestos(self, new_nro_puestos):
        self.nro_puestos = new_nro_puestos

    def __str__(self):
        return super().__str__() + f', Puestos: {self.nro_puestos}'


class Carga(Automovil):
    def __init__(self, carga, *args):
        super(Carga, self).__init__(*args)
        self.carga = int(carga)

    def get_carga(self):
        return self.carga

    def set_carga(self, new_carga):
        self.carga = new_carga

    def __str__(self):
        return super().__str__() + ', ' + f'Carga: {self.carga:,} Kg'.format(self.carga).replace(',', '.')


class Bicicleta(Vehiculo):
    def __init__(self, tipo, *args):
        super().__init__(*args)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, new_tipo):
        self.tipo = new_tipo

    def __str__(self):
        return super().__str__() + f', Tipo: {self.tipo}'


class Motocicleta(Bicicleta):
    def __init__(self, motor, cuadro, nro_radios, *args):
        super(Motocicleta, self).__init__(*args)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = int(nro_radios)

    def get_nro_radios(self):
        return self.nro_radios

    def set_nro_radios(self, new_nro_radios):
        self.nro_radios = new_nro_radios

    def __str__(self):
        return super().__str__() + f', Motor: {self.motor}, Cuadro: {self.cuadro}, Nro. Radios: {self.nro_radios}'
