import sqlite3
import random
from datetime import datetime, timedelta

# =========================
# Configurações
# =========================
DB_PATH = "data/raw/vendas_lojas.db"
NUM_REGISTROS = 5000

LOJAS = [
    "Loja Centro SP", "Loja Norte RJ", "Loja Sul RS",
    "Loja Interior MG", "Loja Litoral SC",
    "Loja Centro BH", "Loja Zona Oeste SP"
]

CATEGORIAS = {
    "Eletrônicos": ["Notebook", "Smartphone", "Tablet", "Monitor"],
    "Casa": ["Liquidificador", "Geladeira", "Microondas"],
    "Esporte": ["Bicicleta", "Esteira", "Halteres"],
    "Moda": ["Tênis", "Jaqueta", "Calça Jeans"]
}

REGIOES = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]

STATUS_LOJA = ["normal", "destaque", "fraca"]

# =========================
# Funções auxiliares
# =========================
def faixa_preco(preco):
    if preco < 500:
        return "baixo"
    elif preco < 2000:
        return "medio"
    return "alto"


def margem_categoria(preco, custo):
    margem = (preco - custo) / preco
    if margem < 0.2:
        return "baixa"
    elif margem < 0.4:
        return "media"
    return "alta"


def nivel_estoque(estoque):
    if estoque < 20:
        return "critico"
    elif estoque < 50:
        return "baixo"
    return "normal"


def data_aleatoria():
    inicio = datetime.now() - timedelta(days=365)
    return inicio + timedelta(days=random.randint(0, 365))


# =========================
# Criação do banco
# =========================
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas_lojas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loja TEXT,
    produto TEXT,
    categoria TEXT,
    preco REAL,
    custo REAL,
    quantidade_vendida INTEGER,
    estoque INTEGER,
    regiao TEXT,
    data_venda TEXT,
    status_loja TEXT,
    faixa_preco TEXT,
    margem TEXT,
    nivel_estoque TEXT,
    loja_alta_performance INTEGER,
    produto_premium INTEGER
)
""")

# =========================
# Inserção dos dados
# =========================
for _ in range(NUM_REGISTROS):
    loja = random.choice(LOJAS)
    categoria = random.choice(list(CATEGORIAS.keys()))
    produto = random.choice(CATEGORIAS[categoria])

    preco = round(random.uniform(100, 6000), 2)
    custo = round(preco * random.uniform(0.5, 0.85), 2)

    quantidade_vendida = random.randint(1, 200)
    estoque = random.randint(0, 120)

    regiao = random.choice(REGIOES)
    status = random.choice(STATUS_LOJA)

    faixa = faixa_preco(preco)
    margem = margem_categoria(preco, custo)
    nivel = nivel_estoque(estoque)

    loja_perf = 1 if quantidade_vendida > 120 else 0
    premium = 1 if preco > 3000 else 0

    cursor.execute("""
        INSERT INTO vendas_lojas (
            loja, produto, categoria, preco, custo,
            quantidade_vendida, estoque, regiao,
            data_venda, status_loja,
            faixa_preco, margem, nivel_estoque,
            loja_alta_performance, produto_premium
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        loja, produto, categoria, preco, custo,
        quantidade_vendida, estoque, regiao,
        data_aleatoria().isoformat(),
        status, faixa, margem, nivel,
        loja_perf, premium
    ))

conn.commit()
conn.close()

print("✅ Banco SQLite criado com sucesso!")
