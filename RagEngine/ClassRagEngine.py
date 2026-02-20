from langchain_ollama import ChatOllama
from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from pathlib import Path
from prompt import PROMPT, message
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


class Rag:
    def __init__(self, model_name,model_retriver, path_db, collection, type_question, K ):
        self.llm = ChatOllama(model=model_name)
        self.embedding = OllamaEmbeddings(model=model_retriver)
        self.vectorstore  = Chroma(
            persist_directory=path_db, 
            collection_name=collection, 
            embedding_function=self.embedding  
        )

        self.retriver = self.vectorstore.as_retriever(
            search_type= type_question,       
            search_kwargs={"k": K}          
        )
        self.chat_history = []


    

    def Pretriever(self, question) -> str:

        return self.retriver.invoke(question)
    
    def context_builder(self,docs):

        context = "" 

        for i, doc in enumerate(docs, start=1): 
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
    
    def greeting(self):
        greeting = AIMessage(content="Olá! Sou seu analista de estoque. Como posso ajudar você hoje?")
        self.chat_history.append(greeting)
        return greeting.content



    def run(self,ask):
                
        docs = self.Pretriever(ask)

        context = self.context_builder(docs)

        user_message = message(ask, context)

        msg = [PROMPT] + self.chat_history + [user_message] 

        response = self.llm.invoke(msg)


        return response.content

      

