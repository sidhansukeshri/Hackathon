import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spysiddhu@#2004",
    database="scrap"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Prompt the user for input
search_value = input("Enter the search value: ")

# Ask the user what information they want to search for
while True:
    search_choice = input(""""What information do you want to search for?
enter
'1' for ID,
'2' for address,
'3' for ID and address
'4' for to show everthing
what is your choice : """)
    if search_choice == '1':
        sql_query = "SELECT id FROM customers WHERE name = %s"
        break
    elif search_choice == '2':
        sql_query = "SELECT address FROM customers WHERE name = %s"
        break
    elif search_choice == '3':
        sql_query = "SELECT id, address FROM customers WHERE name = %s"
        break
    elif search_choice == '4':
        sql_query = "SELECT * FROM customers WHERE name = %s"
        break
    else:
        print("Invalid choice. Please enter '1', '2', '3' or '4'.")

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
