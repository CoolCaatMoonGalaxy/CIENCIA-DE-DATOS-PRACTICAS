import numpy as np
import csv 
import os
import time 

# Datos
data = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]

# Convertir a un array de numpy
grades = np.array(data)

# Imprimir el array original y el array multiplicado por 2
print('Original data:', data)
print('Data x 2:', np.array(data) * 2)
print('---')

print('Grades array:', grades)
print('Grades x 2:', grades * 2)

# Mostrar la forma del array
print('Shape of grades:', grades.shape)

# Mostrar el primer elemento del array
print('First element in grades:', grades[0])

# Calcular y mostrar la media del array
print('Mean of grades:', grades.mean())

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
print(student_data)

# Obtener la ruta de la carpeta Documentos del usuario
ruta_documentos = os.path.join(os.path.expanduser('~'), 'Documentos', 'archivos csv de numpy')

# Verificar si la carpeta existe, y si no, crearla
if not os.path.exists(ruta_documentos):
    os.makedirs(ruta_documentos)
    print(f"Directorio '{ruta_documentos}' creado.")

# Definir la ruta completa para guardar el archivo CSV
ruta_de_archivo_csv = os.path.join(ruta_documentos, 'student_data.csv')

# Verificar si el archivo ya existe
if os.path.exists(ruta_de_archivo_csv):
    print(f"El archivo '{ruta_de_archivo_csv}' ya existe.")
else:
    # Crear el archivo CSV si no existe
    with open(ruta_de_archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir los encabezados
        writer.writerow(["Study Hours", "Grades"])
        # Escribir los datos
        writer.writerows(student_data.T)  # Transponer para escribir por filas
    print(f"Archivo '{ruta_de_archivo_csv}' creado con éxito.")
