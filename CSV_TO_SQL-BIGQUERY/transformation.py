import pandas as pd
import ast  # Para convertir strings a listas reales

# Cargar el Json
df = pd.read_json("climatic_data.json")
# pasar el json a csv
df.to_csv("climatic_data.csv", index=False)

# Convertir strings en listas reales
for col in df.columns:
    df[col] = df[col].apply(lambda x: ast.literal_eval(x) if isinstance(x,str) else x)

# Toma cada elemento que hay en una lista y hace que ocupe su propia casilla
df_expanded = df.explode(list(df.columns)) # se hace que se aplique a todas la columnas
# usamos copy para no alterar el dataftame original
df_time = df_expanded.iloc[:168,:].copy()#todos los elementos de todas las columnas hasta la fila 170 
df_temperature_2m = df_expanded.iloc[168:336,:].copy()
df_relative_humididy_2m = df_expanded.iloc[336:504,:].copy()
df_wind_speed_10m = df_expanded.iloc[504:,:].copy()

# convertimos las segmentaciona a dataframes
df_time["category"] = "time"
df_temperature_2m["category"] = "temperature_2m"
df_relative_humididy_2m["category"] = "relative_humidity_2m"
df_wind_speed_10m["category"] = "wind_speed_10m"

df_final = pd.concat([df_time, df_temperature_2m, df_relative_humididy_2m, df_wind_speed_10m], ignore_index=True)

df_final.to_csv("climatic_data_final.csv", index=False)

print(f"📊 Archivo CSV se ha creado correctamente")