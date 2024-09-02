import pandas as pd
import requests
from matplotlib import pyplot as plt

# Descargar el archivo CSV desde la URL
url = 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv'
response = requests.get(url)

# Guardar el contenido del archivo en un archivo local
with open('grades.csv', 'wb') as file:
    file.write(response.content)

# Cargar los datos desde el archivo CSV asegurando la codificación correcta
df_students = pd.read_csv('grades.csv', delimiter=',', header='infer', encoding='utf-8')

# Elimina cualquier fila con datos faltantes
df_cleaned = df_students.dropna(axis=0, how='any')

# Verificar si la columna 'Grade' está presente y calcular quién aprobó
if 'Grade' in df_cleaned.columns:
    df_cleaned['Pass'] = df_cleaned['Grade'] >= 60
else:
    print("La columna 'Grade' no está en el DataFrame.")

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_cleaned['Name'], df_cleaned['Grade'])
plt.xlabel('Nombre')
plt.ylabel('Calificación')
plt.title('Nombre vs Calificación')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(df_cleaned['Name'], df_cleaned['Grade'], marker='o')
plt.xlabel('Nombre')
plt.ylabel('Calificación')
plt.title('Nombre vs Calificación')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['Name'], df_cleaned['Grade'])
plt.xlabel('Nombre')
plt.ylabel('Calificación')
plt.title('Nombre vs Calificación')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de pastel (Proporción de aprobados y no aprobados)
pass_counts = df_cleaned['Pass'].value_counts()
labels = ['Aprobado', 'No Aprobado']

plt.figure(figsize=(8, 8))
plt.pie(pass_counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Proporción de Aprobados y No Aprobados')
plt.show()

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['Grade'], bins=10, edgecolor='black')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones')
plt.show()

# Gráfico de caja
plt.figure(figsize=(10, 6))
plt.boxplot(df_cleaned['Grade'])
plt.ylabel('Calificación')
plt.title('Distribución de Calificaciones')
plt.show()
