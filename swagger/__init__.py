from flask_restx import Api

api = Api(
    version="1.0",
    title="API de Gestão Escolar",
    description="Documentação da API para Professores",
    doc="/docs",
    mask_swagger=False, 
    prefix="/api"
)
