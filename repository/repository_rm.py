from server import consulta

class multimesas_repository:
    def getAll():
        return consulta("select * from Fundos")