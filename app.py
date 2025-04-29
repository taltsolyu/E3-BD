from swagger.swagger_config import configure_swagger
import pytest
import os
import sys
from config import app, db
from professores.professores_routes import professores_bp

app.register_blueprint(professores_bp, url_prefix='/api')

configure_swagger(app)

with app.app_context():
    db.create_all()

def run_tests():
    os.environ['FLASK_ENV'] = 'testing'
    result = pytest.main(['--maxfail=1', '--disable-warnings', '--tb=short'])
    return result

if __name__ == '__main__':
    
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
  