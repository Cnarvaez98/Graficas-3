import pandas as pd
import plotly.express as px

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con un boxplot
fig_box = px.box(df, x='materia', y='nota', color='aprobado', points='all',
                 title='Distribución de Notas por Materia',
                 labels={'nota': 'Nota', 'materia': 'Materia', 'aprobado': 'Aprobado'})

# Mostrar la gráfica de boxplot
fig_box.show()

# Graficar la distribución de aprobados con un pie chart
aprobados_count = df['aprobado'].value_counts()
labels_pie = aprobados_count.index

fig_pie = px.pie(aprobados_count, names=labels_pie, 
                 title='Proporción de Estudiantes Aprobados/No Aprobados',
                 labels={'label': 'Estado'})

# Mostrar la gráfica de pie chart
fig_pie.show()
