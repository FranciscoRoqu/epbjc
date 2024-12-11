def read_turmas():
    from src.connection import cursor
    cursor = cursor()
    cursor.execute("SELECT * FROM Turmas INNER JOIN Alunos INNER JOIN Professores ON Turmas.id_alunos = Alunos.id ON Turmas.id_professores = Professores.id")    
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)