from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document
from pathlib import Path
import json

PATH_JSONL = Path("D:/Projeto_agente_ia_gpt/data/processed/vendas.jsonl")
DB = Path("D:/Projeto_agente_ia_gpt/data/raw/db")


jsonl = []

with open(PATH_JSONL, "r", encoding="utf-8") as f:
    for line in f:
        jsonl.append(json.loads(line))


struct = []

for dados in jsonl:
    structl = {
    "text": dados["text"],
    "metadata": dados["metadata"]}

    struct.append(structl)


documents = [
    Document(page_content=d["text"], metadata=d["metadata"])
    for d in struct
]

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=str(DB),
    collection_name="vendas"
)
