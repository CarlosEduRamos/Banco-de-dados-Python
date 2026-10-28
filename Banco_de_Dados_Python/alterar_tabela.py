from db import nova_conexao
from mysql.connector import ProgrammingError

alter = "ALTER TABLE contatos ADD COLUMN id INT AUTOINCRENT PRIMARY KEY"

with nova_conexao as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(alter)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')