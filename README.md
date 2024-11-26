para ejecutar el programa, entra en un entorno virtual y descarga los requerimiento.

para la instalacion de los requerimiento puedes instalarlos usando

  python -m pip install -r Requirementos.txt


en caso de que no instale todos los paquetes puedes hacerlo manual desde la consola te muestra los paquetes faltantes.

y simplemente ejecutas el programa con


  python3 index.py


seguramente a la hora de ejecutar el programa te muestre un error con my sql
este problema se debe a la base de dato, esto se puede configurar en el archivo:


  index.py


en mi caso yo uso mariadb que se puede hacer de la misma forma que mysql.

en el archivo index.py, cambia lo siguiente:

como esta en la configuracion:


  app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:134679@localhost/Sistemas'


lo que se cambia para su uso:

  

  app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://"usuario de la base de datos":"contraseña de la base de datos"@localhost/"Nombre de la base de datos"'


para que funcione tiene que estar creada la base de datos que se piensa usar y que se remplaza por "Sistemas" o por el nombre de la base de datos.

para crear la base de dato ingresa a la base de datos desde la terminal o tambien se puede usar algun programa para gestionar una base de datos.

una vez dentro de la base de datos, que se deberia ver de la siguiente forma.


  Welcome to the MariaDB monitor.  Commands end with ; or \g.
  Your MariaDB connection id is 3
  Server version: 11.6.2-MariaDB Arch Linux
  
  Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
  
  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
  
  MariaDB [(none)]> 


usa el comando:


  CREATE database "NombreBaseDeDatos";


el ";" es importate a la hora de usar los comando desde una terminal para el manejo o gestion de la base de datos.

para ver todas las bases de datos que hay en el sistema usa el comando:


  SHOW databases;


y para ingresar a ella usa:


  USE "NombreBaseDeDatos";


No hay necesidad de la " " (Solo lo use para hacer la referencia)

una vez creada la base de dato ese nombre es el que cambias en la configuracion en index.py como ya indeque en la linea 25 de este archivo


y los datos o la tabla de los datos se creara si no existe esa tabla, en mi caso yo la llame "Usuarios".
