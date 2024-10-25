# # import streamlit as st
# # import ollama

# from langchain.document_loaders import PyPDFLoader  # Corrigido
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema import Document  # Ajuste correto para importação
# from typing import List  # Tipagem para Python 3.8 ou anterior

# DATA_PATH = 'data/manual-corsa-2008.pdf'

# def load_documents() -> List[Document]:
#     # PyPDFLoader carrega um único PDF ao invés de um diretório
#     document_loader = PyPDFLoader(DATA_PATH)
#     return document_loader.load()

# def split_documents(documents: List[Document]):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=80,
#         length_function=len,
#         separators=["\n\n", "\n", " "]  # Boa prática incluir separadores
#     )
#     return text_splitter.split_documents(documents)

# # 







# streamlit
st.title('Ollama API Demo')
user_input = st.text_input('Enter your question here:')


if st.button("Send"):
    if user_input:
        response = ollama.generate(model='', prompt=user_input)
        st.write(response['response'])
    else:
        st.write("Please enter a question.")

