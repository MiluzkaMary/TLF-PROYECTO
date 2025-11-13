import streamlit as st
from validators import validate, PATTERNS
from text_patterns import extract_all

# Configuración inicial de la app (título y modo de pantalla)
st.set_page_config(page_title="Proyecto TLF - Patrones y Validación", layout="wide")
st.title("Proyecto TLF – Patrones y Validación con Regex")

# Creación de dos pestañas principales:
# - Extracción en texto (búsqueda de patrones dentro de un documento)
# - Validación individual (validación exacta contra un patrón)
tab1, tab2 = st.tabs(["🔍 Extracción en texto", "✔ Validación individual"])

with tab1:
    st.subheader("Extraer patrones desde un texto")

    # Importación local de Document para evitar carga innecesaria fuera de esta pestaña
    from docx import Document

    # Función para leer archivos .docx y unir su contenido en un solo texto
    def leer_docx(archivo_subido):
        """Extrae texto de un archivo .docx subido a Streamlit."""
        doc = Document(archivo_subido)
        # Se unen los párrafos para evitar saltos inesperados
        return "\n".join([p.text for p in doc.paragraphs])

    # Componente para cargar archivos .txt o .docx
    archivo = st.file_uploader("Cargar archivo (.txt o .docx)", type=["txt", "docx"])

    texto_cargado = ""
    if archivo:
        # Si el archivo es txt → se lee como texto plano
        if archivo.name.endswith(".txt"):
            texto_cargado = archivo.read().decode("utf-8", errors="ignore")
        # Si el archivo es docx → se procesa con la función leer_docx
        elif archivo.name.endswith(".docx"):
            texto_cargado = leer_docx(archivo)

    # Área donde el usuario puede ver o modificar el texto cargado
    texto = st.text_area(
        "Pega aquí el texto a analizar:",
        height=220,
        value=texto_cargado,
        placeholder="Ej: Juan Pérez vive en Calle 45 # 12-34. Su correo es juan@example.com ..."
    )

    # Botón para iniciar la búsqueda de patrones dentro del texto
    if st.button("Buscar patrones", key="buscar"):
        # extract_all normaliza texto y aplica las regex de búsqueda
        resultados = extract_all(texto or "")
        if resultados:
            # Recorre cada patrón encontrado y lo muestra con su nombre y lista
            for k, lista in resultados.items():
                st.markdown(f"**{PATTERNS[k].name}** ({k})")
                st.write(lista)
                st.divider()
        else:
            # Mensaje cuando no se encuentran coincidencias
            st.info("No se encontraron patrones en el texto.")

with tab2:
    st.subheader("Validación campo por campo")

    # Dos columnas: una para elegir el patrón y otra para escribir el valor a validar
    col1, col2 = st.columns(2)
    with col1:
        # Selectbox con la lista de patrones disponibles
        seleccion = st.selectbox(
            "Patrón",
            list(PATTERNS.keys()),
            index=0,
            help="Selecciona el patrón que quieres validar"
        )
    with col2:
        # Campo donde el usuario ingresa el valor a validar
        valor = st.text_input(
            "Valor a validar",
            placeholder="Escribe aquí el valor a validar"
        )

    # Botón para ejecutar la validación individual
    if st.button("Validar", key="validar"):
        ok, msg = validate(seleccion, valor)
        # Muestra éxito o error según corresponda
        st.success(msg) if ok else st.error(msg)

# Pequeña nota informativa al final de la app
st.caption("Incluye: correos, teléfonos CO, fechas dd/mm/yyyy, cédula/ID, códigos postales, URLs, placas CO, direcciones CO, montos de dinero, horas, NIT/RUT y hashtags.")
