#.venv\Scripts\Activate.ps1
from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import faiss
from langchain.memory import ConversationBufferMemory
import datetime


#def get_pdf_text(pdf_docs):


#def get_text_chunks(text):


#def get_vectorstore(text_chunks):


#def get_conversation_chain(vectorstore):



def main():
    load_dotenv()
    st.set_page_config(page_title="Read My Doc")
    archivos_cargados = st.session_state.get("archivos", [])
    st.header("Ingrese su documento")
    st.text_input("Pregunte algo relacionado con su documento", key="input_text")

    st.markdown("""
        <style>
            div[data-baseweb="input"] {
                width: 500px !important;
                height: 50px !important;
                font-size: 40px !important;
                
            }
        </style>
    """, unsafe_allow_html=True)
    
    
    #--- Cargamos el archivo ---

    pdf = st.file_uploader("Upload your PDF", type ="pdf")

    background_container_up_style = """
    <style>
    .background-container-up {
        background-image: url('https://wallpapers.com/images/featured/ultra-hd-wazf67lzyh5q7k32.webp');
        background-size: cover;
        padding: 110px;
        border-radius: 20px;
    }
    </style>
    """
    # Aplicar el estilo del contenedor de arriba
    st.markdown(background_container_up_style, unsafe_allow_html=True)

    # Contenedor de arriba
    st.markdown('<div class="background-container-up">', unsafe_allow_html=True)
    #--------Fin---------

      #--------Seccion gif y titulo--------
    col1, col2 = st.columns([3, 1])  # Dividir el espacio en 3/4 para el título y 1/4 para la imagen
    with col1:
        st.markdown("<h2 style='margin-top: 40px;'>Ingrese su documento</h2>", unsafe_allow_html=True)
    with col2:
        st.image("imagenes/documento.gif", width=150, use_column_width=False)

    # Cerrar el contenedor de fondo
    st.markdown('</div>', unsafe_allow_html=True)


    #--- Extraemos el pdf ---
    if pdf is not None:
        archivos_cargados.append(pdf.name)  # Agregar el nombre del archivo a la lista de archivos cargados
        st.session_state["archivos"] = archivos_cargados  # Actualizar la lista de archivos cargados en el estado de la sesión

        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Separar en chunks
            #Clase text splitter
            #Dividir los chunks en 1000, despues el siguiente chunk arranca 200 caracteres antes 

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len

        )

        #Corremos nuestro textsplitter 
        chunks = text_splitter.split_text(text)
        #st.write (chunks)
        return chunks

        #Pasos a seguir //

        #Crear Embeddings -> Crear Index semantico -> 
    # Estilo CSS para el contenedor de abajo
    background_container_down_style = """
    <style>
    .background-container-down {
        background-image: url('https://wallpapers.com/images/hd/blue-orange-firewatch-tower-wvnoqi9lqoxfj6ob.webp');
        background-size: cover;
        padding: 110px;
        border-radius: 20px;
    }
    </style>
    """
    # Aplicar el estilo del contenedor de abajo
    st.markdown(background_container_down_style, unsafe_allow_html=True)

    # Contenedor de abajo
    st.markdown('<div class="background-container-down">', unsafe_allow_html=True)
    #-------------FIN---------------

    #---------Seccion barra lateral----------
    #imagen barra lateral izquierda
    st.sidebar.image("imagenes/izquierda.jpeg", output_format="PNG", caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    # Estilo CSS para ajustar el tamaño de la imagen
    st.markdown(f"""
        <style>
            .sidebar .stImage > img {{
                max-width: 150px;
                max-height: 100px;
                border-radius: 20px;
                padding: 110px;
                background-size: cover;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Archivos anteriores de PDF cargados
    st.sidebar.markdown("### Archivos Anteriores de PDF Cargados")

    # Mostrar archivos anteriores de PDF cargados
    for pdf in archivos_cargados:
        st.sidebar.write(pdf)

    #-----------FIN-----------
        

    def get_vectorstore(text_chunks):

        embeddings = OpenAIEmbeddings()
        vectorstore = faiss.from_texts(text = text_chunks, embeddings = embeddings)
        return vectorstore

    


if __name__ == '__main__':
    main()  