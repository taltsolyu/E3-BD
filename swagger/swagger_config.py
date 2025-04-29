from . import api
from swagger.namespaces.professor_namespace import professores_ns

def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(professores_ns, path="/professores")
    api.mask_swagger = False