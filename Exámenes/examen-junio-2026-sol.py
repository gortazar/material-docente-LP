# Ejercicio 1 (3 puntos)

class Vehiculo:
    def __init__(self, nombre: str, consumo: float, km: float):
        self.nombre = nombre
        self.consumo = consumo
        self.km = km
    
    def gasolina_gastada(self) -> float:
        return (self.km * self.consumo) / 100

class Flota:
    def __init__(self, lista_vehiculos: list[Vehiculo]):
        self.vehiculos = lista_vehiculos

    def generar_informe_consumos(self):
        for v in self.vehiculos:
            yield v.gasolina_gastada()


# Ejercicio 2 (3 puntos)

def convert_comprehension(precios):
    return [p * 1.21 for p in precios if p > 10]

#####################

v1 = Vehiculo("v1", 12, 1230)
v2 = Vehiculo("v2", 9.8, 2345)

flota = Flota([v1, v2])

for gasto in flota.generar_informe_consumos():
    print(gasto)



print(convert_comprehension([8.7, 12.8]))