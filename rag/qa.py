from context_builder import context_builder
from prompt import PROMPT
from retriever import Pretriever
from langchain_ollama import ChatOllama


def IA(pergunta):


    docs = Pretriever(pergunta)

    context = context_builder(docs)

    prompt = PROMPT(pergunta, context)

    llm = ChatOllama(model="qwen2.5")

    resposta = llm.invoke(prompt)

    return resposta.content


pergunta = "QUal loja tem o nimel do estoque critico ?, e se isso parece uma boa venda ao pedido estar em um estoque critico ?"

print(IA(pergunta))