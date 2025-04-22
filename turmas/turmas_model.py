# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# class Turmas(db.Model):
#     __tablename__ = "Turmas"
#     id = db.Column(db.Integer,primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.String(100), nullable=False)
#     professor_id = db.Column(db.Integer, db.ForeignKey('request.id'))
#     ativo = db.Column(db.Boolean, nullable=False)

class Turma_nao_encontrada(Exception):
    pass

def turma_por_id(id_turma):
    lista_turmas = dados['turmas']
    for turma in lista_turmas:
        if turma['id'] == id_turma:
            return turma 
    raise Turma_nao_encontrada

def turma_existe(id_turma):
    try:
        turma_por_id(id_turma)
        return True
    except Turma_nao_encontrada:
        return False

def atualiza_turma(id_turma, novos_dados):
    turma = turma_por_id(id_turma)
    turma.update(novos_dados)

def adiciona_turma(dict):
    dados['turmas'].append(dict)
    
def lista_turmas():
    return dados['turmas']

def apaga_todas_turmas():
    dados['turmas'] = []

def apaga_turma(id_turma):
    lista_turmas = dados['turmas']
    for turma in lista_turmas:
        if turma['id'] == id_turma:
            lista_turmas.remove(turma)
            return True
    raise Turma_nao_encontrada

# dados = {
#    "turmas": [
#         {
#             "id": 1,
#             "descricao": "Turma de Matematica",
#             "professor_id": 101,
#             "ativo": True  
#         },
#         {}
#    ]
# }