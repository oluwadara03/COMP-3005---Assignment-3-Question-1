import psycopg2

# Function to connect to the Student database
def establish_db_connection():
    # Connects to the database using provided credentials
    connection = psycopg2.connect("dbname=Students user=postgres password=postgres")
    return connection

# Function to add a new student to the Student database
def addStudent(first_name, last_name, email, enrollment_date):
    # Connects to the database
    db_connection = establish_db_connection()
    # Creates a cursor for queries
    cursor = db_connection.cursor()
    # Inserts a new student record with provided details
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    # Saves changes in the database
    db_connection.commit()
    # Closes the connection
    db_connection.close()

# Function to update a student's email address
def updateStudentEmail(student_id, new_email):
    # Connects to the database
    db_connection = establish_db_connection()
    # Creates a cursor for queries
    cursor = db_connection.cursor()
    # Updates the email address of a specific student
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    # Commits the changes
    db_connection.commit()
    # Closes the connection
    db_connection.close()

# Function to retrieve all students from the Student database
def getAllStudents():
    # Connects to the database
    db_connection = establish_db_connection()
    # Creates a cursor to execute SQL queries
    cursor = db_connection.cursor()
    # Fetches all student records
    cursor.execute("SELECT * FROM students")
    # Retrieves all student data
    rows = cursor.fetchall()
    # Displays each student's information
    for row in rows:
        print(row)
    # Closes the database connection
    db_connection.close()

# Function to remove a student from the database
def deleteStudent(student_id):
    # Connects to the database
    db_connection = establish_db_connection()
    # Creates a cursor for queries
    cursor = db_connection.cursor()
    # Deletes a specific student record from the 'students' table - note that student_id is a tuple in this case
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    # Commits the deletion
    db_connection.commit()
    # Closes the connection
    db_connection.close()

# Examples of function usages
getAllStudents()

