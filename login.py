#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.UsuariosDao import UsuariosDao
from dao.models import Usuario
import cgi

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()
username=datos.getvalue('username')
contraseña =datos.getvalue('contraseña')

dao=UsuariosDao()
usuario = dao.consultar(username,contraseña)
if(usuario is not None):
    print('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.username+'"}')
else:
    print('{"tipo":"error","mensaje":"Usuario o contrasena invlidos"}')