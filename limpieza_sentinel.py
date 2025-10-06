import pandas as pd
import numpy as np
import glob
import os
from shapely import wkt

# === CONFIGURACIÓN ===
# Carpeta donde están los archivos CSV
carpeta = r"C:\DataEngineering"
# Patrón de archivos
patron = os.path.join(carpeta, "sentinel3_geometrias*.csv")
# Archivos de salida
archivo_salida = os.path.join(carpeta, "sentinel3_geometrias_unificadas_limpias.csv")
reporte_salida = os.path.join(carpeta, "sentinel3_reporte_limpieza.csv")

# === FUNCIÓN DE LIMPIEZA ===
def limpiar_df(df):
    original = len(df)
    columnas = len(df.columns)
    
    # Contar duplicados
    duplicados = df.duplicated().sum()
    df = df.drop_duplicates().copy()
    
    # Guardar antes de eliminar coordenadas inválidas
    antes_coords = len(df)
    
    # Eliminar coordenadas fuera de rango
    df.loc[(df['centroid_lat'] < -90) | (df['centroid_lat'] > 90), 'centroid_lat'] = np.nan
    df.loc[(df['centroid_lon'] < -180) | (df['centroid_lon'] > 180), 'centroid_lon'] = np.nan
    df = df.dropna(subset=['centroid_lat', 'centroid_lon'])
    coords_invalidas = antes_coords - len(df)
    
    # Guardar antes de eliminar geometrías inválidas
    antes_geo = len(df)

    # Validar y corregir geometrías WKT
    def format_wkt(wkt_str):
        try:
            geom = wkt.loads(wkt_str)
            if not geom.is_valid:
                geom = geom.buffer(0)
            return geom.wkt
        except Exception:
            return None

    df['geometry_wkt'] = df['geometry_wkt'].apply(format_wkt)
    df = df.dropna(subset=['geometry_wkt'])
    geometrias_invalidas = antes_geo - len(df)
    
    final = len(df)
    eliminadas_totales = original - final
    
    return df, {
        "filas_originales": original,
        "columnas": columnas,
        "duplicados_eliminados": duplicados,
        "coords_invalidas_eliminadas": coords_invalidas,
        "geometrias_invalidas_eliminadas": geometrias_invalidas,
        "filas_finales": final,
        "filas_eliminadas_total": eliminadas_totales
    }

# === PROCESAMIENTO ===
archivos = glob.glob(patron)
dfs = []
reporte = []

if not archivos:
    print("⚠️ No se encontraron archivos con el patrón especificado.")
else:
    for archivo in archivos:
        print(f"Procesando: {archivo}")
        df = pd.read_csv(archivo)
        df_limpio, stats = limpiar_df(df)
        stats["archivo"] = os.path.basename(archivo)
        dfs.append(df_limpio)
        reporte.append(stats)

    # Unir todos los archivos limpios
    df_final = pd.concat(dfs, ignore_index=True)
    df_final.to_csv(archivo_salida, index=False)

    # Crear y guardar el reporte
    df_reporte = pd.DataFrame(reporte)
    df_reporte.to_csv(reporte_salida, index=False)

    print("\n✅ Limpieza completada con éxito.")
    print(f"📁 Archivo combinado guardado en: {archivo_salida}")
    print(f"📊 Reporte detallado guardado en: {reporte_salida}\n")
    print("Resumen de limpieza general:")
    print(df_reporte)
