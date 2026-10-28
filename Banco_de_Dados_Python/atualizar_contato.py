from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "UPDATE contato SET nome = %s WHERE id = %s"
args = ("Lucas Y.", 44)

with nova_conexao as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')