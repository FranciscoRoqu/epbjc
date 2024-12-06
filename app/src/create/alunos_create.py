def create_alunos():
    # Importar a biblioteca random
    import random
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()
    # print("insert")
    # Lista de nome
    nomes = [
        "Ana",
        "Sofia",
        "Beatriz",
        "Camila",
        "Alice",
        "Clara",
        "Gabriela",
        "Helena",
        "Laura",
        "Júlia",
        "João",
        "Pedro",
        "Miguel",
        "Tiago",
        "Rafael",
        "Gabriel",
        "Lucas",
        "Daniel",
        "Henrique",
        "Eduardo"
    ]
    
    # cursor.execute("INSERT INTO Alunos(id,nome) VALUES(NULL,'Patrícia')")
    for i in range(50):
        nome = nomes[random.randint(0, len(nomes) - 1)]
        # print(nome)
        cursor.execute("INSERT INTO Alunos(nome,idade) VALUES(?,?)", (nome, random.randint(16,20)))

    # cursor.execute("INSERT INTO ALUNOS(id,nome,idade) values(52,'Bah',16)")
    commit()