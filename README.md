
# Proyecto TLF – Patrones y Validación con Regex

## Requisitos
- Python 3.9+
- pip

## Instalación rápida
```bash
python -m venv venv
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Ejecución
```bash
streamlit run app.py
```
Se abrirá el navegador con la interfaz.

## Funcionalidades
- **Extracción**: Pega texto o sube un .txt y detecta patrones (sin duplicados, preservando orden).
- **Validación**: Selecciona un patrón y valida un único valor con retroalimentación.
- **Patrones incluidos**:
  - Correo electrónico
  - Teléfono colombiano
  - Fecha **dd/mm/yyyy**
  - Cédula/ID (6–10 dígitos)
  - Código postal (4–10 dígitos)
  - URL (http/https)
  - Otros

