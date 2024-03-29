import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your password"; #your password 
  database="scrap"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Prompt the user for input
search_value = input("Enter the search value: ")

# Define the SQL query
sql_query = "SELECT * FROM customers WHERE name = %s"

# Define the parameter(s) for the query
query_param = (search_value,)

# Execute the query with the parameter(s)
mycursor.execute(sql_query, query_param)

# Fetch all the matching rows
results = mycursor.fetchall()

# Print the results
if len(results) > 0:
  for row in results:
    print(row)
else:
  print("No results found.")
