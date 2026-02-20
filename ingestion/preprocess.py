import sqlite3
import pandas as pd
import json
from pathlib import Path

path_json = Path("D:/Projeto_agente_ia_gpt/data/processed/vendas.jsonl")

db_path = r"D:\Projeto_agente_ia_gpt\data\raw\vendas_lojas.db"
conn = sqlite3.connect(db_path)

query = f"SELECT * FROM vendas_lojas;"

df = pd.read_sql_query(query, conn)


for _, row in df.iterrows():
    text = (
    f"Loja: {row['loja']}. "
    f"Produto: {row['produto']}. "
    f"Categoria: {row['categoria']}. "
    f"Preço: {row['preco']}. "
    f"Custo: {row['custo']}. "
    f"Quantidade vendida: {row['quantidade_vendida']}. "
    f"Estoque: {row['estoque']}. "
    f"Região: {row['regiao']}. "
    f"Data da venda: {row['data_venda']}. "
    f"Status da loja: {row['status_loja']}. "
    f"Faixa de preço: {row['faixa_preco']}. "
    f"Margem: {row['margem']}. "
    f"Nível de estoque: {row['nivel_estoque']}. "
    f"Loja alta performance: {row['loja_alta_performance']}. "
    f"Produto premium: {row['produto_premium']}."
)


    DICT_JSONL = {
        "id": row["id"],
        "text": text,
        "metadata":{
            "loja": row["loja"],
            "produto": row["produto"],
            "margem": row["margem"],
            "nivel_estoque": row["nivel_estoque"],
            "regiao": row["regiao"],
            "categoria": row["categoria"],
            "faixa_preco": row["faixa_preco"],
            "data_venda": row["data_venda"],
            "loja_alta_performance": row["loja_alta_performance"]


        }   
    }
    
    with open(path_json, "a+", encoding="utf-8") as f:
        f.write(json.dumps(DICT_JSONL, ensure_ascii=False) + "\n")