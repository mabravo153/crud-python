import mysql.connector
from mysql.connector import Error 


class Conector:
    
    __hostname='localhost'
    __database = 'prueba_db'
    __user='mabravo153'
    __password='Barranquilla1.'
    
    base_datos = mysql.connector.connect(
            host= __hostname,
            user=__user,
            passwd=__password,
            database=__database
        )

    """Metodo para crear conexion y una base de datos """
    def create_db(self,nombre):

        try: 
            base_datos = mysql.connector.connect(
                host= self.__hostname,
                user=self.__user,
                passwd=self.__password
            )  

            cursor = base_datos.cursor()

            cursor.execute(f"CREATE DATABASE {nombre}")

            print(f'La base de datos {nombre} se creo correctamente')
            
        except Error as error:
            print(f'Ocurrio un error {error}')
        
        finally:
            cursor.close()
            base_datos.close()


    def conect_db(self):
        """ esta funcion me permite conectarme a la base de datos 
        y retornar el cursor para ejecutarlo."""
        self.base_datos 

        mycursor = self.base_datos.cursor()

        return mycursor

