def create_professor():
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()

    nome = input("Insira o nome do professor: ")
    choice = input("Deseja introduzir a idade do professor?\n=> ").lower()
    match choice:
        case "s" | "sim":
            idade = int(input("Introduza a idade do professor: "))
            cursor.execute(f"INSERT INTO Professores(nome,idade) VALUES('{nome}',{idade})")
        case "n" | "não":
            cursor.execute(f"INSERT INTO Professores(nome) VALUES('{nome}')")
    commit()