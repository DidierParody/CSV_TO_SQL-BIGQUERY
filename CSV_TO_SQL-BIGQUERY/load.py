from google.cloud import bigquery
import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()

json_credentials = os.getenv("CREDENTIALS_PATH")

client = bigquery.Client.from_service_account_json(json_credentials)

climatic_data_csv = "climatic_data_final.csv"

table_id = os.getenv("TABLE_ID")

# Cargar el CSV en un DataFrame de Pandas
df = pd.read_csv(climatic_data_csv)

# Especificar la tabla de destino en BigQuery
tabla_destino = f"{table_id}"

# Configurar el job para subir los datos
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,  # Detecta automáticamente los tipos de datos
    skip_leading_rows=1,  # Ignora la primera fila si es un encabezado
)

# Cargar el DataFrame en BigQuery
job = client.load_table_from_dataframe(df, tabla_destino, job_config=job_config)

# Esperar a que termine la carga
job.result()

print(f"📊 Archivo CSV subido a BigQuery en {tabla_destino}")
