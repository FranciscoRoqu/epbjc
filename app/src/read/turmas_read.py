def read_turmas():
    from src.connection import cursor

    cursor().execute('''
                    SELECT * FROM Turmas
                    ''')
    
    resultados = cursor().fetchall()

    
    for resultado in resultados:
        print(resultado)