# How create the conecct to database this is the first step
import mysql.connector
from mysql.connector import Error 

class DAO():
    
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root", 
                password="202188",
                db="university"       
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))            
# Second step, create method to view all courses


    def showCourses(self): 
         if self.conexion.is_connected():  
            try:
                 cursor = self.conexion.cursor()
                 cursor.execute("SELECT * FROM courses ORDER BY name ASC")
                 result=cursor.fetchall()
                 return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))