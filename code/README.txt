Step 1: Open a terminal and pyscopg2 using the following command in your terminal: "pip install psycopg2". Psycopg is the most popular PostgreSQL database adapter for the Python programming language, and it allows you to preform queries in PostgreSQL (more specifically in pgAdmin4).

Step 2: Download the code folder that contains the students.py and students.sql files. These are the only two files needed to run the program.

Step 3: Open pgAdmin 4 and login. Then, create a database called "Students" in pgAdmin4. 

Step 4: After creating the database, right click on the Students database and go to Query Tools. Click on the folder icon (under the Students/postgres@PostgreSQL 16 line, or just right beside the save button) and import the SQL file. Then run the Query to create and populate the table.

Step 5: Locate the downloaded folder. Review the code (in a text editor of your choice) and make sure that the username, password, and database name located in the code (Line 6 or so) match the specifications of your pgAdmin4 database username and password.

Step 6: Open a terminal. Once you have moved into the correct folder, execute in your terminal: "python students.py". Right now, nothing will output because the function calls are commented out. Go back to the code and uncomment any function you want to test, and feel free to change any of the testing values.

Step 7: Save the code and go back to the terminal to try to run the code again using "python students.py. If there are no errors, you have successfully tested this code.
