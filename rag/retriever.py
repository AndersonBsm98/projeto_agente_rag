from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from pathlib import Path


DB_VECTOR = Path("D:/Projeto_agente_ia_gpt/data/raw/db")
COLLECTION = "vendas" #qualquer nome so estou criando uma colleção separada de busca
# A COLLECTION SERVE ENTAO PARA EU CONSEGUIR ATRIBUIR O BANCO A UMA COLLEÇAO

def Pretriever(pergunta) -> str:
    embeddings = OllamaEmbeddings(model="nomic-embed-text") # Fazendo o embbing da resposta

    vectorstore = Chroma(
        persist_directory=DB_VECTOR, # atribuindo o banco de pesquisa
        collection_name=COLLECTION, # atribuindo a coleção que sera usada e apontada para o banco
        embedding_function=embeddings  # usado para embedar a QUERY na hora da busca
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",        # estratégia: pegue os mais similares
        search_kwargs={"k": 3}           # parâmetro: traga 3 resultados
    )


    return retriever.invoke(pergunta)

