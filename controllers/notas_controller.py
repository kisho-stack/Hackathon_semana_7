from classes.periodo import Periodo
from classes.profesor_curso import Profesor_curso
from classes.salon import Salon
from classes.malla import Malla
from classes.curso import Curso
from classes.profesor import Profesor
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from classes.alumno import Alumno
from classes.nota import Nota

class Notas_controller:
    def __init__(self):
        self.alumno = Alumno()
        self.curso = Curso()
        self.profesor_curso = Profesor_curso()
        self.periodo = Periodo()
        self.nota = Nota()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===================
                    Notas
                ===================
                ''')
                menu = ['Listar notas',  "Buscar notas", "Nueva nota", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_notas()
                elif respuesta == 2:
                    self.buscar_notas()
                elif respuesta == 3:
                    self.insertar_notas()    
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_notas(self):
        print('''
        ===========================
            Lista de Notas
        ===========================
        ''')
        notas = self.nota.obtener_notas('id_nota')
        print(print_table(notas, ['ID', 'Alumno', 'Malla', 'Nota']))
        input("\nPresione una tecla para continuar...")

    def buscar_notas(self):
        print('''
        ===========================
             Buscar Notas
        ===========================
        ''')
        try:
            id_notas = input_data("Ingrese el ID de la nota>> ", "int")
            notas = self.nota.obtener_nota({'id_nota': id_notas})
            print(print_table(notas, ['ID', 'Alumno', 'Malla', 'Nota']))

            if notas:
                if pregunta(f"¿Deseas dar mantenimiento al registro notas '{notas[0]}'?"):
                    opciones = ['Editar notas', 'Eliminar nota', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_notas()
                    elif respuesta == 2:
                        self.eliminar_notas(id_nota)  
                    
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_notas(self):
        id_alumno = input_data("Ingrese el ID del alumno >> ", "int")
        alumno = self.alumno.obtener_alumno({'alumno_id': id_alumno})
        print(print_table(alumno, ['ID', 'Nombre', 'Edad', 'Correo']))
        
        id_curso = input_data("Ingrese el ID del curso >> ", "int")
        curso = self.curso.obtener_curso({'curso_id': id_curso})
        print(print_table(curso, ['ID', 'Nombre']))
            
        id_malla = input_data("Ingrese el ID de la malla >> ", "int")
        malla = self.malla.obtener_malla({'malla_id': id_malla})
        print(print_table(malla, ['ID', 'ID Periodo', 'ID Salon', 'ID Profesor-Cursor']))
                    
        nota = input_data("Ingrese nota del alumno >> ")
        self.nota.guardar_nota({
            'id_alumno': id_alumno,
            'id_malla': id_malla,
            'nota': nota
        })
        print('''
        =================================
         La nota se registro con exito !
        =================================
        ''')
        self.listar_notas()

    def editar_notas(self):
        id_nota = input_data("Ingrese el id de la nota a modificar >> ")
        nota = input_data("Ingrese la nueva nota del alumno  >> ")
        self.nota.modificar_nota({
            'id_nota' : id_nota
            
        }, {
            'nota': nota
           
        })
        print('''
        ==========================
            Nota Editada !
        ==========================
        ''')

    def eliminar_notas(self,id_nota):
        self.nota.eliminar_nota({
            'id_nota': id_nota
        })
        print('''
        ===========================
            Nota Eliminada !
        ===========================
        ''')
    
    
        