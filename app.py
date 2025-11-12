import streamlit as st
from validators import validate, PATTERNS
from text_patterns import extract_all



st.set_page_config(page_title="Proyecto TLF - Patrones y Validación", layout="wide")
st.title("Proyecto TLF – Patrones y Validación con Regex")

tab1, tab2 = st.tabs(["🔍 Extracción en texto", "✔ Validación individual"])

with tab1:
    st.subheader("Extraer patrones desde un texto")

    # --- Leer archivos DOCX ---
    from docx import Document

    def leer_docx(archivo_subido):
        """Extrae texto de un archivo .docx subido a Streamlit."""
        doc = Document(archivo_subido)
        return "\n".join([p.text for p in doc.paragraphs])

    # --- Cargar archivo .txt o .docx ---
    archivo = st.file_uploader("Cargar archivo (.txt o .docx)", type=["txt", "docx"])

    texto_cargado = ""
    if archivo:
        if archivo.name.endswith(".txt"):
            texto_cargado = archivo.read().decode("utf-8", errors="ignore")
        elif archivo.name.endswith(".docx"):
            texto_cargado = leer_docx(archivo)

    # --- Área de texto (permite pegar o editar el contenido cargado) ---
    texto = st.text_area(
        "Pega aquí el texto a analizar:",
        height=220,
        value=texto_cargado,
        placeholder="Ej: Juan Pérez vive en Calle 45 # 12-34. Su correo es juan@example.com ..."
    )

    # --- Botón de búsqueda ---
    if st.button("Buscar patrones", key="buscar"):
        resultados = extract_all(texto or "")
        if resultados:
            for k, lista in resultados.items():
                st.markdown(f"**{PATTERNS[k].name}** ({k})")
                st.write(lista)
                st.divider()
        else:
            st.info("No se encontraron patrones en el texto.")


with tab2:
    st.subheader("Validación campo por campo")
    col1, col2 = st.columns(2)
    with col1:
        seleccion = st.selectbox("Patrón", list(PATTERNS.keys()), index=0, help="Selecciona el patrón que quieres validar")
    with col2:
        valor = st.text_input("Valor a validar", placeholder="Escribe aquí el valor a validar")
    if st.button("Validar", key="validar"):
        ok, msg = validate(seleccion, valor)
        st.success(msg) if ok else st.error(msg)

st.caption("Incluye: correos, teléfonos CO, fechas dd/mm/yyyy, cédula/ID, códigos postales, URLs, placas CO, direcciones CO, montos de dinero, horas, NIT/RUT y hashtags.")
