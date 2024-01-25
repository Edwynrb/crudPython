# How create the conecct to database this is the first step
import mysql.connector
from mysql.connector import Error 

class DAO():
    
    def __init__(self):
        try:
            self.conection=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root", 
                password="202188",
                db="university"       
            )
        except Error as ex:
            print("Error in conection with db")
            
# Second step, create method to view all courses

def viewsCourses(self):
    if self.conection.is_connected():
       try:
           cursor=self.conection.cursor()
           cursor.execute("SELECT * FROM courses ORDER BY name ASC")
           result=cursor.fetchall()
           return result
       except Error as ex:
           print("Error in connection with db")
    