from ClassRagEngine import Rag
from pathlib import Path


DB_VECTOR = Path("D:/Projeto_agente_ia_gpt/data/raw/db")
COLLECTION = "vendas"

rag = Rag(
    model_name = "qwen2.5",
    model_retriver = "nomic-embed-text",
    path_db= DB_VECTOR,
    collection = COLLECTION,
    type_question = "similarity",
    K= 3
)

while True: 

    pergunta = input("Qual a sua pergunta hoje ?")

    run = rag.run(pergunta)

    print(run)