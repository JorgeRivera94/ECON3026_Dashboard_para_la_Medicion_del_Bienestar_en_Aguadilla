'''
File to transform raw data into cleaded data for plotting in dashboard
'''
import pandas as pd

def transform_cambio_RCP_45(df):
    '''
    Function to transform raw data of cambio RCP 4.5 into cleaned data
    '''
    # Convertir columna "Variable observation date" a formato datetime
    df['Variable observation date'] = pd.to_datetime(df['Variable observation date'], format='%Y-%m')

    # Agregar columna "año" extrayendo el año de "Variable observation date"
    df['año'] = df['Variable observation date'].dt.year
    # Agregar promedio por año
    df_yearly = df.groupby('año')["Variable observation value"].mean().reset_index()
    df_yearly.rename(columns={"Variable observation value": "cambio_RCP_45"}, inplace=True)
    # Remover todas las columnas excepto "año" y "cambio_RCP_45"
    df_yearly = df_yearly[['año', 'cambio_RCP_45']]
    return df_yearly

def transform_cambio_RCP_85(df):
    '''
    Function to transform raw data of cambio RCP 8.5 into cleaned data
    '''
    # Convertir columna "Variable observation date" a formato datetime
    df['Variable observation date'] = pd.to_datetime(df['Variable observation date'], format='%Y-%m')

    # Agregar columna "año" extrayendo el año de "Variable observation date"
    df['año'] = df['Variable observation date'].dt.year
    # Agregar promedio por año
    df_yearly = df.groupby('año')["Variable observation value"].mean().reset_index()
    df_yearly.rename(columns={"Variable observation value": "cambio_RCP_85"}, inplace=True)
    # Remover todas las columnas excepto "año" y "cambio_RCP_85"
    df_yearly = df_yearly[['año', 'cambio_RCP_85']]
    return df_yearly

# Write to CSV
transformed_dir = "./ETL/Transform/transformed_files/"
source_dir = "./ETL/Extract/extracted_files/"

# Transform Cambio RCP 4.5
cambio_RCP_45_df = pd.read_csv(source_dir + "Aguadilla_ Cambio previsto de la temperatura máx. según el RCP 4.5 (en base al año 2006) (2100).csv")
cambio_RCP_45_transformed = transform_cambio_RCP_45(cambio_RCP_45_df)
cambio_RCP_45_transformed.to_csv(transformed_dir + "cambio_RCP_45.csv", index=False)

# Transform Cambio RCP 8.5
cambio_RCP_85_df = pd.read_csv(source_dir + "Aguadilla_ Cambio previsto de la temperatura máx. según el RCP 8.5 (en base al año 2006) (2100).csv")
cambio_RCP_85_transformed = transform_cambio_RCP_85(cambio_RCP_85_df)
cambio_RCP_85_transformed.to_csv(transformed_dir + "cambio_RCP_85.csv", index=False)