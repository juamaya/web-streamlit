import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

 

st.title("Graficas Page")

st.image('images/A320.jpg', width=400)


st.divider()

st.title("Graficos Interactivos")
st.info("Carga un archivo CSV para crear Graficos Interactivos") 
archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")  
if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columna para el eje X") 
        eje_x = st.selectbox ("Eje X", df.columns)
        st.write("Elige una columna para el eje Y") 
        eje_y = st.selectbox ("Eje Y", df.columns)

        if st.button("Crear Grafico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)

st.divider()


 
 


 


st.markdown("Juamaya 🍺 2025")

st.sidebar.success("Select a page 👆")