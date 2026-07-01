from app.modelos.estudiante import Estudiante

class Aplicacion:
    def __init__(self):
        self.estudiantes = []

    def mostrar_menu(self):
        print("Bienvenido a la aplicación de gestión de estudiantes")
        salir = False
        while salir == False:

            print("1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Editar estudiantes")
            print("4. Eliminar Estudiante")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_estudiante()
            elif opcion == "2":
                self.mostrar_estudiantes()
            elif opcion == "3":
                self.editar_estudiante()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                salir = True
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def existen_estudiantes(self): #len(self.estudiantes) = 2 > 0 -> True
        return len(self.estudiantes) > 0

    def agregar_estudiante(self):
        print("Por favor ingrese los datos del estudiante")
        nombre_completo = input("Nombre Completo: ")
        dni = input("DNI: ")
        edad = input("Edad: ")

        estudiante = Estudiante(len(self.estudiantes) + 1, nombre_completo, dni, edad)
        self.estudiantes.append(estudiante)
        
    def mostrar_estudiantes(self):
        if self.existen_estudiantes() == False:
            print("No hay estudiantes registrados.")
        else:
            print("Lista de estudiantes:")
            for estudiante in self.estudiantes:
                estudiante.mostrar_datos()
    
    def editar_estudiante(self):
        if self.existen_estudiantes() == False:
            print("No hay estudiantes registrados.")

        print("Ingrese el ID del estudiante que desea editar:")   
        id_estudiante = input("ID: ") 
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()
            if int(estudiante.id) == int(id_estudiante):
                print("Por favor ingrese los datos del estudiante")
                nombre_completo = input("Nombre Completo: ")
                dni = input("DNI: ")
                edad = input("Edad: ")    
                estudiante.editar_datos(nombre_completo, dni, edad)


