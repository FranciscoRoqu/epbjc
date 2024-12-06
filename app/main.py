# Importar todos os pacotes do src
from src import *
# Importar os menus do src
from src import menus

# Chamar a função create_tables para criar as tabelas
create_tables()
# Função main
def main():
    # Definir a variável que vai recolher a escolha do utilizador para o segundo menu
    # Loop para repetir infinitamente
    while True:
        # Recolher a escolha do utilizador para o primeiro menu
        choice = menus.display_menu()
        # Começar a escolha principal para entrar no segundo menu correto
        match choice:
            # Caso choice seja 1 ou 2 ou 3 ou 4, o programa abre o segundo menu
            case 1 | 2 | 3 | 4:
                sub_choice = 0
                # Enquanto sub_choice != 4, executar o segundo menu
                while sub_choice != 4:
                    # Recolher o valor do segundo menu
                    sub_choice = menus.menu_desprincipal()
                    # Começar a escolher para o segundo menu
                    match sub_choice:
                        # Caso sub_choice seja 1 ou 2 ou 3, verificar qual foi a escolha feita no primeiro menu
                        case 1 | 2 | 3:
                            # Começar a escolha da variável choice
                            match choice:
                                # Em todos os casos, verificar qual função deve ser usada
                                case 1:
                                    match sub_choice:
                                        case 1:
                                            create_alunos()
                                case 2: 
                                    match sub_choice:
                                        case 1:
                                            read_alunos()
                                        case 2:
                                            read_professores()
                                        case 3:
                                            read_turmas()
                                case 3:
                                    break
                                case 4:
                                    break
                        case 4:
                            break
                        # Caso a opção não seja válida
                        case _:
                            print("Opção inválida")
            case 5:
                # Fechar a conexão
                close()
                break                             
            # Caso a opção não seja válida
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    main()