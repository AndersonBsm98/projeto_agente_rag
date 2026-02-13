def context_builder(docs):

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

# Basicamente escreve um TEXTO em memoria que aponta para os metadados para
# Que a IA consiga entender mais facil o que procurar com pistar, isso aumenta
# A resposta certa junto com o prompt 

#QUEM FAZ A BUSCA NO BANCO VETORIAL E O RETRIVER E NAO A IA 
# |COM OS DADOS VETORIZADOS O RETRIVER DA O RETORNO DE QUAIS INFORMAÇÔES SAO
#MAIS RELEVANTES


# A IDEIA AQUI E UMA CHAIN 
# USUARIO -> RETRIVER ( EMBEDING + VETORIAL ) -> DOCS -> CONTEXT BUILDER -> LLM -> RESPOSTA