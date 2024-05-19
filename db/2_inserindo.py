import sqlite3
from pathlib import Path

ROOTH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH/"clientes.db")
cursor = conexao.cursor()

data = ("Giselle", "giselle@email.com.br")
cursor.execute('INSERT INTO cliente(nome, email) VALUES (?,?);', data)

conexao.commit()