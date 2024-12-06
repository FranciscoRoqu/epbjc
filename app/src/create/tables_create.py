def create_tables():
    from src.connection import cursor
    from src.connection import commit
    cursor().execute('''
                    CREATE TABLE IF NOT EXISTS Alunos(
                        id    INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome  TEXT NOT NULL,
                        idade INTEGER
                   )
                    ''')
    
    cursor().execute('''
                    CREATE TABLE IF NOT EXISTS Professores(
                        id    INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome  TEXT NOT NULL,
                        idade INTEGER
                   )
                    ''')
    
    cursor().execute('''
                    CREATE TABLE IF NOT EXISTS Turmas(
                        id             INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome           TEXT NOT NULL,
                        id_alunos      INTEGER NOT NULL,
                        id_professores INTEGER NOT NULL,
                     
                        FOREIGN KEY(id_alunos)       REFERENCES Alunos(id)
                        FOREIGN KEY(id_professores) REFERENCES Professores(id)
                   )
                    ''')
    
    commit()