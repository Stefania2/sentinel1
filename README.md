# 🌐 Sentinel-1 Geometry Search & Cleaning Pipeline

Este proyecto automatiza la **búsqueda, análisis, visualización y limpieza de geometrías Sentinel-1** utilizando la API de la **Alaska Satellite Facility (ASF)**.  
El flujo completo puede ejecutarse **localmente** o **de forma automática mediante GitHub Actions**.

## Descripción general
SentinelExperimento es un conjunto de scripts en Python diseñados para realizar búsquedas, análisis y procesamiento de datos satelitales provenientes de la Alaska Satellite Facility (ASF).  
El proyecto utiliza el módulo `asf-search` para consultar escenas del satélite Sentinel, procesarlas en formato GeoJSON, graficar sus geometrías y limpiar conjuntos de datos exportados en formato CSV.

El objetivo principal es automatizar el flujo de trabajo para la obtención, validación y visualización de datos geoespaciales, facilitando el análisis de coberturas, áreas y perímetros de escenas Sentinel.
---

## 📦 Requisitos

Antes de ejecutar los scripts, instala las dependencias necesarias:

# SentinelExperimento

## Descripción general
SentinelExperimento es un conjunto de scripts en Python diseñados para realizar búsquedas, análisis y procesamiento de datos satelitales provenientes de la Alaska Satellite Facility (ASF).  
El proyecto utiliza el módulo `asf-search` para consultar escenas del satélite Sentinel, procesarlas en formato GeoJSON, graficar sus geometrías y limpiar conjuntos de datos exportados en formato CSV.

El objetivo principal es automatizar el flujo de trabajo para la obtención, validación y visualización de datos geoespaciales, facilitando el análisis de coberturas, áreas y perímetros de escenas Sentinel.

---

## Requisitos del sistema

- Python 3.9 o superior  
- pip actualizado (`python -m ensurepip --upgrade`)
- Conexión a internet para acceder a los servicios de ASF

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/sentinel1.git
cd sentinel1

Referencias

ASF Search API Documentation:
🔗 https://docs.asf.alaska.edu/asf_search/basics/

Shapely Geometry Tools:
🔗 https://shapely.readthedocs.io

Matplotlib:
🔗 https://matplotlib.org/stable/
