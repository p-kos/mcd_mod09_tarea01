import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.header("Reducción de Dimensiones con PCA")
if 'df' not in st.session_state:
    st.warning("Datos no cargados")
else:
    df = st.session_state.df

    # Estandarizar los datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[['x', 'y']])

    # Aplicar PCA para reducir la dimensionalidad a 2 componentes
    st.sidebar.write("Criterios para reducción")
    n_components = st.sidebar.slider("Nro componentes", 0, 2, 2)
    pca_random_state = st.sidebar.slider("Random state", 1, 100, 42)
    pca = PCA(n_components=n_components, random_state=pca_random_state)
    pca_data = pca.fit_transform(scaled_data)    

    col1,col2,col3 = st.columns(3)
    with col1:
        st.write('Varianza explicada', pca.explained_variance_)
    with col2:
        st.write('Ratio - Varianza explicada', pca.explained_variance_ratio_)
    with col3:
        st.write('Componentes Principales: ', pca.components_)    

    # Crear un DataFrame con los componentes principales
    pca_df = pd.DataFrame(pca_data, columns=['x', 'y'])


    # Implementar el clustering con K-means (probando con 3 clusters inicialmente)
    st.sidebar.write("Criterios K-Means")

     # seleccionar el nro de clusters
    n_clusters = st.sidebar.slider("Número de clusters", 2, 10, 3)

    # Definir el seed
    kmean_random_state = st.sidebar.slider("Random State", 0, 100, 42)

    # Nro de iteraciones
    max_iter = st.sidebar.slider("Número de iteraciones", 100, 1000, 300)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=kmean_random_state, max_iter=max_iter)
    clusters = kmeans.fit_predict(pca_data)

    # Agregar los clusters al DataFrame
    pca_df['Cluster'] = clusters

    # Calcular el puntaje de silueta para evaluar el clustering
    silhouette = silhouette_score(pca_data, clusters)
    # dividir en 2 columnas
    col1, col2 = st.columns(2)
    with col1:
        # Visualización del clustering
        fig = plt.figure(figsize=(12, 6))
        sns.scatterplot(x=pca_df['x'], y=pca_df['y'], hue=pca_df['Cluster'], palette='viridis', alpha=0.7)
        plt.title(f'Clustering con PCA (Silhouette Score: {silhouette:.2f})')
        plt.xlabel('x')
        plt.ylabel('y')
        st.pyplot(fig)
    with col2:
        st.markdown("###  Medidas de evaluación")
        st.write("Número de Clusters:", kmeans.n_clusters)
        # st.write("Centrolides", kmeans.cluster_centers_)
        st.write("Inercia:", kmeans.inertia_)
        st.write("Siluette Score:", silhouette)
