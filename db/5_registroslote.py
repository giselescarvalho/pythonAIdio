import sqlite3
from pathlib import Path

ROOTH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH/"clientes.db")
cursor = conexao.cursor()

##
##

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO cliente (nome, email) VALUES(?,?)", dados)
    conexao.commit()

dados = [
    ('Jonas', 'jonas@email.com'),
    ('Maria', 'maria@gmail.com')
]    

inserir_muitos(conexao, cursor, dados)