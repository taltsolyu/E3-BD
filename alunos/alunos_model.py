# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# class Alunos(db.Model):
#     __tablename__ = "Alunos"
#     id = db.Column(db.Integer,primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     idade = db.Column(db.Integer)
#     data_nascimento = db.Column(db.DateTime, nullable=False)
#     nota_primeiro_semestre = db.Column(db.Float)
#     nota_segundo_semestre = db.Column(db.Float)
#     media_final = db.Column(db.Float)
#     turma_id = db.Column(db.Integer, db.ForeingnKey('turmas.id'),nullable=False)

dados = {}

alunos = dados
aluno_id_controle = 1  # Isso precisa estar aqui para o adicionar_aluno funcionar corretamente

class AlunoNaoEncontrado(Exception):
    pass

def listar_alunos():
    return alunos["alunos"]

def aluno_por_id(id_aluno):
    aluno = next((a for a in alunos["alunos"] if a.get("id") == id_aluno), None)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno

def adicionar_aluno(data):
    global aluno_id_controle
    novo_aluno = {
        "id": aluno_id_controle,
        "nome": data["nome"],
        "idade": data["idade"],
        "turma_id": data.get("turma_id"),
        "data_nascimento": data.get("data_nascimento"),
        "nota_primeiro_semestre": float(data["nota_primeiro_semestre"]),
        "nota_segundo_semestre": float(data["nota_segundo_semestre"]),
        "media_final": float(data["media_final"])
    }
    alunos["alunos"].append(novo_aluno)
    aluno_id_controle += 1
    return novo_aluno

def atualizar_aluno(id_aluno, data):
    aluno = aluno_por_id(id_aluno)
    aluno["nome"] = data.get("nome", aluno["nome"])
    aluno["idade"] = data.get("idade", aluno["idade"])
    aluno["turma_id"] = data.get("turma_id", aluno["turma_id"])
    aluno["data_nascimento"] = data.get("data_nascimento", aluno["data_nascimento"])
    aluno["nota_primeiro_semestre"] = float(data.get("nota_primeiro_semestre", aluno["nota_primeiro_semestre"]))
    aluno["nota_segundo_semestre"] = float(data.get("nota_segundo_semestre", aluno["nota_segundo_semestre"]))
    aluno["media_final"] = float(data.get("media_final", aluno["media_final"]))
    return aluno

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    alunos["alunos"].remove(aluno)

# dados = {
#     "alunos": [
#         {
#             "id": 1
#             "nome": "Maria Silva",
#             "turma_id": 101,
#             "idade": 20,
#             "data_nascimento": "2004-03-19",
#             "nota_primeiro_semestre": 8.5,
#             "nota_segundo_semestre": 9.0,
#             "media_final": 8.75
#         },
#         {}
#     ]
# }