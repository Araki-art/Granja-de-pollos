from Base_datos import Base_datos  

class Pollos:
    # métodos constructores
    def __init__(self, id_pollo, dato_edad):
        self.codigo_pollo = id_pollo
        self.edad_pollo = dato_edad

        # objeto de la base de datos
        self.self_objBase_datos = Base_datos()

    # métodos públicos para modificar atributos
    def getCodigo_pollo(self):
        return self.codigo_pollo

    def setCodigo_pollo(self, codigo_pollo):
        self.codigo_pollo = codigo_pollo

    def getEdad_pollo(self):  
        return self.edad_pollo

    def setEdad_pollo(self, edad_pollo): 
        self.edad_pollo = edad_pollo

    # métodos para conectar base de datos
    def guardar_pollo(self):
        obj_pollo = [self.codigo_pollo, "desconocida", self.edad_pollo]  
        self.self_objBase_datos.crear_pollo(obj_pollo) 



        

