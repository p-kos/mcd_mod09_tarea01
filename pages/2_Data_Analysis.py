import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Análisis de los datos")
if 'df' not in st.session_state:
    st.warning("El dataset no fue cargado, cargue antes de continuar")
else:
    df = st.session_state.df
    st.write("El dataset tiene {} filas y {} columnas".format(df.shape[0], df.shape[1]))
    st.write("x: Valores numéricos flotantes.")
    st.write("y: Valores numéricos flotantes.")
    st.write("color: Valores enteros que parecen representar categorías (posiblemente etiquetas de algún tipo).")

    # revisamos si hay valores nulos
    total_na = df.isna().sum()
    st.write("Total nulos", total_na)

    st.write("Tipos de colores", df['color'].unique())
    
    # Análisis exploratorio
    # Visualización de la distribución de las variables 'x' y 'y' y su relación con 'color'

    plt.figure(figsize=(12, 6))

    # Relación entre 'x' y 'y' coloreada por la columna 'color'
    sns.scatterplot(x=df['x'], y=df['y'], hue=df['color'], palette='viridis', alpha=0.7)
    plt.title('Distribución de x vs y coloreada por color')
    plt.xlabel('x')
    plt.ylabel('y')
    st.pyplot(plt)