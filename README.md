---  

```md
# 🌍 ETL de Datos Climáticos con Python y BigQuery  

Este proyecto implementa un **flujo ETL (Extracción, Transformación y Carga)** para recopilar, limpiar y almacenar datos climáticos en Google BigQuery. Se obtienen datos de temperatura, humedad y velocidad del viento desde la API de Open-Meteo, se procesan con Pandas y se almacenan en una base de datos en la nube.  

## 🚀 Tecnologías utilizadas  

- **Python**: Lenguaje de programación principal  
- **httpx**: Para hacer solicitudes HTTP de manera asíncrona  
- **pandas**: Para manipulación y transformación de datos  
- **google-cloud-bigquery**: Para interactuar con BigQuery  
- **dotenv**: Para la gestión de variables de entorno  

## 📁 Estructura del Proyecto  

```
ETL/
│── extraction.py      # Obtiene datos climáticos de Open-Meteo
│── transformation.py  # Convierte y limpia los datos en CSV
│── load.py            # Sube los datos transformados a BigQuery
│── main.py            # Ejecuta todo el flujo ETL
│── .env               # Variables de entorno (no subir a GitHub)
│── requirements.txt   # Dependencias del proyecto
│── README.md          # Documentación
```

## 🛠️ Configuración  

### 1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/tuusuario/etl-climatico.git
cd etl-climatico
```

### 2️⃣ Crear un entorno virtual e instalar dependencias  
```bash
python3 -m venv etlenv
source etlenv/bin/activate  # En Windows: etlenv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configurar variables de entorno  
Crea un archivo **.env** y define las siguientes variables:  

```
CREDENTIALS_PATH=/ruta/a/credenciales.json
TABLE_ID=etl-452119.dataset.tabla
```

## 📌 Flujo de Datos  

1️⃣ **Extracción (`extraction.py`)**  
   - Obtiene datos meteorológicos de ciudades como Bogotá, Medellín, etc.  
   - Usa `httpx` para hacer solicitudes asíncronas.  
   - Guarda los datos en formato JSON.  

2️⃣ **Transformación (`transformation.py`)**  
   - Convierte el JSON a CSV usando `pandas`.  
   - Expande los datos en múltiples filas para facilitar su análisis.  

3️⃣ **Carga (`load.py`)**  
   - Sube el CSV final a Google BigQuery.  
   - Utiliza `google-cloud-bigquery` para la conexión.  

## ▶️ Ejecución  

Para ejecutar todo el proceso ETL, usa el siguiente comando:  
```bash
python3 main.py
```

## 📊 Visualización de los datos en BigQuery  

1. Ve a [Google BigQuery Console](https://console.cloud.google.com/bigquery)  
2. Selecciona tu dataset y tabla  
3. Usa una consulta SQL como:  
   ```sql
   SELECT * FROM `etl-452119.dataset.tabla` LIMIT 10;
   ```

## ✨ Mejoras Futuras  

- Agregar almacenamiento en una base de datos local como PostgreSQL.  
- Crear un dashboard en **Google Looker Studio** para visualizar los datos.  
- Optimizar la transformación con Apache Spark para datasets grandes.  

---

📌 **Autor**: Didier José Torres Parodis  
📆 **Última actualización**: Febrero 2025  
📂 **Licencia**: MIT  
```

---

### 🔹 ¿Qué hace esta documentación bien?  

✅ **Explicación gradual**: Comienza sencilla y se vuelve técnica.  
✅ **Estructura clara**: Introducción, tecnologías, configuración, flujo, ejecución.  
✅ **Ejemplos y comandos**: Para que cualquier usuario pueda ejecutarlo fácilmente.  
✅ **Mejoras futuras**: Para mostrar posibles optimizaciones.  
