import streamlit as st 
import io
from PIL import Image
from functions import load_llm, create_docx
import requests
from fetch_images import fetch_photo

st.set_page_config(layout="wide")

def main():
    st.title("Aplicación Generadora de textos con AI")
    user_input = st.text_input("¡Por favor, introduce la idea/tema para el artículo que deseas generar!")
    image_input = st.text_input("¡Por favor, introduce el tema de la imagen que deseas obtener!")

    if len(user_input) > 0 and len(image_input) > 0:
        col1, col2, col3 = st.columns([1,2,1])

        with col1:
            st.subheader("Contenido Generado con inteligencia artifical")
            st.write("El tema del artículo es: " + user_input)
            st.write("La imagen del artículo es: " + image_input)
            prompt = """Eres un experto en marketing digital y SEO y tu tarea es escribir un artículo
              sobre el tema proporcionado: {user_input}. El artículo no debe superar las 800 palabras.
              El artículo no debe ser muy largo.
            """
            llamada_llm = load_llm(template=prompt)
            print(llamada_llm)
            result = llamada_llm(user_input)
            if len(result) > 0:
                st.info("¡Tu artículo ha sido generado con éxito!")
                st.write(result)
            else:
                st.error("¡No se pudo generar tu artículo!")

        with col2:
            st.subheader("Imagen Obtenida")
            image_url = fetch_photo(image_input)
            st.image(image_url)

        with col3:
            st.subheader("Descarga el articulo")
            image_response = requests.get(image_url)
            img = Image.open(io.BytesIO(image_response.content))
            doc = create_docx(user_input, result['text'], img)
            doc_buffer = io.BytesIO()
            doc.save(doc_buffer)
            doc_buffer.seek(0)
            st.download_button(
                label='Download Word Document',
                data=doc_buffer,
                file_name='document.docx',
                mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )

if __name__ == "__main__":
    main()
