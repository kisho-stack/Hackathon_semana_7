from classes.alumno import Alumno
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class alumnos_controller():
    def __init__(self):
        self.alumno = Alumno()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===================
                    Alumnos
                ===================
                ''')
                menu = ['Listar alumnos', 'Buscar alumno', "Nuevo alumno", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_alumnos()
                elif respuesta == 2:
                    self.buscar_alumno()
                elif respuesta == 3:
                    self.insertar_alumno()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_alumnos(self):
        print('''
        ===========================
            Lista de Alumnos
        ===========================
        ''')
        alumnos = self.alumno.obtener_alumnos('alumno_id')
        print(print_table(alumnos, ['ID', 'Nombre', 'Edad', 'Correo']))
        input("\nPresione una tecla para continuar...")
    def buscar_alumno(self):
        print('''
        ===========================
            Buscar Alumno
        ===========================
        ''')
        try:
            id_alumno = input_data("Ingrese el ID del alumno >> ", "int")
            alumno = self.alumno.obtener_alumno({'alumno_id': id_alumno})
            print(print_table(alumno, ['ID', 'Nombre', 'Edad', 'Correo']))

            if alumno:
                if pregunta("¿Deseas dar mantenimiento a la lista de alumnos?"):
                    opciones = ['Editar alumno', 'Eliminar alumno', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_alumno(id_alumno)
                    elif respuesta == 2:
                        self.eliminar_alumno(id_alumno)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    def insertar_alumno(self):
        nombre = input_data("Ingrese el nombre del alumno >> ")
        edad = input_data("Ingrese la edad del alumno >> ")
        correo = input_data("Ingrese el correo del alumno >> ")
        self.alumno.guardar_alumno({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        =================================
            Nuevo Alumno agregado !
        =================================
        ''')
        self.listar_alumnos()

    def editar_alumno(self, id_alumno):
        nombre = input_data("Ingrese el nuevo nombre del alumno >> ")
        edad = input_data("Ingrese la nueva edad del alumno >> ")
        correo = input_data("Ingrese el nuevo correo del alumno >> ")
        self.alumno.modificar_alumno({
            'alumno_id': id_alumno
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ===================================
            Datos del Alumno Editado !
        ===================================
        ''')
    def eliminar_alumno(self, id_alumno):
        self.alumno.eliminar_alumno({
            'alumno_id': id_alumno
        })
        print('''
        ========================
            Alumno Eliminado !
        ========================
        ''')

