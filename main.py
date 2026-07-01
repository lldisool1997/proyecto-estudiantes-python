from app.aplicacion import Aplicacion


class Main:
    def __init__(self):
        self.aplicacion = Aplicacion()
    
    def ejecutar(self):
        self.aplicacion.mostrar_menu()
    
main = Main()
main.ejecutar()
