from classes.periodo import Periodo
from classes.profesor_curso import Profesor_curso
from classes.salon import Salon
from classes.malla import Malla
from classes.curso import Curso
from classes.profesor import Profesor
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Periodo_controller:
    def __init__(self):
        self.periodo = Periodo()
        self.profesor_curso = Profesor_curso()
        self.profesor = Profesor()
        self.malla = Malla()
        self.curso = Curso()
        self.salon = Salon()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Periodos
                ===============
                ''')
                menu = ['Listar periodos', 'Buscar periodo', "Nuevo periodo", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_periodo()
                elif respuesta == 2:
                    self.buscar_periodo()
                elif respuesta == 3:
                    self.insertar_periodo()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_periodo(self):
        print('''
        ========================
            Lista de Periodos
        ========================
        ''')
        periodo = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodo, ['ID', 'Periodo','Inicio','Fin','Estado']))
        input("\nPresione una tecla para continuar...")

    def buscar_periodo(self):
        print('''
        =====================
            Buscar Periodo
        =====================
        ''')
        try:
            id_periodo = input_data("Ingrese el ID del periodo >> ", "int")
            periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
            print(print_table(periodo, ['ID', 'Periodo','Inicio','Fin','Estado']))

            if periodo:
                if pregunta("¿Deseas dar mantenimiento a este periodo?"):
                    opciones = ['Asignar una malla al periodo escolar', 'Editar periodo escolar', 'Eliminar periodo escolar', 'Aperturar periodo escolar', 'Cerrar periodo escolar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.agregar_malla(id_periodo, periodo)
                    elif respuesta == 2:
                        self.editar_periodo(id_periodo)
                    elif respuesta == 3:
                        self.eliminar_periodo(id_periodo)
                    elif respuesta == 4:
                        self.aperturar_periodo(id_periodo)
                    elif respuesta == 5:
                        self.cerrar_periodo(id_periodo)    
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_periodo(self):
        nombre_periodo = input_data("Ingrese el nombre del periodo >> ")
        fecha_desde = input_data("Ingrese desde cuando inicia el periodo >> ")
        fecha_hasta = input_data("Ingrese hasta cuando finaliza el periodo >> ")
        self.periodo.guardar_periodo({
            'nombre_periodo': nombre_periodo,
            'fecha_desde': fecha_desde,
            'fecha_hasta': fecha_hasta
        })
        print('''
        ==============================
            Nuevo Periodo agregado !
        ==============================
        ''')
        self.listar_periodo()

    def editar_periodo(self, id_periodo):
        nombre_periodo = input_data("Ingrese el nuevo nombre del periodo >> ")
        fecha_desde = input_data("Ingrese desde cuando inicia el nuevo periodo >> ")
        fecha_hasta = input_data("Ingrese hasta cuando finaliza el nuevo periodo >> ")
        self.periodo.modificar_periodo({
            'id_periodo': id_periodo
        }, {
            'nombre_periodo': nombre_periodo,
            'fecha_desde': fecha_desde,
            'fecha_hasta': fecha_hasta                  
        })
        print('''
        ========================
            Periodo Editado !
        ========================
        ''')

    def cerrar_periodo(self, id_periodo):
        periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
        if pregunta(f'¿Seguro que desea cerrar el periodo {periodo[1]}?'):                
            self.periodo.modificar_periodo({
                'id_periodo': id_periodo
            }, {
                
                'estado_periodo': 'cerrado'                  
            })
            print('''
            ========================
                Periodo Editado !
            ========================
        ''')        

    def aperturar_periodo(self, id_periodo):
        periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
        if pregunta(f'¿Seguro que desea aperturar el periodo {periodo[1]}?'):                
            self.periodo.modificar_periodo({
                'id_periodo': id_periodo
            }, {
                
                'estado_periodo': 'aperturado'                  
            })
            print('''
            ========================
                Periodo Editado !
            ========================
        ''')      

    def eliminar_periodo(self, id_periodo):
        self.periodo.eliminar_periodo({
            'id_periodo': id_periodo
        })
        print('''
        ========================
            Periodo Eliminado !
        ========================
        ''')

    def agregar_malla(self, id_periodo, periodo):
        print(f'\n Por favor elige el grado o salón para el que desea trabajar su malla curricular :')
        salon_seleccionado=[]
        salones_1=self.salon.obtener_salones('id_salon')
        print(print_table(salones_1,['ID','Salón','Nombre del Salon']))
        id_salon_seleccionado = input_data("Seleccione el ID del salón a trabajar su malla: >> ", "int")
        salon_seleccionado = self.salon.obtener_salon({'id_salon': id_salon_seleccionado})
        print(f'\n Creación de la malla curricular para el periodo : {periodo[1]} y salón: {salon_seleccionado[1]}')
        print(f'''
            =======================================================
                Malla curricular del Salón: {salon_seleccionado[1]}
            =======================================================
        ''')
        #malla_periodo = self.malla.obtener_malla({'id_periodo': id_periodo,'id_salon': id_salon_seleccionado})
        malla_periodo = self.malla.obtener_malla({'id_periodo': id_periodo,'id_salon': id_salon_seleccionado})
        print(print_table(malla_periodo, ['ID', 'ID_Periodo', 'ID_salon', 'ID_Profesor']))
        mallas_imprimir = []        
        if malla_periodo:
            for v in malla_periodo:
                id_malla = v[0]
                id_periodo1 = v[1]
                id_salon1 = v[2]
                id_profesor_curso1 = v[3]
                nomb_periodo = self.periodo.obtener_periodo({
                    'id_periodo': id_periodo1
                })
                if not nomb_periodo:
                    nomb_periodo = ''                
                nomb_salon = self.salon.obtener_salon({
                    'id_salon': id_salon1
                })
                if not nomb_salon:
                    nomb_salon = ''                
                nomb_profesor_curso = self.profesor_curso.obtener_profesor_curso({
                    'id_profesor_curso': id_profesor_curso1           
                })
                if not nomb_profesor_curso:
                    nomb_profesor_curso = ''
                    break                
                nombre_profe = self.profesor.obtener_profesor({
                    'profesor_id': nomb_profesor_curso[1]
                })
                if not nombre_profe:
                    nombre_profe = ''                
                nombre_curso1 = self.curso.obtener_curso({
                    'curso_id' : nomb_profesor_curso[2]
                })
                if not nombre_curso1:
                    nombre_curso1 = ''
                mallas_imprimir.append({
                        'id': id_malla,
                        'Periodo': nomb_periodo[1],
                        'Salon': nomb_salon[1],
                        'Profesor': nombre_profe[1],
                        'Curso': nombre_curso1[1],
                        'Codigo_curso_profe': id_profesor_curso1
                })
            print(print_table(mallas_imprimir))

            if pregunta(f'¿Deseas ver la relación de cursos dictados por profesores?'):                
                curso_profe_1=self.profesor_curso.obtener_profesor_cursos('id_profesor_curso')
                print(print_table(curso_profe_1,['ID','Profesor','Curso']))
                
            else: 
                curso_profe_1=[]
            id_curso_profe_seleccionado = input_data("Seleccione el código profesor curso : >> ", "int")
            self.malla.guardar_malla({
                'id_periodo'    :   id_periodo,
                'id_salon'  :   id_salon_seleccionado,
                'id_profesor_curso' :   id_curso_profe_seleccionado
            })
            print('''
                ==============================
                    Malla agregada !
                ==============================
            ''')

