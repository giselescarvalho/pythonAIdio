import sqlite3
from pathlib import Path

ROOTH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH/"clientes.db")
cursor = conexao.cursor()

##
##

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM cliente WHERE id=?;", data)
    conexao.commit()

excluir_registro(conexao, cursor, 2)