import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Usuario
"""
import sys
sys.path
sys.path.append('/FruverHouseBack/modelo/usuarios.py')
"""
class UsuariosDao(dao):
    """
    docstring
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[usuario.username,usuario.contraseña]
            cursor.callproc("crearUsuario",args)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
    def consultar(self,username,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select from usuarios where username='"+username+"' and contraseña=sha('"+password+"');"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                username=row[0]
                contraseña=row[1]
                usuario=Usuario(username,contraseña)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None