def read_alunos():
    # print("read")
    from src.connection import cursor
    cursor = cursor()
    cursor.execute('''
                    SELECT * FROM Alunos
                    ''')
    
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)