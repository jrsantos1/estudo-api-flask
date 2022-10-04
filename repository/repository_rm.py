from server import consulta
from services.consultas import todos_os_fundos_filtro 

class multimesas_repository:
    def getAll():
        return consulta("select * from Fundos")
    def get_by_name(todo_id):
        return consulta(todos_os_fundos_filtro(todo_id))