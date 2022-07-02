# importing required libraries
import mysql.connector
  
# dataBase = mysql.connector.connect(
#   host ="localhost",
#   user ="root",
#   passwd =""
# )
 
# print(dataBase)

# cursorObject = dataBase.cursor()
 
# # creating database
# cursorObject.execute("CREATE DATABASE gfg")

# # Disconnecting from the server
# dataBase.close()

  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "gfg"
)

cursorObject = dataBase.cursor()
  
print("creating table")

studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL
                   )"""
  
print("table created")

#cursorObject.execute(studentRecord)
  
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL)\
VALUES (%s, %s, %s)"
val = ("Ram", "CSE", "85")
   
cursorObject.execute(sql, val)
dataBase.commit()
   
dataBase.close()

#https://www.geeksforgeeks.org/python-mysql/