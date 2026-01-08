# this file handles everything related to MySQL database
# Connects to the database using credentials from config.py

import mysql.connector
from config import HOST, USER, PASSWORD
from datetime import date


class DbConnectionError(Exception):
    pass

#Function to connect to the database

def connect_to_db(database_name="pet_adoption_db"):
    connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = database_name
    )
    return connection

#function to fetch and print all the data

def get_all_pets():
    db_name = "pet_adoption_db"
    try:
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()   #cursor is a pointer or messenger between your Python code and the database that lets you to execute SQL statements and retrieve results
        print(f"connected to DB:{db_name}")

        query = "SELECT * FROM pets"
        cursor.execute(query)
        records = cursor.fetchall()

        return records

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#function to add a new pet into the data

def insert_new_pet(record):
    db_name = "pet_adoption_db"
    try:
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f"connected to DB: {db_name}")

        query = """
                INSERT INTO pets (pet_name, species, gender, age, status) 
                VALUES (%s, %s, %s, %s, %s)
            """
        values = (
            record['pet_name'],
            record['species'],
            record['gender'],
            record['age'],
            record['status']
        )
        cursor.execute(query,values)

        db_connection.commit()

        print(f"Inserted new pet record: {record['pet_name']}")

    except Exception:
        raise DbConnectionError("Failed to insert pet into DB")
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# #check add new pet function
# record = {
#     'pet_name':'Simbuuudii',
#     'species':'Golden Retriever',
#     'gender':'male',
#     'age':8,
#     'status':'adopted'
# }

# insert_new_pet(record)

#function to adopt a pet

def adopt_pet(pet_id, user_id):
    """Adopt a pet and mark the pet as adopted."""
    db_name = "pet_adoption_db"
    try:
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()

        insert_query = """
            INSERT INTO adoptions (pet_id, user_id, adoption_date, return_status)
            VALUES (%s, %s, %s, %s)
        """
        values = (
            pet_id,
            user_id,
            date.today(),
            'not returned'
        )
        
        cursor.execute(insert_query, values)

        # to update pet status to adopted
        update_query = "UPDATE pets SET status = 'adopted' WHERE id = %s"
        cursor.execute(update_query, (pet_id,))

        db_connection.commit()
        print(f"Pet_id {pet_id} adopted by User_id {user_id}")

    except Exception:
        raise DbConnectionError(f"Failed to adopt pet")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed.")

# # check adopt_pet function
# adopt_pet(pet_id=2, user_id=4)

#funtction to return  a pet and log the rreason for return
def return_pet(adoption_id, reason):
    """ Marks the pet as return and logs the reason for return
    """
    db_name ="pet_adoption_db"

    try:
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()

        return_query = """
                INSERT INTO returns (adoption_id, return_date, reason) 
                VALUES (%s, %s, %s)
            """
        values=(
            adoption_id,
            date.today(),
            reason
        )
        cursor.execute(return_query, values)

        #CALL stored procedure mark_pet_returned
        cursor.execute("CALL mark_pet_returned(%s)", (adoption_id,))

        db_connection.commit()
        print(f"Pet with adoption id {adoption_id} marked as returned")

    except Exception:
        raise DbConnectionError("Failed to return pet")
    
    finally:
        if db_connection:
            db_connection.close()

# #checking  the return function
# return_pet(adoption_id=5, reason="Pet was sad")

