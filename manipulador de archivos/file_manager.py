from tkinter import filedialog

class FileManager:
    """
    Clase FileManager para manejar operaciones de archivos.
    Permite abrir, guardar, editar y eliminar archivos utilizando cuadros de diálogo.
    """
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.file = None

    def open_file(self, mode='r'):
        """Abre un archivo utilizando un cuadro de diálogo.
        
        Parámetros:
        mode (str): Modo en el que se abrirá el archivo ('r' para lectura, 'w' para escritura).
        
        Retorna:
        file: El archivo abierto o None si no se seleccionó ningún archivo.
        """
        self.filepath = filedialog.askopenfilename(title="Seleccionar archivo")
        if not self.filepath:
            return None

        try:
            self.file = open(self.filepath, mode)  # Cambiar a 'w' si se necesita escribir
            return self.file
        except FileNotFoundError:
            print(f"Error: El archivo '{self.filepath}' no fue encontrado.")
            return None
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            return None

    def save_file(self, content):
        """Guarda el contenido en un archivo utilizando un cuadro de diálogo.
        
        Parámetros:
        content (str): Contenido que se guardará en el archivo.
        
        Retorna:
        bool: True si el archivo se guardó exitosamente, False en caso contrario.
        """
        self.filepath = filedialog.asksaveasfilename(title="Guardar archivo")
        if not self.filepath:
            return False

        try:
            with open(self.filepath, 'w') as file:
                file.write(content)  # Asegurarse de que se escriba el contenido
            print(f"Archivo '{self.filepath}' guardado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return False

    def edit_file(self, new_content):
        """Edita el archivo guardando nuevo contenido.
        
        Parámetros:
        new_content (str): Nuevo contenido que se guardará en el archivo.
        
        Retorna:
        bool: Resultado de la operación de guardado.
        """
        return self.save_file(new_content)

    def delete_file(self):
        """Elimina el archivo seleccionado.
        
        Retorna:
        bool: True si el archivo se eliminó exitosamente, False en caso contrario.
        """
        import os
        try:
            os.remove(self.filepath)
            print(f"Archivo '{self.filepath}' eliminado exitosamente.")
            return True
        except FileNotFoundError:
            print(f"Error: El archivo '{self.filepath}' no fue encontrado.")
            return False
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")
            return False
