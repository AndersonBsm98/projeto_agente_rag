from app.rag.qa import IA

# criar uma comunicação entre o usuario e a IA 

while True:

    
    pergunta = input("OLA ME DIGA EM QUE POSSO AJUDAR ?")

    IA(pergunta)

    if pergunta == "q" or pergunta == "sair":
        break

