from mysql.connector import connect

conexao = connect(
    host="localhost",
    user="root",
    port=3306,
    passwd="12345678",
)

print(conexao)