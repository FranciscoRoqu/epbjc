def delete_turma():
    from src.connection import cursor
    from src.connection import commit

    cursor = cursor()

    cursor.execute("SELECT id,nome from Alunos")
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)

    ingabunga = int(input("Introduza o id do aluno que deseja apagar: "))
    cursor.execute(f"DELETE FROM Aluno WHERE id={ingabunga}")
    commit()
    
    
    
    
    # match pergunta:
    #     case True:
    #         match crtz:
    #             case true:
    #                 match absoluta:
    #                     case true:
    #                         match warning:
    #                             case "nao":