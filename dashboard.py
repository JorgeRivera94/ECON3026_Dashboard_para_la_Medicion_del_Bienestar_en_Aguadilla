import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Economía y Sostenibilidad en Aguadilla", layout="wide")
st.title("Dashboard de Bienestar y Sostenibilidad en Aguadilla")

# CONFIGURACIÓN DE PLOTLY
config = {
    "displayModeBar": False,
    "responsive": True
}


# CARGA DE DATOS

st.sidebar.header("📂 Configuración de datos")

uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV con los indicadores", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Datos cargados correctamente")
else:
    st.warning("⚠️ No has subido ningún CSV. Se usarán datos de ejemplo.")
    df = pd.DataFrame({
        "anio": ["2000", "2001", "2003", "2004", "2005", "2006"],
        "turismo": [120, 125, 140, 145, 155, 160],
        "energia_renovable": [5, 8, 10, 15, 18, 22]
    })

### PARTICIPACION ELECTORAL CSV ###
part_electoral_df = pd.read_csv("./ETL/Transform/transformed_files/participacion_electoral.csv")
part_electoral_df['participación'] = part_electoral_df['participación'].interpolate()

### EDUCACION SUPERIOR CSV ###
edu_superior_df = pd.read_csv("./ETL/Transform/transformed_files/educacion_superior.csv")
edu_superior_df['educacion_superior'] = edu_superior_df['educacion_superior'].interpolate()

### DESEMPLEO CSV ###
desempleo_df = pd.read_csv("./ETL/Transform/transformed_files/desempleo.csv")
desempleo_df['desempleo'] = desempleo_df['desempleo'].interpolate()

### Pobreza CSV ###
pobreza_df = pd.read_csv("./ETL/Transform/transformed_files/pobreza.csv")
pobreza_df['pobreza'] = pobreza_df['pobreza'].interpolate()

### Ingreso Medio CSV ###
ingreso_medio_df = pd.read_csv("./ETL/Transform/transformed_files/ingreso_medio.csv")
ingreso_medio_df['ingreso_medio'] = ingreso_medio_df['ingreso_medio'].interpolate()

### RIESGO DE CANCER CSV ###
riesgo_cancer_df = pd.read_csv("./ETL/Transform/transformed_files/riesgo_cancer.csv")
riesgo_cancer_df['riesgo'] = riesgo_cancer_df['riesgo'].interpolate()

## CONCENTRACION DIESEL CSV ###
concentracion_diesel_df = pd.read_csv("./ETL/Transform/transformed_files/concentracion_diesel.csv")
concentracion_diesel_df['concentración'] = concentracion_diesel_df['concentración'].interpolate()
###################################

# VISUALIZACIÓN DE DATOS
st.subheader("Indicadores ")

col1, col2, col3 = st.columns(3)


with col1:
    fig1 = px.line(part_electoral_df, x="año", y="participación", title="Participación Electoral (%)")
    fig1.update_layout(xaxis_title="Año", yaxis_title="Participación Electoral (%)")
    fig1.add_annotation(
        text="Tasa de participacón electoral. Fuente: Comisión Estatal de Elecciones de Puerto Rico",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig1, use_container_width=True, config=config)

with col2:
    fig2 = px.line(edu_superior_df, x="fecha", y="educacion_superior", title="Educación Superior (%)")
    fig2.update_layout(xaxis_title="Año", yaxis_title="Educación Superior (%)")
    fig2.add_annotation(
        text="Tasa de la población con un grado de Bachillerato o mayor. Fuente: FRED",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig2, use_container_width=True, config=config)

with col3:
    fig3 = px.line(pobreza_df, x="año", y="pobreza", title="Población en Pobreza")
    fig3.update_layout(xaxis_title="Año", yaxis_title="Población en Pobreza")
    fig3.add_annotation(
        text="Cantidad de la población bajo el nivel de pobreza. Fuente: Data Commons",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig3, use_container_width=True, config=config)



# Segunda fila de gráficos
# st.subheader("Indicadores ") 

col4, col5, col6 = st.columns(3)

with col4:
    fig4 = px.line(desempleo_df, x="fecha", y="desempleo", title="Desempleo (%)")
    fig4.update_layout(xaxis_title="Año", yaxis_title="Desempleo (%)")
    fig4.add_annotation(
        text="Tasa del desempleo. Fuente: Data Commons",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig4, use_container_width=True, config=config)

with col5:
    fig5 = px.line(ingreso_medio_df, x="año", y="ingreso_medio", title="Ingreso Medio por Individuo (USD)")
    fig5.update_layout(xaxis_title="Año", yaxis_title="Ingreso Medio por Individuo (USD)")
    fig5.add_annotation(
        text="Ingreso medio por individuo. Fuente: Data Commons",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig5, use_container_width=True, config=config)


with col6:
    fig6 = px.line(riesgo_cancer_df, x="año", y="riesgo", title="Riesgo a Padecer de Cáncer por Exposición A Sustancias Tóxicas en el Aire")
    fig6.update_layout(xaxis_title="Año", yaxis_title="Riesgo (ppm)")
    fig6.add_annotation(
        text="En personas por millón. Fuente: Data Commons",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig6, use_container_width=True, config=config)

col7, col8, col9 = st.columns(3)
#Mean Concentration of Diesel PM Air Pollutant
with col7:
    fig7 = px.line(concentracion_diesel_df, x="año", y="concentración", title="Concentración de MP de Diesel en Aire (µg/m³)")
    fig7.update_layout(xaxis_title="Año", yaxis_title="MP de Diesel en Aire (µg/m³)")
    fig7.add_annotation(
        text="Concentración promedio de MP de diesel en el aire. Fuente: Data Commons",
        xref="paper", yref="paper",
        x=0.5, y=-0.25,
        showarrow=False
    )
    st.plotly_chart(fig7, use_container_width=True, config=config)

### LINKS A FUENTES DE DATOS ###
st.markdown("""
**Fuentes de Datos:**
- Participación Electoral: [Comisión Estatal de Elecciones de Puerto Rico](https://ww2.ceepur.org/Home/Estadisticas)
- Educación Superior: [FRED - Federal Reserve Economic Data](https://fred.stlouisfed.org/series/HC01ESTVC1772005)
- Pobreza: [Data Commons](https://datacommons.org/place/geoId/72005?hl=es)
- Desempleo: [Data Commons](https://datacommons.org/place/geoId/72005?hl=es)
- Ingreso Medio Por Individio: [Data Commons](https://datacommons.org/place/geoId/72005?hl=es)
- Riesgo de Cáncer: [Data Commons](https://datacommons.org/place/geoId/72005?category=Environment&hl=es)
- Concentración de MP de Diesel en Aire: [Data Commons](https://datacommons.org/place/geoId/72005?category=Environment&hl=es)
""")


# SECCIÓN DE CHAT IA

st.divider()
st.header("💬 Asistente de Inteligencia Artificial sobre los Datos")

st.markdown("""
Este asistente usa la API de **OpenAI (GPT-4o-mini)** para analizar los datos.  
Puedes preguntarle cosas como:
- “¿Qué representa la primera tabla?”
- “¿Cuál es la tendencia de la pobreza?”
- “¿Qué relación hay entre educación y pobreza?”
""")

# API Key
api_key = st.text_input("🔑 Introduce tu API key de OpenAI:", type="password")

# Entrada del usuario
user_input = st.text_area("✏️ Escribe tu pregunta aquí:")

# Botón de consulta
if st.button("Preguntar a la IA"):
    if not api_key:
        st.warning("⚠️ Por favor, introduce tu API key de OpenAI antes de consultar.")
    elif user_input:
        try:
            client = OpenAI(api_key=api_key)

            # Preparamos una muestra representativa del DataFrame
            muestra = df.head(10).to_markdown(index=False)
            columnas = ", ".join(df.columns)

            system_prompt = f"""
Eres un experto en análisis de datos socioeconómicos del municipio de Aguadilla, Puerto Rico.
A continuación tienes una tabla de indicadores con las siguientes columnas:
{columnas}

Aquí tienes una muestra de los datos en formato tabla Markdown:
{muestra}

Tu tarea es responder preguntas del usuario de forma analítica, explicando qué representan los datos,
qué mide cada indicador y las tendencias observadas.
Si el usuario pregunta "qué representa la primera tabla", describe de manera detallada el contenido
de la tabla y el significado de cada columna.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )

            st.success(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error al conectar con OpenAI: {e}")
    else:
        st.info("Escribe una pregunta antes de presionar el botón.")


# FIN
st.divider()
