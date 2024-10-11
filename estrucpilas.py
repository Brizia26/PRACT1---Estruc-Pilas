class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertar({elemento}): {self.pila} | Tope = {self.tope}")
        else:
            print("Error: La pila está llena. No se puede insertar.")

    def eliminar(self):
        if self.tope > 0:
            elemento_eliminado = self.pila.pop()
            self.tope -= 1
            print(f"Eliminar(): {self.pila} | Tope = {self.tope}")
            return elemento_eliminado
        else:
            print("Error: La pila está vacía. No se puede eliminar.")

# Crear una pila con capacidad para 8 elementos
pila = Pila(8)

# Realizar las operaciones especificadas
pila.insertar("X")  # a. Insertar X
pila.insertar("Y")  # b. Insertar Y
pila.eliminar()     # c. Eliminar Z
pila.eliminar()     # d. Eliminar T
pila.eliminar()     # e. Eliminar U
pila.insertar("V")  # f. Insertar V
pila.insertar("W")  # g. Insertar W
pila.eliminar()     # h. Eliminar P
pila.insertar("R")  # i. Insertar R
