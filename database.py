from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_cursos(self):        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  cursos(
                curso_id SERIAL,
                nombre character varying(150) COLLATE pg_catalog."default",
                CONSTRAINT cursos_pkey PRIMARY KEY (curso_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_malla_curricular(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  malla_curricular(
                id_malla SERIAL,
                id_periodo integer NOT NULL,
                id_salon integer NOT NULL,
                id_profesor_curso integer NOT NULL,
                CONSTRAINT malla_curricular_pkey PRIMARY KEY (id_malla)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_notas(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  notas(
                id_nota SERIAL,
                id_alumno integer NOT NULL,
                id_malla integer NOT NULL,
                nota double precision NOT NULL,
                CONSTRAINT notas_pkey PRIMARY KEY (id_nota)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_periodo_escolar(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  periodo_escolar(
                id_periodo SERIAL,
                nombre_periodo character varying(150) COLLATE pg_catalog."default",
                fecha_desde date,
                fecha_hasta date,
                estado_periodo varchar(25) DEFAULT 'aperturado',
                CONSTRAINT periodo_escolar_pkey PRIMARY KEY (id_periodo)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_profesor_curso(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesor_curso(
                id_profesor_curso SERIAL,
                id_profesor integer NOT NULL,
                id_curso integer NOT NULL,
                CONSTRAINT profesor_curso_pkey PRIMARY KEY (id_profesor_curso)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_profesor_salon(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesor_salon(
                id_profesor_salon SERIAL,
                id_profesor integer NOT NULL,
                id_salon integer NOT NULL,
                CONSTRAINT profesor_salon_pkey PRIMARY KEY (id_profesor_salon)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)


    def crear_profesores(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesores(
                profesor_id SERIAL,
                nombres character varying(150) COLLATE pg_catalog."default",
                edad integer,
                correo character varying(150) COLLATE pg_catalog."default",
                CONSTRAINT profesores_pkey PRIMARY KEY (profesor_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_alumnos(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  alumnos(
                alumno_id SERIAL,
                nombres character varying(150) COLLATE pg_catalog."default",
                edad integer,
                correo character varying(150) COLLATE pg_catalog."default",
                CONSTRAINT alumnos_pkey PRIMARY KEY (alumno_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_salones(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  salones(
                id_salon SERIAL,
                grado_salon character varying(150) NOT NULL,
                nombre_salon character varying(150) COLLATE pg_catalog."default" NOT NULL,
                CONSTRAINT salones_pkey PRIMARY KEY (id_salon)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
    def insert_salones(self):
        create_table_query ='''
            INSERT INTO salones (
                id_salon,grado_salon,nombre_salon
            )
            VALUES (1,'1ro Primaria','Esperanza'),(2,'2do Primaria','Amor'),(3,'3ro Primaria','Gratitud'),
                   (4,'4to Primaria','Fuerza'),(5,'5to Primaria','Honor'),(6,'6to Primaria','Honor'),
                   (7,'1ro Secundaria','Responsabilidad'),(8,'2do Secundaria','Respeto'),(9,'3ro Secundaria','Libertad'),
                   (10,'4to Secundaria','Justicia'),(11,'5to Secundaria','Honestidad')
            
        '''
        conn.ejecutar_sentencia(create_table_query)    
    

conn = Conexion('sistema_colegio')
db= Database(conn)
db.crear_cursos()
db.crear_malla_curricular()
db.crear_notas()
db.crear_periodo_escolar()
db.crear_profesor_curso()
db.crear_profesor_salon()
db.crear_profesores()
db.crear_alumnos()
db.crear_salones()
db.insert_salones()