from mysql.connector import ProgrammingError
from db import nova_conexao

sql = "INSERT INTO contatos(nome, tel) VALUES(%s, %s)"
parametros = ("Alô!?", "940028922")

with nova_conexao as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'1 registro gerado com o ID: {cursor.lastrowid}')