import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Encabezado de la aplicación
st.header('Cuadro de Mando de Anuncios de Vehículos')
st.write('Bienvenido al panel interactivo de análisis exploratorio del mercado de coches usados.')

# 2. Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# 3. Sección de Casillas de Verificación (Interactividad)
st.subheader('Visualizaciones Disponibles')

# Casilla para el histograma
build_histogram = st.checkbox('Mostrar Histograma del Odómetro')

if build_histogram:
    st.write('Generando histograma para la columna de kilometraje (odómetro)...')
    # Crear e indicar el histograma con Plotly Express
    fig = px.histogram(car_data, x='odometer', title='Distribución del Kilometraje de los Vehículos')
    # Mostrar el gráfico interactivo ajustado al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Casilla del gráfico de dispersión
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs. Odómetro)')

if build_scatter:
    st.write('Generando gráfico de dispersión para analizar precio en función del kilometraje...')
    # Crear e indicar el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Relación entre Kilometraje y Precio')
    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)