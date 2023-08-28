from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos


#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicializar el objeto SQLalchemy
db = SQLAlchemy(app)
migrate = Migrate(app , db )

#registrar modulos(blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)


from .models import Cliente,Venta, Producto, Detalle



