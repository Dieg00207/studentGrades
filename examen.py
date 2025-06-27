import os
import sqlite3

# Ruta al directorio
ruta_direct = r'C:\Users\aleja\Desktop\III Semestre 2024\Base da datos relacionales\repaso_9_12_24\examen'
# Comprobación de existencia y creación de directorios
os.makedirs(ruta_direct, exist_ok=True)

# Ruta completa a la base de datos
ruta_dbAlumno = os.path.join(ruta_direct, 'bddregistronotas.db')

# Conecta a la base de datos SQLite
conexion = sqlite3.connect(ruta_dbAlumno)


import sqlite3

# Definir la ruta de la base de datos
ruta_db = r'C:\Users\aleja\Desktop\III Semestre 2024\Base da datos relacionales\repaso_9_12_24\examen\bddregistronotas.db'

# Conectar a la base de datos SQLite (se creará si no existe)
conexion = sqlite3.connect(ruta_db)

# Crear la tabla si no existe
cursor = conexion.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS alumnos (
    ID_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre_alumno TEXT NOT NULL,
    Apellido_alumno TEXT NOT NULL,
    Fecha_nacimiento DATE,
    Carrera TEXT NOT NULL,
    Direccion TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS notas (
    ID_nota INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_alumno INTEGER NOT NULL,
    Clase TEXT NOT NULL,
    Nota1 REAL NOT NULL,
    Nota2 REAL NOT NULL,
    Nota3 REAL NOT NULL,
    FOREIGN KEY (ID_alumno) REFERENCES alumnos(ID_alumno) ON DELETE CASCADE
);
''')

cursor.close()

def mostrar_menu():
    print("\nBienvenido al sistema de gestión de alumnos ")
    print("1. Agregar Alumno")
    print("2. Consultar Alumno")
    print("3. Modificar Alumno")
    print("4. Eliminar Alumno")
    print("5. Agregar Notas")
    print("6. Consultar Notas")
    print("7. Consultar alumno")
    print("8. Salir")

def agregar_alumno():
    Nombre_alumno = input("Ingrese el nombre del alumno: ")
    Apellido_alumno= input("Ingrese el apellido del alumno: ")
    Fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    Carrera = input("Ingrese la carrera que estudia")
    Direccion = input("Ingrese la descripcion: ")

    cursor = conexion.cursor()
    sql_insert = "INSERT INTO alumnos (Nombre_alumno, Apellido_alumno, Fecha_nacimiento, Carrera, Direccion) VALUES (?, ?, ?, ?, ?)"
    valores = (Nombre_alumno, Apellido_alumno, Fecha_nacimiento, Carrera, Direccion)
    cursor.execute(sql_insert, valores)
    conexion.commit()  # Confirmar cambios en la base de datos
    cursor.close()
    print("Alumno agregado con éxito.")

def consultar_alumno():
    cursor = conexion.cursor()
    
    # Obtener la lista de alumnos y sus notas
    cursor.execute('''
    SELECT alumnos.ID_alumno, 
        alumnos.Nombre_alumno, 
        alumnos.Apellido_alumno, 
        alumnos.Fecha_nacimiento, 
        alumnos.Carrera, 
        alumnos.Direccion, 
        notas.Nota1, 
        notas.Nota2, 
        notas.Nota3
    FROM alumnos
    LEFT JOIN notas ON alumnos.ID_alumno = notas.ID_alumno
    ''')
    
    resultados = cursor.fetchall()
    print("\n--- Lista de Alumnos ---")
    
    for fila in resultados:
        # Información del alumno
        print(f"ID_Alumno: {fila[0]}, Nombre del alumno: {fila[1]}, Apellido del alumno: {fila[2]}, "
            f"Fecha de nacimiento: {fila[3]}, Carrera: {fila[4]}, Direccion: {fila[5]}")
        
        # Comprobar si hay notas registradas
        if fila[6] is not None and fila[7] is not None and fila[8] is not None:
            promedio = round((fila[6] + fila[7] + fila[8]) / 3, 2)
            print(f"  Notas: Nota1: {fila[6]}, Nota2: {fila[7]}, Nota3: {fila[8]}, Promedio: {promedio}")
        else:
            print("  No se han asignado notas para este alumno.")
    
    cursor.close()


def modificar_alumno():
    consultar_alumno()  # Mostrar libros disponibles
    ID_alumno = input("\nIngrese el ID del alumno que desea modificar: ")
    Nombre_alumno = input("Ingrese el nuevo nombre del alumno (dejar en blanco si no desea cambiar): ")
    Apellido_alumno = input("Ingrese el nuevo apellido del alumno (dejar en blanco si no desea cambiar): ")
    Fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (dejar en blanco si no desea cambiar): ")
    Carrera = input("Ingrese la nueva carrera (dejar en blanco si no desea cambiar): ")
    Direccion = input("Ingrese la nueva Direccion (dejar en blanco si no desea cambiar): ")


    cursor = conexion.cursor()

    # Intentar seleccionar el libro
    cursor.execute("SELECT * FROM alumnos WHERE ID_alumno = ?", (ID_alumno,))
    alumnos = cursor.fetchone()

    if not alumnos:
        print("No se encontró ningún libro con ese ID.")
        return  # Salir de la función si no hay resultados

    # Si el campo es dejado vacío, usar el valor existente
    Nombre_alumno = Nombre_alumno if Nombre_alumno else alumnos[1]
    Apellido_alumno = Apellido_alumno if Apellido_alumno else alumnos[2]
    Fecha_nacimiento = Fecha_nacimiento if Fecha_nacimiento else alumnos[3]
    Carrera =  Carrera if Carrera else alumnos[4]
    Direccion = Direccion if Direccion else alumnos[5]

    sql_update = """
    UPDATE alumnos
    SET Nombre_alumno = ?, Apellido_alumno = ?, Fecha_nacimiento = ?, Carrera = ?, Direccion = ? 
    WHERE ID_alumno = ?
    """
    valores = (Nombre_alumno, Apellido_alumno, Fecha_nacimiento, Carrera, Direccion, ID_alumno)
    print(f"Valores para actualizar: {valores}") 
    cursor.execute(sql_update, valores)
    conexion.commit()
    cursor.close()
    print("Alumno modificado con éxito.")


def eliminar_alumno():
    consultar_alumno()
    ID_libro = input("\nIngrese el ID del alumno que desea eliminar: ")

    cursor = conexion.cursor()
    sql_delete = "DELETE FROM alumnos WHERE ID_libro = ?"
    valores = (ID_libro,)
    cursor.execute(sql_delete, valores)
    conexion.commit()
    cursor.close()
    print("Alumnos eliminado con éxito.")
def agregar_notas():
    consultar_alumno()
    ID_alumno = input("\nIngrese el ID del alumno al que desea agregar notas: ")
    Clase = input("Ingrese el nombre de la clase: ")
    Nota1 = float(input("Ingrese la primera nota: "))
    Nota2 = float(input("Ingrese la segunda nota: "))
    Nota3 = float(input("Ingrese la tercera nota: "))

    cursor = conexion.cursor()
    sql_insert = "INSERT INTO notas (ID_alumno, Clase, Nota1, Nota2, Nota3) VALUES (?, ?, ?, ?, ?)"
    valores = (ID_alumno, Clase, Nota1, Nota2, Nota3)
    cursor.execute(sql_insert, valores)
    conexion.commit()
    cursor.close()
    print("Notas agregadas con éxito.")

def consultar_alumno():
    cursor = conexion.cursor()
    
    # Mostrar solo el ID y Nombre de los alumnos
    cursor.execute("SELECT ID_alumno, Nombre_alumno FROM alumnos")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("\nNo hay alumnos registrados.")
        cursor.close()
        return
    
    print("\n--- Lista de Alumnos (ID y Nombre) ---")
    for fila in resultados:
        print(f"ID_Alumno: {fila[0]}, Nombre del alumno: {fila[1]}")

    # Solicitar al usuario el ID del alumno para consultar más detalles
    ID_alumno = input("\nIngrese el ID del alumno para ver más detalles: ")

    # Consultar la información completa del alumno y sus notas
    cursor.execute('''
    SELECT alumnos.ID_alumno, 
           alumnos.Nombre_alumno, 
           alumnos.Apellido_alumno, 
           alumnos.Fecha_nacimiento, 
           alumnos.Carrera, 
           alumnos.Direccion, 
           notas.Nota1, 
           notas.Nota2, 
           notas.Nota3
    FROM alumnos
    LEFT JOIN notas ON alumnos.ID_alumno = notas.ID_alumno
    WHERE alumnos.ID_alumno = ?
    ''', (ID_alumno,))
    
    fila = cursor.fetchone()
    
    if fila:
        # Mostrar la información del alumno
        print(f"\n--- Información Completa del Alumno ---")
        print(f"ID_Alumno: {fila[0]}")
        print(f"Nombre del alumno: {fila[1]}")
        print(f"Apellido del alumno: {fila[2]}")
        print(f"Fecha de nacimiento: {fila[3]}")
        print(f"Carrera: {fila[4]}")
        print(f"Dirección: {fila[5]}")
        
        # Mostrar las notas y el promedio si existen
        if fila[6] is not None and fila[7] is not None and fila[8] is not None:
            promedio = round((fila[6] + fila[7] + fila[8]) / 3, 2)
            print(f"Notas: Nota1: {fila[6]}, Nota2: {fila[7]}, Nota3: {fila[8]}, Promedio: {promedio}")
        else:
            print("No se han asignado notas para este alumno.")
    else:
        print("No se encontró un alumno con ese ID.")
    
    cursor.close()

def consultar_notas():
    consultar_alumno()

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            consultar_alumno()
        elif opcion == '3':
            modificar_alumno()
        elif opcion == '4':
            eliminar_alumno()
        elif opcion == '5':
            agregar_notas()
        elif opcion == '6':
            consultar_notas()
        elif opcion == '7':
            consultar_alumno()
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta nuevamente.")

if __name__ == "__main__":
    try:
        main()
    finally:
        conexion.close()  # Asegurar que la conexión se cierra al finalizar