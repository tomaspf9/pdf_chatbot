#.venv\Scripts\Activate.ps1
from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings   


def main():
    load_dotenv()
    st.set_page_config(page_title="Read My Doc")
    st.header("Ingrese su documento")
    
    #--- Cargamos el archivo ---

    pdf = st.file_uploader("Upload your PDF", type ="pdf")

    #--- Extraemos el pdf ---
    if pdf is not None:
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
        st.write(chunks)

        #Pasos a seguir //

        #Crear Embeddings -> Crear Index semantico -> 

        embeddings = OpenAIEmbeddings()

    


if __name__ == '__main__':
    main()  