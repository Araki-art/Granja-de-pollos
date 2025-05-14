class Base_datos:
  def __init__(self):
    self.lista_datos = [["P001", "pequeña", "15dias"]]

  def imprimir_info(self):
    for info_pollo in self.lista_datos:
      print(info_pollo)

  def crear_pollo(self, pollo):
    nuevo = [pollo.codigo_pollo, "desconocido", f"{pollo.edad_pollo}dias"]
    self.lista_datos.append(nuevo)

  def leer_pollo(self, codigo):
    for pollo in self.lista_datos:
      if pollo[0] == codigo:
        return pollo
    return None

  def actualizar_pollo(self, codigo, nueva_edad):
    for pollo in self.lista_datos:
      if pollo[0] == codigo:
        pollo[2] = nueva_edad
        return True
    return False

  def eliminar_pollo(self, codigo):
    for i, pollo in enumerate(self.lista_datos):
      if pollo[0] == codigo:
        del self.lista_datos[i]
        return True
    return False
