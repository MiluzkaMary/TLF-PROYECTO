from validators import PATTERNS, findall
import re

def extract_all(text: str):
    """
    Recorre todos los patrones definidos y extrae coincidencias únicas
    preservando el orden de aparición en el texto.
    """

    # --- NORMALIZACIÓN DEL TEXTO PARA EVITAR FALSOS NEGATIVOS ---

    # Reemplaza saltos de línea, tabs y saltos especiales Unicode por espacios
    text = text.replace("\u2028", " ").replace("\u2029", " ").replace("\u00A0", " ")
    text = text.replace("\t", " ")

    # Quitar saltos de línea innecesarios
    text = text.replace("\n", " ").replace("\r", " ")

    # Reemplazar múltiples espacios por un solo espacio
    text = re.sub(r"\s{2,}", " ", text).strip()

    resultados = {}

    # --- EJECUCIÓN DE BÚSQUEDA PATRÓN POR PATRÓN ---
    for nombre_patron in PATTERNS:
        hallazgos = findall(nombre_patron, text)

        if hallazgos:
            # Eliminar duplicados preservando orden
            resultados[nombre_patron] = list(dict.fromkeys(hallazgos))

    return resultados
