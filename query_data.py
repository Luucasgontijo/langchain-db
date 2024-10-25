import streamlit as st
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """ 
Responda a pergunta com base no contexto abaixo:

{context}

---

pergunta: {question}
"""

def query_rag(query_text: str):
    #prepara as partes do db
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # procura no db
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Resposta: \n\n{response_text}\n\FONTES: {sources}"
    return formatted_response

def main():
    st.title("Query RAG app")  
    query_text = st.text_input("Digite sua pergunta:")  

    if st.button("Enviar"): 
        if query_text:
            response = query_rag(query_text)  
            st.write(response)  
        else:
            st.warning("Por favor, digite uma pergunta")  

if __name__ == "__main__":
    main()