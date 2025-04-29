from flask_restx import Namespace, Resource, fields
from professores.professores_model import getTodosProfessores, criarProfessor, getPorIdProfessor, attProfessor, deletarProfessor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("professor", {
    "id": fields.Integer(required=True, description="ID professor"),
    "nome": fields.String(required=False, description="Nome do professor"),
    "idade": fields.Integer(required=False, description="Idade do professor"),
    "materia": fields.String(required=False, description="Matéria ministrada pelo professor"),
    "observacoes": fields.String(required=True, description="Observações sobre o professor"),
})

professor_output_model = professores_ns.model("professorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@professores_ns.route("/")
class professoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        return getTodosProfessores()

    @professores_ns.expect(professor_model)
    def post(self):
        data = professores_ns.payload
        response, status_code = criarProfessor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class professorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        return getPorIdProfessor(id_professor)

    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        data = professores_ns.payload
        attProfessor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        deletarProfessor(id_professor)
        return {"message": "professor excluído com sucesso"}, 200