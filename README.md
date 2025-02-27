# 🌎 ETL de Datos Climáticos con BigQuery

## 📌 Descripción
Este proyecto implementa un pipeline **ETL (Extracción, Transformación y Carga)** que recopila datos climáticos de varias ciudades, los procesa y los almacena en **Google BigQuery** para su posterior análisis.

El flujo de trabajo sigue tres fases principales:
1. **Extracción**: Obtiene datos climáticos desde la API de Open-Meteo.
2. **Transformación**: Convierte y estructura los datos en un formato tabular.
3. **Carga**: Sube la información procesada a una tabla en **BigQuery**.

## 🛠️ Tecnologías utilizadas
- **Python 3.12**
- **httpx** (para solicitudes HTTP asíncronas)
- **pandas** (para manipulación de datos)
- **Google BigQuery** (para almacenamiento y análisis de datos)
- **dotenv** (para gestión de variables de entorno)

## 📂 Estructura del proyecto
```
ETL_Project/
│── extraction.py      # Extrae datos de Open-Meteo API
│── transformation.py  # Procesa y estructura los datos
│── load.py            # Sube los datos a BigQuery
│── main.py            # Orquesta todo el flujo ETL
│── .env               # Variables de entorno (no subir a GitHub)
│── requirements.txt   # Dependencias del proyecto
│── README.md          # Documentación
```

## 🚀 Instalación y Configuración
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/ETL_Project.git
   cd ETL_Project
   ```

2. **Crear un entorno virtual:**
   ```bash
   python3 -m venv etlenv
   source etlenv/bin/activate  # En Windows: etlenv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto y agrega:
   ```ini
   CREDENTIALS_PATH=/ruta/a/tu/credencial.json
   TABLE_ID=etl_proyecto.tu_tabla
   ```

## 🏗️ Funcionamiento del ETL
### 1️⃣ Extracción de Datos (`extraction.py`)
Este script obtiene datos climáticos de **Bogotá, Medellín, Barranquilla, Santa Marta y Bucaramanga** desde la API de Open-Meteo.

📌 *Ejemplo de datos extraídos:*
```json
{
  "bogota": {
    "hourly": {
      "temperature_2m": [15, 14, 13, 12],
      "relative_humidity_2m": [80, 82, 85, 90],
      "wind_speed_10m": [5, 6, 7, 8]
    }
  }
}
```

### 2️⃣ Transformación de Datos (`transformation.py`)
Se convierte el JSON en un CSV estructurado y se normalizan los datos.

📌 *Ejemplo de datos transformados:*
```
ciudad, tiempo, temperatura_2m, humedad_relativa_2m, velocidad_viento_10m, categoria
Bogotá, 2024-09-01T12:00, 15, 80, 5, temperature_2m
Bogotá, 2024-09-01T13:00, 14, 82, 6, temperature_2m
```

### 3️⃣ Carga de Datos a BigQuery (`load.py`)
Se envía el CSV final a **BigQuery**, detectando automáticamente los tipos de datos.

📌 *Código relevante:*
```python
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    skip_leading_rows=1
)
job = client.load_table_from_dataframe(df, tabla_destino, job_config=job_config)
job.result()
```

## ▶️ Ejecución del Pipeline
Para correr todo el flujo ETL, ejecuta:
```bash
python3 main.py
```
Esto ejecutará `extraction.py`, `transformation.py` y `load.py` en orden.

## 📊 Consulta de Datos en BigQuery
Para verificar que los datos llegaron correctamente a BigQuery, puedes ejecutar la siguiente consulta SQL:
```sql
SELECT * FROM `etl_proyecto.tu_tabla`
LIMIT 10;
```

## ✨ Contribuciones
Si deseas contribuir, haz un **fork** del proyecto, crea una rama, realiza tus cambios y envía un **pull request**.

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**.

---
📌 *Desarrollado por Didier José Torres Parodis*


