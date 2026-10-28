from mysql.connector import ProgrammingError
from db import nova_conexao

sql = "INSERT INTO contatos(nome, tel) VALUES(%s, %s)"
parametros = (
    ("Alô!?", "940028922")
    ("Will Smith?", "940028921")
    ("Vasco", "940028923")
    ("Pepino", "940028924")
    ("Goku", "940028925")
)

with nova_conexao as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, parametros)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram gerados {cursor.rowcount} registros')