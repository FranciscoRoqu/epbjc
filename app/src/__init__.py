from src.create.tables_create import create_tables
from src.create.alunos_create import create_alunos 
# from src.create.turmas_create import 
# from src.create.professores_create import 
from src.read.alunos_read import read_alunos
from src.read.turmas_read import read_turmas
from src.read.professores_read import read_professores
# from src.delete.alunos_delete import 
# from src.delete.turmas_delete import 
# from src.delete.professores_delete import 
# from src.update.alunos_update import 
# from src.update.turmas_update import 
# from src.update.professores_update import 
from src.connection import close

__all__ = [
    'create_alunos',
    # 'turmas_create',
    # 'professores_create',
    'read_alunos',
    'read_turmas',
    'read_professores',
    # 'alunos_delete',
    # 'turmas_delete',
    # 'professores_delete',
    # 'alunos_update',
    # 'turmas_update',
    # 'professores_update'
    'create_tables',
    'close'
]