from Base_datos import Base_datos

class Pollos:
  # métodos constructores
  def __init__(self, id_pollo, dato_raza, dato_edad, produccion):
    self.codigo_pollo = id_pollo
    self.raza_pollo = dato_raza
    self.edad_pollo = dato_edad
    self.produccion_semanal = produccion
    self.objBase_datos = Base_datos()

  # métodos públicos para modificar atributos
  def getCodigo_pollo(self):
    return self.codigo_pollo

  def setCodigo_pollo(self, codigo_pollo):
    self.codigo_pollo = codigo_pollo

  def getRaza_pollo(self):
    return self.raza_pollo

  def setRaza_pollo(self, raza_pollo):
    self.raza_pollo = raza_pollo

  def getEdad_pollo(self):
    return self.edad_pollo

  def setEdad_pollo(self, edad_pollo):
    self.edad_pollo = edad_pollo

  def getProduccion_semanal(self):
    return self.produccion_semanal

  def setProduccion_semanal(self, produccion):
    self.produccion_semanal = produccion

  # métodos para conectar base de datos
  def guardar_pollo(self):
    self.objBase_datos.crear_pollo(self)

        

