import os

from alunos.alunos_rotas import alunos_blueprint
from config import app, db
from professores.professores_model import Professor
from professores.professores_routes import professores_bp
from turmas.turmas_routes import turmas_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(turmas_blueprint)
app.register_blueprint(professores_bp)

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
  