#the third step
from BD.conexion import DAO
import functions
def mainMenu():
    Continue=True
    while(Continue):
        rightChoice = False
        while(not rightChoice):
            print("==================== Main Menu ====================")
            print("1.- Show courses")
            print("2.- Add courses")
            print("3.- Update courses")
            print("4.- Delete courses")
            print("5.- Exit")
            print("========================================================")
            option = int(input("Choose a option: "))
            
            if option < 1 or option > 5:
                print("Incorrect option repeat again")
            elif option == 5:
                Continue = False
                print("Thanks for use this system")
                break
            else:
                rightChoice = True
                executeOption(option)
     
            
            
            
                
def executeOption(option):
    dao = DAO()
   
    if option == 1:
        try:
            courses = dao.listCourses()  
            if len(courses) > 0:
               functions.listCourses(courses)
            else:
                print("Courses empty.....")  
        except:
            print("an error has occurred!")
    
    elif option == 2:
        print("REGISTER COURSES")
        
    elif option == 3:
        print(" UPDATE COURSES")
        
    elif option == 4:
        print("DELETE COURSES")
    else:
        print("this option is not correct: ")
    
mainMenu()
    