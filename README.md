#Implementação de RAG utilizando PDF como fonte de dados.

A aplicação usa o modelo de llm (local) ollama [mistral](https://ollama.com/library/mistral)

Utilizei as libs do langchain pra carregar o pdf, e splitar ele em paginas e chunks e armazenar em ids de padrão "data/arquivo.pdf: pagina : chunk"

Print da interface do streamlit ---> resposta gerada com base no pdf + fonte de consulta (id)
<img width="1709" alt="image" src="https://github.com/user-attachments/assets/7ba2b21a-0754-46d8-a490-acece1625cc8">





## Como rodar

1. Crie um ambiente virtual:
```python -m venv venv```

2. Ative ele com:
```
source venv/bin/activate #macos
venv\Scripts\activate #windows
```

3. Instale as dependencias (localizadas em requirements.txt) com:

```pip install -r requirements.txt```

4. Processo de instalação e setup do ollama (caso não tenha):
   
------------------------------------------------------------------------------


- Primeiro, baixe e instale o Ollama. [site oficial](https://ollama.com/)

- Após instalar, inicie o ollama com: 
    ```ollama run```

- Pull no modelo que estou utilizando (nesse caso, mistral):

    ```ollama pull mistral```

- Execute o modelo:

    ```ollama run mistral```
------------------------------------------------------------------------------

5. Rodar o script query_data.py utilizando o streamlit (front end simples):

```streamlit run query_data.py```

## Relativo ao db

Para alimentar o db, basta colocar algum arquivo .pdf na pasta 'DATA', localizada na raiz, e rodar o populate_database.py com: 

```python populate_database.py```

Para limpar as informações do db, basta rodar o código acima com a flag --reset.








