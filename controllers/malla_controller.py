from classes.malla import Malla
from classes.periodo import Periodo
from classes.salon import Salon
from classes.profesor_curso import Profesor_curso
from controllers.periodo_controller import Periodo_controller
from controllers.salon_controllers import Salon_controller
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Malla_controller:
    def __init__(self):
        self.malla = Malla()
        self.periodo = Periodo()
        self.salon = Salon()
        self.profesor_curso = Profesor_curso()

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Malla
                =============
                ''')
                menu = ['Listar malla', 'Buscar malla', "Nueva malla", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_mallas()
                elif respuesta == 2:
                    self.buscar_malla()
                elif respuesta == 3:
                    self.insertar_malla()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_mallas(self):
        print('''
        ========================
            Lista de Mallas
        ========================
        ''')
        mallas = self.malla.obtener_mallas('malla_id')
        print(print_table(mallas, ['ID', 'ID Periodo', 'ID Salon', 'ID Profesor-Curso']))
        input("\nPresione una tecla para continuar...")

    def buscar_malla(self):
        print('''
        ===========================
            Buscar Malla
        ===========================
        ''')
        try:
            id_malla = input_data("Ingrese el ID de la malla >> ", "int")
            malla = self.malla.obtener_malla({'malla_id': id_malla})
            print(print_table(malla, ['ID', 'ID Periodo', 'ID Salon', 'ID Profesor-Cursor']))

            if malla:
                if pregunta("¿Deseas dar mantenimiento a la malla?"):
                    opciones = ['Editar malla', 'Eliminar malla', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_malla(id_malla)
                    elif respuesta == 2:
                        self.eliminar_malla(id_malla)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_malla(self, id_malla):
        id_periodo = input_data("Ingrese el nuevo ID Periodo >> ")
        id_salon = input_data("Ingrese el nuevo ID Salon >> ")
        id_profesor_curso = input_data("Ingrese el nuevo ID Profesor-Curso >> ")
        self.malla.modificar_malla({
            'malla_id': id_malla
        }, {
            'id_periodo': id_periodo,
            'id_salon': id_salon,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        ==========================
            Malla Editada !
        ==========================
        ''')

    def eliminar_malla(self, id_malla):
        self.malla.eliminar_malla({
            'malla_id': id_malla
        })
        print('''
        ===========================
            Malla Eliminada !
        ===========================
        ''')

    def listar_profesor_cursos(self):
        print('''
        ==================================================
            Lista de Asignaciones del Profesor a Curso
        ==================================================
        ''')
        profesor_cursos = self.profesor_curso.obtener_profesor_cursos('profesor_curso_id')
        print(print_table(profesor_cursos, ['ID', 'ID Profesor', 'ID Curso']))

    def insertar_malla(self):
        self.listar_periodos()
        id_periodo = input_data("Ingrese el ID del Periodo en el se habilitará la nueva malla >> ")
        self.listar_salones()
        id_salon = input_data("Ingrese el ID del Salón al que asignara el curso con el respctivo profesor >> ")
        self.listar_profesor_cursos()
        id_profesor_curso = input_data("Ingrese el ID del Profesor-Curso que asignará al Salón ya seleccionado >> ")
        self.malla.guardar_malla({
            'id_periodo': id_periodo,
            'id_salon': id_salon,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        =================================
            Nueva Malla Generada !
        =================================
        ''')
        self.listar_mallas()