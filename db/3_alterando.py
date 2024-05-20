import sqlite3
from pathlib import Path

ROOTH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH/"clientes.db")
cursor = conexao.cursor()

##
##

# def criar_tabela(conexao, cursor):
#     cursor.execute(
#         "CREATE TABLE cliente (id INTERGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
#     )
#     conexao.commit() #nao tem necessidade

# def inserir_registro(conexao, cursor, nome, email):
#     data = (nome, email)  
#     cursor.execute("INSERT INTO cliente (nome, email) VALUES (?,?);", data)
#     conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)  
    cursor.execute("UPDATE cliente SET nome=?, email=?, WHERE id=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "JGisele", 'jg@gmail.com', 2)