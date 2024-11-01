import mysql.connector

# Creating Local Variable
__cnx = None

# Defining SQL Connection
def get_sql_connection():
    
    # Making the local variable Global
    global __cnx
    if __cnx is None:

    # Creating Database Connection
        __cnx = mysql.connector.connect(user='root',password='root',
                                host='127.0.0.1',
                                database='cs')
    return __cnx