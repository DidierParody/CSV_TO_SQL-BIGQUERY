import asyncio
import extraction
import transformation
import load

async def main():
    print("🚀 Iniciando proceso ETL...")

    # Ejecutar extracción de datos
    print("📡 Extrayendo datos...")
    await extraction.main()

    # Ejecutar transformación de datos
    print("🔄 Transformando datos...")
    transformation

    # Ejecutar carga de datos
    print("📤 Cargando datos a BigQuery...")
    load

    print("✅ Proceso ETL completado con éxito.")

if __name__ == "__main__":
    asyncio.run(main())
