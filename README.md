## Generador de Artículos con Inteligencia Artificial

Este proyecto utiliza Inteligencia Artificial para generar artículos basados en una entrada de texto dada por el usuario. Además, recupera una imagen relacionada y ofrece la opción de descargar el artículo en formato Word (.docx).

### Pre-requisitos

Antes de ejecutar el código, necesitas instalar las siguientes bibliotecas:

- `streamlit`
- `python-dotenv`
- `docx`
- `requests`
- `Pillow`
- Además, asegúrate de tener las bibliotecas `langchain.prompts`, `langchain.chains`, y `langchain.chat_models`. Estas podrían ser específicas de un paquete privado o desarrolladas internamente.

### Configuración

1. Crear un archivo `token.env` en el directorio raíz y añadir tu clave API de OpenAI como:
   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```

2. Asegúrate de tener un script o función `fetch_photo` en el archivo `fetch_images.py` que devuelva la URL de una imagen basada en un tema dado.

### Ejecución

Para ejecutar la aplicación, simplemente corre:
```
streamlit run nombre_del_archivo.py
```

### Cómo usar

1. Abre la aplicación en tu navegador (usualmente es `http://localhost:8501/` si se ejecuta localmente).
2. Introduce un tema/idea para el artículo que deseas generar.
3. Introduce un tema para la imagen que deseas obtener.
4. Espera a que la IA genere el contenido y la imagen se recupere.
5. Descarga el artículo generado en formato Word si lo deseas.

### Contribuciones

Siéntete libre de hacer fork de este proyecto y realizar tus propias modificaciones. Las Pull Requests son bienvenidas.

---

Espero que este README te sea útil y te ayude a comprender y utilizar mejor el proyecto. ¡Buena suerte!