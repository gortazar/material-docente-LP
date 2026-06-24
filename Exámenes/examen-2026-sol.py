# Ejercicio 1

class Linea:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def total(self):
        return self._precio * self._cantidad


class Ticket:
    def __init__(self, lineas):
        self._lineas = lineas

    def total(self):
        total = 0
        for linea in self._lineas:
            total += linea.total()
        return total

    def total_lineas(self):
        for linea in self._lineas:
            yield linea.total()


l1 = Linea("leche", 0.98, 12)
l2 = Linea("Pan", 0.50, 2)

t = Ticket([l1, l2])
for total in t.total_lineas():
    print(total)

# Ejercicio 2

def convert(lista_original):
    return list(map(lambda i : len(i), lista_original))

print(list(convert([[1, 2], [1, 2, 3]])))

def convert2(lista_original):
    return list(map(len, lista_original))

print(list(convert2([[1, 2], [1, 2, 3]])))



# Test

# 4.
a= {"k": "v"}
for x, y in a.items():
    print(f"({x},{y})")
print(type(a))

# 5.
def inverso(n):
    return 1/n

def wrapper(func, arg):
    return func(arg)

print(wrapper(inverso, 5))

# 8.
a = (1, "Hola", [1, 2, 3])
print(a[2])

# 10
for x in [x**2 for x in (1, 2, 3)]:
    print(x)
