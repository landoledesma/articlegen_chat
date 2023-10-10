from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st 
from docx import Document
from docx.shared import Inches
import io
from PIL import Image
from fetch_images import fetch_photo
import requests

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def load_llm(template):
    llm  = ChatOpenAI(
        max_tokens=2000,
        temperature=0.5
        )
    
    llm_chain = LLMChain(
        llm = llm,
        prompt=PromptTemplate.from_template(template),
    )
    return llm_chain

def create_docx(user_input,paragraph,image_input):
    doc = Document()
    doc.add_heading(user_input)
    doc.add_paragraph(paragraph)

    doc.add_heading('Image',level=1)
    image_stream = io.BytesIO()
    image_input.save(image_stream,format='PNG')
    image_stream.seek(0)
    doc.add_picture(image_stream,width=Inches(4))

    return doc

st.set_page_config(layout="wide")

def main():
    st.title("Aplicación Generadora de Artículoscon AI")

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
            image_input = "temp_image.jpg"
            image_response = requests.get(image_url)
            img = Image.open(io.BytesIO(image_response.content))
            doc = create_docx(user_input, result['text'],img)

            # Save the Word document to a BytesIO buffer
            doc_buffer = io.BytesIO()
            doc.save(doc_buffer)
            doc_buffer.seek(0)

            # Prepare the download link
            st.download_button(
                label='Download Word Document',
                data=doc_buffer,
                file_name='document.docx',
                mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )


if __name__ == "__main__":
    main()