import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Economia y Sostenibilidad en Aguadilla", layout="wide")

# Config plotly

config = {
    "displayModeBar": False,
    "responsive": True
}

st.title("Dashboard de Bienestar en Aguadilla")

col1, col2, col3 = st.columns(3)

# Llamadas para la captura de datos
# ...
# Visual 1 de prueba
try:
    # Datos de prueba para probar streamlit
    df = pd.DataFrame({
        "años": ["2000", "2001", "2003", "2004", "2005", "2006"],

        "numero_de_votantes": [78, 84, 65, 90, 200, 80],

        "Porcentaje_de_Educacion_mayor_a_superior": [78, 84, 65, 90, 200, 80],

        "Porcentaje_de_pobreza": [78, 84, 65, 90, 200, 80]

    })  # conversion de JSON a data para el grafo

    with col1:
        fig1 = px.line(df, x="años", y="numero_de_votantes", title="Participacion electoral")
        st.plotly_chart(fig1, use_container_width=True, config=config)

    with col2:
        fig1 = px.line(df, x="años", y="Porcentaje_de_Educacion_mayor_a_superior", title="Educacion")
        st.plotly_chart(fig1, use_container_width=True, config=config)

    with col3:
        fig1 = px.line(df, x="años", y="Porcentaje_de_pobreza", title="Pobreza")
        st.plotly_chart(fig1, use_container_width=True, config=config)


except Exception as e:
    st.error(f"[-] Err: {e}")
