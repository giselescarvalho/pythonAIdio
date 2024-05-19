import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conexao = sqlite3.connect(ROOT/"clientes.db")

cursor = conexao.cursor()
cursor.execute('CREATE TABLE cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

print(conexao)