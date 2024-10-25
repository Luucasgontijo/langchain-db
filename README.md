#  Rag simples usando pdf como base
A aplicação usa o modelo de llm (local) ollama mistral.
Utilizei as libs do langchain pra carregar o pdf, e splitar ele em paginas e chunks e armazenar em ids de padrão "data/arquivo.pdf: pagina : chunk"



## Como rodar

1. Crie um ambiente virtual:
```python -m venv venv```

2. Ativei ele com:
```
source venv/bin/activate #mac
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








