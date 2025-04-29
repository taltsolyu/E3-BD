from config import db
import copy
from sqlalchemy.inspection import inspect


class Professor(db.Model):
    __tablename__ = "Professor"
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(100), nullable=True)
    
    # def __init__(self, id, nome, idade, materia, observacoes):
    #     self.id = id
    #     self.nome = nome
    #     self.idade = idade
    #     self.materia = materia
    #     self.observacoes = observacoes
    
    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'materia': self.materia, 'observacoes': self.observacoes}

class criarProfessorErro(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

class ProfessorNaoEncontrado(Exception):
    pass

def getTodosProfessores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def criarProfessor(dados):
    for key, value in dados.items():
        if(not value):
          raise criarProfessorErro(f"O campo '{key}' é obrigatório e deve estar preenchido.")
    novo_professor = Professor(**dados)
    db.session.add(novo_professor)
    db.session.commit()
    return novo_professor.to_dict()

def getPorIdProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    print(f"professor: {professor}")
    print(f"type(professor): {type(professor)}")
    print(f"professor is None: {professor is None}")
    print(f"bool(professor): {bool(professor)}")
    if professor is None:
        raise ProfessorNaoEncontrado
    return professor.to_dict()

def attProfessor(idProfessor, novoProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    professor = merge_objects(professor, Professor(**novoProfessor))
    db.session.commit()
    return professor.to_dict()

def merge_objects(obj1, obj2):
    for attr in inspect(obj1).mapper.column_attrs:
        key = attr.key
        new_value = getattr(obj2, key)

        if new_value is not None and new_value != getattr(obj1, key):
            setattr(obj1, key, new_value)

    return obj1

def deletarProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(professor)
    db.session.commit()
    return professor.to_dict()