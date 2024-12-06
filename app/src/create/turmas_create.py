def create_turma():
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()

    nome = input("Insira o nome do aluno: ")
    choice = input("Deseja introduzir a idade do aluno?\n=> ").lower()
    match choice:
        case "s" | "sim":
            idade = int(input("Introduza a idade do aluno: "))
            cursor.execute("INSERT INTO Alunos(nome,idade) VALUES(?,?)", (nome,idade))
        case "n" | "não":
            cursor.execute(f"INSERT INTO Alunos(nome) VALUES('{nome}')")
    commit()