import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect()

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()

    def execute_query(self, sql_query, query_params):
        self.cursor.execute(sql_query, query_params)
        return self.cursor.fetchall()

class Customer:
    def __init__(self, db):
        self.db = db

    def search_customers(self):
        # Prompt the user for input
        search_value = input("Enter the search value: ")

        # Ask the user what information they want to search for
        while True:
            search_choice = input("""What information do you want to search for?
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
        query_params = (search_value,)

        # Execute the query with the parameter(s)
        results = self.db.execute_query(sql_query, query_params)

        # Print the results
        if len(results) > 0:
            for row in results:
                print(row)
        else:
            print("No results found.")

# Create an instance of the Database class
db = Database("localhost", "root", "Spysiddhu@#2004", "scrap")

# Create an instance of the Customer class and search for customers
customer = Customer(db)
customer.search_customers()
