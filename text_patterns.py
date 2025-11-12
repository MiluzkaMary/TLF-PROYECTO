
from validators import PATTERNS, findall

def extract_all(text: str):
    """
    Recorre todos los patrones definidos y extrae coincidencias únicas
    preservando el orden de aparición en el texto.
    """
    resultados = {}
    for nombre_patron in PATTERNS:
        hallazgos = findall(nombre_patron, text)
        if hallazgos:
            # Quitar duplicados preservando orden
            resultados[nombre_patron] = list(dict.fromkeys(hallazgos))
    return resultados
