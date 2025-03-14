from file_manager import FileManager
from tkinter import Tk

# Inicializar Tkinter
root = Tk()
root.withdraw()  # Ocultar la ventana principal

# Crear una instancia de FileManager
file_manager = FileManager()  # No se pasa el nombre del archivo aquí

# Abrir el archivo (crea uno nuevo si no existe) en modo de escritura
file = file_manager.open_file(mode='w')

if file:
    file.write("Hola, mundo!\n")
    file.close()

# Editar el archivo
file_manager.edit_file("¡Hola, mundo editado!")

# Abrir y leer el contenido
file = file_manager.open_file(mode='r')
if file:
    content = file.read()
    print("Contenido del archivo:")
    print(content)
    file.close()

# Pausa para que el usuario vea el resultado antes de cerrar
input("Presione Enter para continuar...")
# Preguntar al usuario si desea eliminar el archivo
eliminar = input("¿Desea eliminar el archivo? (sí/no): ")

if eliminar.lower() == 'sí':
    file_manager.delete_file()
    print("El archivo ha sido eliminado.")
else:
    print("El archivo no ha sido eliminado.")
