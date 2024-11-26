class Desarrollo():
	DEBUG = True

	MYSQL_HOST = 'localhost'
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = '123456'
	MYSQL_DB = 'LoginRegistro'
	MYSQL_PORT = '3600'
	MYSQL_UNIX_SOCKET = '/var/run/mysqld/mysqld.sock'
	MYSQL_CONNECT_TIMEOUT = 30
	MYSQL_READ_DEFAULT_FILE = '/etc/mysql/my.cnf'
	MYSQL_USE_UNICODE = True
	MYSQL_CHARSET = 'utf8mb4'


config ={
	'desarrollo': Desarrollo
}