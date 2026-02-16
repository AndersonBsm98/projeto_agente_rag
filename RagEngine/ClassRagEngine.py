from langchain_ollama import ChatOllama
from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from pathlib import Path
from prompt import PROMPT

class Rag:
    def __init__(self, model_name,model_retriver, path_db, collection, type_question, K ):
        self.llm = ChatOllama(model=model_name)
        self.embedding = OllamaEmbeddings(model=model_retriver)
        self.vectorstore = vectorstore = Chroma(
            persist_directory=path_db, 
            collection_name=collection, 
            embedding_function=self.embedding  
        )

        self.retriver = self.vectorstore.as_retriever(
            search_type= type_question,       
            search_kwargs={"k": K}          
        )


    def generate(self,prompt):
        
        response =  self.llm.invoke(prompt)
        return response.content
    

    def Pretriever(self, question) -> str:

        return self.retriver.invoke(question)
    
    def context_builder(self,docs):

        context = "" #Aqui é o contexto da IA que sera gerados pelo retriver

        for i, doc in enumerate(docs, start=1): # pega os documentos do retriver
            context +=f'''

        [DOC {i}]

        TEXTO:
        {doc.page_content}      
        META:
        loja={doc.metadata.get("loja")} |
        nivel_estoque={doc.metadata.get("nivel_estoque")} |
        margem={doc.metadata.get("margem")} |
        produto={doc.metadata.get("produto")} |
        regiao={doc.metadata.get("regiao")} |
        categoria={doc.metadata.get("categoria")} |
        loja_alta_performance={doc.metadata.get("loja_alta_performance")} |

    '''
            
        return context



    def run(self,pergunta):

        docs = self.Pretriever(pergunta)

        context = self.context_builder(docs)

        prompt = PROMPT(pergunta, context)

        llm = self.generate(prompt)

        return llm

      

