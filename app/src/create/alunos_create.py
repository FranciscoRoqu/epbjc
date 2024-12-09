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

    nome = input("Insira o nome do aluno: ")
    choice = input("Deseja introduzir a idade do aluno?\n=> ").lower()
    match choice:
        case "s" | "sim":
            idade = int(input("Introduza a idade do aluno: "))
            cursor.execute("INSERT INTO Alunos(nome,idade) VALUES(?,?)", (nome,idade))
        case "n" | "não":
            cursor.execute(f"INSERT INTO Alunos(nome) VALUES('{nome}')")
    commit()