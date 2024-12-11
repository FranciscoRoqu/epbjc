def create_turma():
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()

    nome = input("Insira o nome da turma: ")
    choice = input("Deseja introduzir um A (Aluno) ou um P (Professor), N (Introduzir nenhum)?\n=> ").lower()
    match choice:
        case "aluno" | "a":
            id_aluno = int(input("Introduza o id do aluno: "))
            cursor.execute(f"INSERT INTO Turmas(nome,id_alunos,id_professores) VALUES('{nome}',{id_aluno},0)")
        case "professor" | "p":
            id_professor = int(input("Introduza o id do professor: "))
            cursor.execute(f"INSERT INTO Turmas(nome,id_alunos,id_professores) VALUES('{nome}',0,{id_professor})")
        case "nenhum" | "n":
            cursor.execute(f"INSERT INTO Turmas(nome,id_alunos,id_professores) VALUES('{nome}',0,0)")
    commit()