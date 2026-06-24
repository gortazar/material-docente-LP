# Ejercicio 1

mis_multiplos = [x*3 for x in range(1,16)]
print(mis_multiplos)


# Ejercicio 4

class Paquete:
    def __init__(self, dir, remite, peso):
        self._dir = dir
        self._remite = remite
        self._peso = peso

class Camion:
    def __init__(self, matricula, capacidad):
        self._matricula = matricula
        self._capacidad = capacidad

    def add_paquetes(self, paquetes):
        pesos = map(lambda p: p._peso, paquetes)
        if(sum(pesos) > self._capacidad):
            raise ValueError("El peso excede la capacidad del camión")
        self._paquetes = paquetes

    def ciudades(self):
        for p in self._paquetes:
            yield p._dir

p1 = Paquete("Madrid", "Pamplona", 40, 35.6)
p2 = Paquete("Ciudad Real", "Albacete", 80, 75.6)

c = Camion("0000mna", 130)

c.add_paquetes([p1, p2])

for ciudad in c.ciudades():
    print(ciudad)