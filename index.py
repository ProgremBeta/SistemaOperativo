from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from Src.Servidor.BaseDatos import db
from Src.Main import main
from Src.config import Desarrollo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:123456@localhost/LoginRegistro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Desarrollo)

app.register_blueprint(main)

db.init_app(app)

with app.app_context():
	db.create_all()

if __name__ == '__main__':
	app.run()