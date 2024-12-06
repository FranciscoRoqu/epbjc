def create_alunos():
    # Importar as bibliotecas
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()
    # print("insert")
    # Lista de nome
    # nomes = [
    #     "Ana",
    #     "Sofia",
    #     "Beatriz",
    #     "Camila",
    #     "Alice",
    #     "Clara",
    #     "Gabriela",
    #     "Helena",
    #     "Laura",
    #     "Júlia",
    #     "João",
    #     "Pedro",
    #     "Miguel",
    #     "Tiago",
    #     "Rafael",
    #     "Gabriel",
    #     "Lucas",
    #     "Daniel",
    #     "Henrique",
    #     "Eduardo"
    # ]
    
    # cursor.execute("INSERT INTO Alunos(id,nome) VALUES(NULL,'Patrícia')")
    # for i in range(50):
    #     nome = nomes[random.randint(0, len(nomes) - 1)]
    #     # print(nome)
    #     cursor.execute("INSERT INTO Alunos(nome,idade) VALUES(?,?)", (nome, random.randint(16,20)))

    nome = input("Insira o nome da turma: ")
    choice = input("Deseja introduzir um aluno ou um professor?\n=> ").lower()
    match choice:
        case "aluno" | "a":
            id_aluno = int(input("Introduza o id do aluno: "))
        case "professor" | "p":
            id_professor = int(input("Introduza o id do professor: "))
            cursor.execute(f"INSERT INTO (nome) VALUES('{nome}')")
    commit()