from db import nova_conexao
from mysql.connector import ProgrammingError

inserir_grupo_1 = """
    INSERT INTO grupo(descricao) VALUES(%s)
"""
parametros = (
    ('Casa', ),
    ('Trabalho',)
)

try:
    with nova_conexao as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(inserir_grupo_1, parametros)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro Conexão: {e.msg}')
