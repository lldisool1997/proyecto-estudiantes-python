class Estudiante:
    def __init__(self, id, nombre_completo, dni, edad):
        self.id = id
        self.nombre_completo = nombre_completo
        self.dni = dni
        self.edad = edad

    def editar_datos(self, nombre_completo, dni, edad):
        self.nombre_completo = nombre_completo
        self.dni = dni
        self.edad = edad

    def mostrar_datos(self):
        print(f"ID: {self.id}, Nombre: {self.nombre_completo}, DNI: {self.dni}, Edad: {self.edad}")