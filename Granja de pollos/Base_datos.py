### Clase Base_datos
class Base_datos:

  ### Método constructor
  def __init__(self):
    self.lista_datos = [["P001", "pequeña", "15dias"]]

  ### Leer todos los registros
  def imprimir_info(self):
    for info_pollo in self.lista_datos:
      print(info_pollo)

  ### Crear pollo (agregar nuevo registro)
  def crear_pollo(self, pollo):
    nuevo = [pollo.codigo_pollo, "desconocido", f"{pollo.edad_pollo}dias"]
    self.lista_datos.append(nuevo)

  ### Leer un pollo por código
  def leer_pollo(self, codigo):
    for pollo in self.lista_datos:
      if pollo[0] == codigo:
        return pollo
    return None

  ### Actualizar edad del pollo
  def actualizar_pollo(self, codigo, nueva_edad):
    for pollo in self.lista_datos:
      if pollo[0] == codigo:
        pollo[2] = nueva_edad
        return True
    return False

  ### Eliminar pollo
  def eliminar_pollo(self, codigo):
    for i, pollo in enumerate(self.lista_datos):
      if pollo[0] == codigo:
        del self.lista_datos[i]
        return True
    return False
