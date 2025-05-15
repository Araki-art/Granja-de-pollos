from Pollos import Pollos

### Interfaz de usuario
def menu():
  print("\n--- SISTEMA DE CONTROL DE POLLOS ---")
  print("1. Agregar pollo")
  print("2. Mostrar todos los pollos")
  print("3. Consultar pollo por código")
  print("4. Actualizar edad de un pollo")
  print("5. Eliminar un pollo")
  print("6. Salir")

### Función principal
def ejecutar():
  while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
      codigo = input("Ingrese el código del pollo: ")
      raza = input("Ingrese la raza del pollo: ")
      edad = input("Ingrese la edad del pollo (en días): ")
      produccion = input("Producción semanal de huevos: ")

      pollo = Pollos(codigo, raza, edad, produccion)
      pollo.guardar_pollo()
      print(" Pollo registrado con éxito.")

    if opcion == "2":
      temp = Pollos("temp", "temp", "0", 0)
      print("\n Lista de pollos:")
      temp.objBase_datos.imprimir_info()

    if opcion == "3":
      codigo = input("Ingrese el código del pollo a consultar: ")
      temp = Pollos("temp", "temp", "0", 0)
      resultado = temp.objBase_datos.leer_pollo(codigo)
      if resultado:
        print("Registro encontrado:", resultado)
      else:
        print(" No se encontró el pollo.")

    if opcion == "4":
      codigo = input("Código del pollo a actualizar: ")
      nueva_edad = input("Nueva edad (en días): ")
      temp = Pollos("temp", "temp", "0", 0)
      actualizado = temp.objBase_datos.actualizar_pollo(codigo, f"{nueva_edad}dias")
      if actualizado:
        print(" Edad actualizada correctamente.")
      else:
        print("No se encontró el pollo.")

    if opcion == "5":
      codigo = input("Código del pollo a eliminar: ")
      temp = Pollos("temp", "temp", "0", 0)
      eliminado = temp.objBase_datos.eliminar_pollo(codigo)
      if eliminado:
        print("🗑Pollo eliminado correctamente.")
      else:
        print(" No se encontró el pollo.")

    if opcion == "6":
      print("Saliendo del sistema...")
      break

### Ejecutar interfaz
ejecutar()
