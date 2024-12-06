def display_menu():
    # Mostrar o título do menu
    print("Menu Principal")
    # Mostrar as opções
    print("1. Inserir\n2. Imprimir\n3. Apagar\n4. Atualizar\n5. Sair")
    
    # Recolher o valor de escolha
    choice = int(input("Selecione uma opção: "))

    # Retornar choice
    return choice

def menu_desprincipal():
    # Mostrar as opções
    print("1. Aluno\n2. Professor\n3. Turma\n4. Voltar")

    # Recolher o valor de escolha
    choice = int(input("Selecione uma opção: "))

    # Retornar choice
    return choice