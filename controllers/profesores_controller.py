from classes.profesor import Profesor
from classes.curso import Curso
from classes.profesor_curso import Profesor_curso
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta
from classes.salon import Salon
from classes.profesor_salon import Profesor_salon

class Profesores_controller:
    def __init__(self):
        self.profesor = Profesor()
        self.curso = Curso()
        self.profesor_curso = Profesor_curso()
        self.salon = Salon()
        self.profesor_salon = Profesor_salon()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===================
                    Profesores
                ===================
                ''')
                menu = ['Listar profesores', 'Buscar profesor', "Nuevo profesor", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_profesores()
                elif respuesta == 2:
                    self.buscar_profesor()
                elif respuesta == 3:
                    self.insertar_profesor()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_profesores(self):
        print('''
        ===========================
            Lista de Profesores
        ===========================
        ''')
        profesores = self.profesor.obtener_profesores('profesor_id')
        print(print_table(profesores, ['ID', 'Nombre', 'Edad', 'Correo']))
        input("\nPresione una tecla para continuar...")

    def buscar_profesor(self):
        print('''
        ===========================
            Buscar Profesor
        ===========================
        ''')
        try:
            id_profesor = input_data("Ingrese el ID del profesor >> ", "int")
            profesor = self.profesor.obtener_profesor({'profesor_id': id_profesor})
            print(print_table(profesor, ['ID', 'Nombre', 'Edad', 'Correo']))

            if profesor:
                if pregunta(f"¿Deseas dar mantenimiento al registro profesor '{profesor[1]}'?"):
                    opciones = ['Asignar curso','Asignar salon','Editar profesor', 'Eliminar profesor', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.asignar_curso(id_profesor, profesor)
                    elif respuesta == 2:
                        self.asignar_salon(id_profesor, profesor)
                    elif respuesta == 3:
                        self.editar_profesor(id_profesor)
                    elif respuesta == 4:
                        self.eliminar_profesor(id_profesor)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_profesor(self):
        nombre = input_data("Ingrese el nombre del profesor >> ")
        edad = input_data("Ingrese la edad del profesor >> ")
        correo = input_data("Ingrese el correo del profesor >> ")
        self.profesor.guardar_profesor({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        =================================
            Nuevo Profesor agregado !
        =================================
        ''')
        self.listar_profesores()

    def editar_profesor(self, id_profesor):
        nombre = input_data("Ingrese el nuevo nombre del profesor >> ")
        edad = input_data("Ingrese la nueva edad del profesor >> ")
        correo = input_data("Ingrese el nuevo correo del profesor >> ")
        self.profesor.modificar_profesor({
            'profesor_id': id_profesor
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ==========================
            Profesor Editado !
        ==========================
        ''')

    def eliminar_profesor(self, id_profesor):
        self.profesor.eliminar_profesor({
            'profesor_id': id_profesor
        })
        print('''
        ===========================
            Profesor Eliminado !
        ===========================
        ''')

    def asignar_curso(self, id_profesor, profesor):
        print(f'\n Asignación de cursos para el profesor : {profesor[1]}')
        print('''
            ============================
                Curso disponibles
            ============================
        ''')
        cursos = self.curso.obtener_cursos('curso_id')
        cursos_disponibles = []
        
        if cursos:
            for curso in cursos:
                id_curso = curso[0]
                nombre_curso = curso[1]
                cursos_profesor = self.profesor_curso.buscar_profesor_cursos({
                    'id_profesor': id_profesor,
                    'id_curso': id_curso
                })
                if not cursos_profesor:
                    cursos_disponibles.append({
                        'id': id_curso,
                        'Cursos disponibles': nombre_curso
                    })

            print(print_table(cursos_disponibles))
            curso_seleccionado = input_data(f'\nSeleccione el ID del curso a asignar al profesor: {profesor[1]} >> ', 'int')
            buscar_curso = self.curso.obtener_curso({'curso_id': curso_seleccionado})
            if not buscar_curso:
                print('\nEste curso no existe !')
                return
            cursos_profesor = self.profesor_curso.buscar_profesor_cursos({
                'id_profesor': id_profesor,
                'id_curso': curso_seleccionado
            })
            if cursos_profesor:
                print('\nEste curso ya esta asignado al profesor !')
                return
            self.profesor_curso.guardar_profesor_curso({
                'id_profesor': id_profesor,
                'id_curso': curso_seleccionado
            })
            print('''
                ==============================
                    Nuevo curso asignado !
                ==============================
            ''')
            
    def asignar_salon(self, id_profesor, profesor):
        print(f'\n Asignación de salones para el profesor : {profesor[1]}')
        print('''
            ============================
                Salones disponibles
            ============================
        ''')
        salon = self.salon.obtener_salones('id_salon')
        salon_disponibles = []
        
        if salon:
            for salones in salon:
                id_salon = salones[0]
                grado_salon = salones[1]
                nombre_salon = salones[2]
                salon_profesor = self.profesor_salon.buscar_profesor_salones({
                    'id_profesor': id_profesor,
                    'id_salon': id_salon
                })
                if not salon_profesor:
                    salon_disponibles.append({
                        'id': id_salon,
                        'Salones disponibles': grado_salon,
                        'Nombre Salon' : nombre_salon
                    })

            print(print_table(salon_disponibles))
            
            salon_seleccionado = input_data(f'\nSeleccione el ID del salon a asignar al profesor: {profesor[1]} >> ', 'int')
            buscar_salon = self.salon.obtener_salon({'id_salon': salon_seleccionado})
            if not buscar_salon:
                print('\nEste curso no existe !')
                return
            salon_profesor = self.profesor_salon.buscar_profesor_salones({
                'id_profesor': id_profesor,
                'id_salon': salon_seleccionado
            })
            if salon_profesor:
                print('\nEste curso ya esta asignado al profesor !')
                return
            self.profesor_salon.guardar_profesor_salon({
                'id_profesor': id_profesor,
                'id_salon': salon_seleccionado
            })
            print('''
                ==============================
                    Nuevo salon asignado !
                ==============================
            ''')
        