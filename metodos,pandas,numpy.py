import numpy as np
import pandas as pd

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

print("Primeros valores de datos de estudiantes Usando Index [0][0]:", student_data[0][0])

# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Promedio Horas estudiadas: {:.2f}\nCalificacion Promedio: {:.2f}'.format(avg_study, avg_grade))

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

print("La longitud del dataframe de students es:",len(df_students))
print("Vamos a iterar dentro del DF")
fila = df_students.loc[1]
print(fila)

for index, student in df_students.iterrows():
    if student['Grade'] <= 50:
        print(f'{student["Name"]},{student["StudyHours"]}:horas,{student["Grade"]} reprobó')
    else:
        print(f'{student["Name"]},{student["StudyHours"]}:horas, {student["Grade"]} aprobado')

print(df_students.iloc[2,[0,1,2]])


while True:
    valor_seleccionado = input("Seleccione el alumno que está buscando (o escriba 'salir' para terminar): ")
    
    if valor_seleccionado.lower() == 'salir':
        print("Saliendo del programa.")
        break
    
    if valor_seleccionado.title() in df_students['Name'].values:
        for index, student in df_students.iterrows():
            if student['Name'] == valor_seleccionado.title():
                print(f'Nombre: {student["Name"]}, Horas Estudiadas: {student["StudyHours"]}, Calificación: {student["Grade"]}')
    else:
        print("Alumno no encontrado")
