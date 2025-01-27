import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="College@kali90",
    database="musharraf"
)

# Prompt the user for start and end dates
start_date = input("Enter the start date (MM/DD/YY): ")
end_date = input("Enter the end date (MM/DD/YY): ")

# Convert user input dates to MySQL DATE format
start_date = datetime.datetime.strptime(start_date, "%m/%d/%y").date()
end_date = datetime.datetime.strptime(end_date, "%m/%d/%y").date()

# Execute the query with user-provided dates
cursor = conn.cursor()
query = ("SELECT CONCAT(ename, ', ', job) AS Employees, hiredate "
         "FROM emp "
         "WHERE hiredate BETWEEN %s AND %s")
cursor.execute(query, (start_date, end_date))

# Fetch and display the results
for (employees, hiredate) in cursor:
    print(f"Employee: {employees}, Hire Date: {hiredate}")

# Close cursor and connection
cursor.close()
conn.close()
