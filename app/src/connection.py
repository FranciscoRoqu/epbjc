# Import sqlite3
import sqlite3

# Criar a variável da conexão
conexao = sqlite3.connect("../sqliteDatabase/epbjc.db")

# Imprimir o número de elemento na tabela alunos
# só que sem variáveis
# print(len(sqlite3.connect("../sqliteDatabase/epbjc.db").cursor().execute("SELECT * FROM alunos").fetchall()))

# Definir a função para criar o cursor
def cursor():
    return conexao.cursor()

# Definir a função para fechar a conexão
def close():
    return conexao.close()

# Definir a função para salvar as mudanças feitas à base de dados
def commit():
    return conexao.commit()