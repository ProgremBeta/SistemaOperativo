from Src.Servidor.BaseDatos import db

class Usuarios(db.Model):
	__tablename__ = 'Usuarios'
	
	id = db.Column(db.INT, primary_key=True)
	nombre = db.Column(db.String(50))
	apellido = db.Column(db.String(50))

	def __init__(self, id, nombre, apellido):
		self.id = id
		self.nombre = nombre
		self.apellido = apellido