def update_aluno():
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()

    cursor.execute("SELECT id,nome from Alunos")
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)

    dia = int(input("Introduza o id do aluno que deseja alterar: "))
    if dia >= len(resultados):
        print("Escolha o que deseja alterar:\n\t1. Nome\n\t2. Idade")
        media = int(input())