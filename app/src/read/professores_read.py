def read_professores():
    from src.connection import cursor

    cursor().execute('''
                    SELECT * FROM Professores
                    ''')
    
    resultados = cursor().fetchall()

    
    for resultado in resultados:
        print(resultado)