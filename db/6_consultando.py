import sqlite3
from pathlib import Path

ROOTH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH/"clientes.db")
cursor = conexao.cursor()

##
##

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM cliente WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor, 2)
print(cliente)

#
#
#
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM cliente ORDER BY nome DESC;")

cli = listar_clientes(cursor)
for cliente in cli:
     print(cli)