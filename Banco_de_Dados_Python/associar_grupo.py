from db import nova_conexao
from mysql.connector import ProgrammingError

selecionar_grupo = """
    SELECT id FROM grupo WHERE descricao = %s
"""

atualizar_contato = """
    UPDATE contatos SET grupo_id = %s WHERE nome = %s
"""

dicionario = {
    "Ana": "Casa",
    "Carol": "Trabalho",
    "Luiz": "Trabalho",
    "Amaro": "Casa",
}

with nova_conexao as conexao:
    cursor = conexao.cursor()
    
    for contato, grupo in dicionario.items():
        cursor.execute(selecionar_grupo, (grupo, ))
        grupo_id = cursor.fetchone()[0]
        cursor.execute(atualizar_contato, (grupo_id, contato))
        conexao.commit()