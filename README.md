# Proyecto TLF – Patrones y Validación con Expresiones Regulares

Aplicación desarrollada en **Streamlit** como parte del proyecto de **Teoría de Lenguajes Formales**.  
Permite **extraer** y **validar** múltiples patrones utilizando expresiones regulares, simulando el comportamiento de un analizador léxico sencillo.

---

## 🚀 Características principales

### 🔍 Extracción de patrones desde texto
- Permite pegar texto manualmente o cargar archivos `.txt` / `.docx`.
- Detecta todos los patrones definidos sin duplicados y manteniendo el orden en que aparecen.
- Incluye normalización automática del texto para evitar fallos comunes (saltos invisibles, Unicode extraño, etc.).

### ✔ Validación individual
- Selecciona un patrón y valida un solo valor.
- Usa `fullmatch()` para verificar pertenencia exacta al lenguaje definido por cada regex.
- Muestra mensajes claros de éxito o error con ejemplos.

---

## 📦 Patrones soportados

- Correo electrónico  
- Teléfono colombiano (10 dígitos, con o sin +57)  
- Fecha **dd/mm/yyyy**  
- Cédula colombiana (10 dígitos)  
- Código postal colombiano (6 dígitos)  
- URL (http/https)  
- Placa colombiana (autos/motos)  
- Dirección tipo Calle/Carrera/Avenida  
- Monto de dinero (**COP** o terminado en *pesos*)  
- Hora (24h y 12h AM/PM)  
- NIT/RUT colombiano  
- Hashtag  
- Contraseña segura (mayúscula, minúscula, número y símbolo)

---

## 📁 Estructura del proyecto
- app.py # Interfaz Streamlit
- validators.py # Patrones, regex y validación completa
- text_patterns.py # Extracción global y normalización del texto
- requirements.txt # Dependencias necesarias


---

## 🔧 Requisitos
- Python **3.9+**
- pip


