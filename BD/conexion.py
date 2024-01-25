# How create the conecct to database this is the first step
import mysql.connector
from mysql.connector import Error 

class DAO():
    
    def __init__(self):
        try:
            self.conection=mysql.connector.connect(
                host="localhost",
                port=3306
                user="root"
                password="202188"
                db="course"        
            )
        except Error as ex:
            print("Error in conection with db")
            

    