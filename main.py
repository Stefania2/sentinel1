import asf_search as asf
import pandas as pd

results = asf.granule_search(['ALPSRS279162400', 'ALPSRS279162200'])
print(results)

wkt = 'POLYGON((-135.7 58.2,-136.6 58.1,-135.8 56.9,-134.6 56.1,-134.9 58.0,-135.7 58.2))'
results = asf.geo_search(platform=[asf.PLATFORM.SENTINEL1], intersectsWith=wkt, maxResults=10)
print(results)

## This script requires that the asf-search python module is installed
## to install, run the following in a terminal
## `pip install asf-search`
## Then from the correct folder in your terminal run:
## `python asf-search-script-2025-10-06_04-48-28.py`
## 
## For more information, see the official documentation
## https://docs.asf.alaska.edu/asf_search/basics/
import asf_search as asf
import pprint

opts=asf.ASFSearchOptions(**{
    "maxResults": 250,
    "intersectsWith": "POLYGON ((-102.9496000000000038 72.7377999999999929, -99.9816000000000003 71.2757000000000005, -97.9188999999999936 71.2553999999999945, -96.0087000000000046 71.8268999999999949, -96.6071000000000026 73.9877999999999929, -98.1152000000000015 74.3999000000000024, -101.9741000000000071 73.8064999999999998, -102.9496000000000038 72.7377999999999929))",
    "dataset": [
        "SENTINEL-1"
    ]
})

## if the search requires authentication, uncomment
## the lines below, and enter your EDL credentials when prompted
## (use `session.auth_with_token(getpass('EDL Token'))` instead if a CMR bearer token is required)
# from get_pass import get_pass
# session=asf.ASFSession()
# session.auth_with_creds(input('EDL Username'), getpass('EDL Password'))
# opts.session = session

results=asf.search(opts=opts)
pprint.pp(results.geojson())







import asf_search as asf
from shapely.geometry import shape
import matplotlib.pyplot as plt

# --- 1. Buscar escenas ASF (puedes ajustar los parámetros)
opts = asf.ASFSearchOptions(
    dataset="SENTINEL-1",
    maxResults=5  # Puedes aumentar este número
)
results = asf.search(opts=opts)

# --- 2. Procesar cada escena
for i, result in enumerate(results):
    geojson = result.geojson()
    geom = geojson["geometry"]  # GeoJSON geometry
    poly = shape(geom)  # Convertir a Shapely Polygon

    print(f"\n🔹 Escena #{i+1}: {result.properties['sceneName']}")
    print("  - Área (grados²):", round(poly.area, 6))
    print("  - Perímetro:", round(poly.length, 6))
    print("  - Válido:", poly.is_valid)
    print("  - Simple:", poly.is_simple)

    # --- 3. Graficar el polígono
    x, y = poly.exterior.xy
    plt.figure(figsize=(5, 5))
    plt.fill(x, y, alpha=0.4, color='skyblue', edgecolor='black')
    plt.plot(x, y, color='blue')
    plt.title(f"Escena #{i+1}: {result.properties['sceneName']}")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    from shapely.geometry import shape

    # Buscar escenas en ASF
opts = asf.ASFSearchOptions(
    dataset="SENTINEL-1",
    maxResults=10  # Puedes cambiar la cantidad
)

results = asf.search(opts=opts)

# Lista para guardar los resultados
datos = []

# Recorrer cada escena encontrada
for r in results:
    geojson = r.geojson()
    geom = geojson["geometry"]
    poly = shape(geom)  # Convierte a Shapely Polygon

    props = r.properties

    datos.append({
        "sceneName": props.get("sceneName"),
        "platform": props.get("platform"),
        "startTime": props.get("startTime"),
        "area_deg2": round(poly.area, 6),  # Aproximada en grados cuadrados
        "perimeter": round(poly.length, 6),
        "centroid_lon": round(poly.centroid.x, 6),
        "centroid_lat": round(poly.centroid.y, 6),
        "is_valid": poly.is_valid,
        "is_simple": poly.is_simple,
        "geometry_wkt": poly.wkt  # Guarda el polígono como texto (WKT)
    })

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar en CSV
df.to_csv("sentinel7_geometrias.csv",index=False)

print("✅ Archivo guardado como 'sentinel7_geonmetrias.csv")   

