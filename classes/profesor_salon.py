from connection.conn import Conexion

class Profesor_salon:
    def __init__(self):
        self.model = Conexion('profesor_salon')

    def guardar_profesor_salon(self, profesor_salon):
        return self.model.insert(profesor_salon)

    def obtener_profesor_salon(self, id_profesor_salon):
        return self.model.get_by_id(id_profesor_salon)

    def obtener_profesor_salones(self, order):
        return self.model.get_all(order)

    def buscar_profesor_salones(self, data_profesor_salon):
        return self.model.get_by_column(data_profesor_salon)

   