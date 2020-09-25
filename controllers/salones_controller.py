
from classes.salon import Salon
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Salones_controller:
    def __init__(self):
        self.salones = Salon()
        

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Salones
                =============
                ''')
                menu = ['Listar Salones', 'Buscar Salones', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_salones()
                elif respuesta == 2:
                    self.buscar_salones()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

           
    def listar_salones(self):
        print('''
        ========================
            Lista de Salones
        ========================
        ''')
        salon = self.salones.obtener_salones('id_salon')
        print(print_table(salon, ['ID','Grado', 'Nombre Salon']))
        input("\nPresione una tecla para continuar...")

    def buscar_salones(self):
        print('''
        ===========================
            Buscar Salon
        ===========================
        ''')
        try:
            id_salon = input_data("Ingrese el ID del salon>> ", "int")
            salon = self.salones.obtener_salon({'id_salon': id_salon})
            print(print_table(salon, ['ID', 'Nombre Salon']))

           
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    