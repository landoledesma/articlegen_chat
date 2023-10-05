from langchain.prompts import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os
import openai
from dotenv import load_dotenv
import streamlit as st 
import os
from docx import Document
from docx.shared import Inches
import io
from PIL import Image
import requests
from fetch_images import fetch_photo

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

query = 'kitties'
src_original_url = fetch_photo(query)
if src_original_url:
    print(f"Original URL for query '{query}': {src_original_url}")
else:
    print("No se pudo traer imagens lo siento")
