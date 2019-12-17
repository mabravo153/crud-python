import db_connect
import mysql.connector


class User: 

    def __init__(self, id_usuario = None,nombre_usuario  = None, apellido_usuario  = None, numero_telefono = None):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = nombre_usuario
        self.__apellido_usuario = apellido_usuario
        self.__numero_telefono = numero_telefono

    def create_user(self):
        """metodo para crear usuario """           
        db_con = db_connect.Conector() 
        conexion = db_con.conect_db() #esto nos retorna el cursor(la variable a ejecutar)

        sql = "INSERT INTO users(id_user, nombre_usuario, apellido_usuario, telefono) VALUES(%s,%s,%s,%s) "
        val = (self.__id_usuario, self.__nombre_usuario, self.__apellido_usuario, self.__numero_telefono)

        conexion.execute(sql,val)

        db_con.base_datos.commit()
        conexion.close()
        db_con.base_datos.close()

    def list_all(self):
        """este metodo nos retorna todos los usuario"""
        con_db = db_connect.Conector()
        list_db = con_db.conect_db()

        sql = f"SELECT * FROM users"
        list_db.execute(sql)

        return list_db.fetchall()

    def list_one(self, id_user=0):
        """este metodo nos retorna el usuario seleccionado"""
        con_db = db_connect.Conector()
        list_db = con_db.conect_db()

        sql = f"SELECT * FROM users WHERE id_user= '{id_user}'"
        list_db.execute(sql)

        return list_db.fetchall()

    def update_user(self, id_user=0):
        """metodo para actualizar el usuario que sea pasado"""
        update = db_connect.Conector()
        update_cursor = update.conect_db()

        sql = f"UPDATE users SET nombre_usuario=%s,apellido_usuario=%s, telefono=%s WHERE id_user={id_user}"
        val = (self.__nombre_usuario, self.__apellido_usuario, self.__numero_telefono)

        update_cursor.execute(sql,val)

        update.base_datos.commit()

        update_cursor.close()
        update.base_datos.close()

    def del_user(self, id_user= 0):
        delete = db_connect.Conector()
        cursor_delete = delete.conect_db()

        listado_usuario = self.list_one(id_user)
        sql = f"DELETE FROM users WHERE id_user={id_user}"

        if len(listado_usuario) > 0:
            cursor_delete.execute(sql)
            delete.base_datos.commit()
            cursor_delete.close()
            delete.base_datos.close()

            return 200

        else:
            return 404
