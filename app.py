import os
import math
import numpy as np

# --- Físicas básicas ---
DENSIDAD_TIPICA = 3000.0 # kg/m^3 (valor por defecto)
MTNT_TO_J = 4.184e15
d_m = input("escribe d")
densidad = input("escribe densidad")


def masa_desde_diametro(d_m: float, densidad: float = DENSIDAD_TIPICA) -> float:
# d_m = diámetro en metros
volumen = (math.pi/6.0) * d_m**3
return volumen * densidad


def energia_cinetica(masa: float, velocidad: float) -> float:
# velocidad en m/s, devuelve energía en Joules
return 0.5 * masa * velocidad**2


def energia_en_megatones(energia_j: float) -> float:
return energia_j / MTNT_TO_J


# Crater scaling (modelo simplificado basado en relaciones empíricas)
# Parámetros empíricos simplificados; usar como estimación conservadora.


def crater_diameter_from_energy(energia_j: float, dens_target=2500.0):
# Relación simplificada: D_crater ~ k * E^(1/3.4)
# k ajustable; aquí k en metros/(J^(1/3.4)) para obtener diámetro en metros
k = 1e-2
exponent = 1.0/3.4
D = k * (energia_j ** exponent)
return D


# Overpressure / airblast estimaciones simplificadas
def airblast_radius(energia_megatons: float, threshold_psi: float = 1.0):
# Devuelve radio estimado en km para un umbral de sobrepresión (psi)
# Fórmula aproximada y muy simplificada (solo para visual demo)
# Radio scales roughly with (E)^(1/3)
return (energia_megatons ** (1/3.0)) * 10.0 # km