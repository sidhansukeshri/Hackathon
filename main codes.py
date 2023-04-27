# main codes for admin 
import mysql.connector
from prettytable import PrettyTable

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Spysiddhu@#2004"
)

mycursor = mydb.cursor()
mycursor.execute("USE phone_specifications")

# Function to display all data
def display_data():
    mycursor.execute("SELECT * FROM specifications")
    rows = mycursor.fetchall()
    if rows:
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        for row in rows:
            x.add_row(row)
        print(x)
    else:
        print("No data available.")

# Function to add data
def add_data():
    model_name = input("Enter model name: ")
    os = input("Enter OS: ")
    memory = input("Enter memory: ")
    battery = input("Enter battery: ")
    price = input("Enter price: ")
    camera = input("Enter camera: ")
    review = input("Enter review: ")
    sql = "INSERT INTO specifications (Model_Name, OS, Memory, Battery, Price, Camera, Review) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (model_name, os, memory, battery, price, camera, review)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Function to delete data
def delete_data():
    model_name = input("Enter model name: ")
    sql = "DELETE FROM specifications WHERE Model_Name = %s"
    val = (model_name,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted.")

def modify_data():
  model_name = input("Enter model name to modify: ")
  field_name = input("Enter field name to modify (OS, Memory, Battery, Price, Camera, Review): ")
  new_value = input("Enter new value: ")
  sql = f"UPDATE specifications SET {field_name} = %s WHERE Model_Name = %s"
  val = (new_value, model_name)
  mycursor.execute(sql, val)
  mydb.commit()
  print("Data modified successfully.")


display_data()
while True:
  print("1. ADD PHONE")
  print("2. DELETE PHONE")
  print("3. MODIFY PHONE SPECIFICATIONS")
  print("4. EXIT")

  choice = input("Enter your choice (1-4): ")
  if choice == "1":
      add_data()
      break
  elif choice == "2":
      delete_data()
      break
  elif choice == "3":
      modify_data()
      break
  elif choice == "4":
      break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")

display_data()





















#main codes for phone_specifications
import mysql.connector
from prettytable import PrettyTable

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Spysiddhu@#2004"
)

"""# Create database if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS phone_specifications")
mycursor.execute("USE phone_specifications")

# Create table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS specifications (Model_Name VARCHAR(255)UNIQUE, OS VARCHAR(255), Memory VARCHAR(255), Battery VARCHAR(255), Price VARCHAR(255), Camera VARCHAR(255), Review VARCHAR(255))")

# Insert sample data into the table
# Insert sample data into the table
sql = "INSERT INTO specifications (Model_Name, OS, Memory, Battery, Price, Camera, Review) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("Samsung Galaxy S23 5G", "Android 13", "128GB", "3900 mAh", "80,000", "50MP", "3"), ("OnePlus Nord", "Android Q10", "64GB", "4115 mAh", "20,000", "48MP", "5"), ("OPPO A78 5G", "Android", "128GB", "5000 mAh", "20,000", "13MP", "3"), ("Vivo V27 Pro 5G", "Android 13", "256GB", "4600 mAh", "46,000", "50MP", "4"), ("Apple iPhone 14 Pro", "iOS 16", "128GB", "3200 mAh", "1,20,000", "48MP", "3")]
mycursor.executemany(sql, val)
mydb.commit()

mydb.commit()
"""
mycursor = mydb.cursor()
mycursor.execute("USE phone_specifications")

def display_data():
    mycursor.execute("SELECT * FROM specifications")
    rows = mycursor.fetchall()
    if rows:
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        for row in rows:
            x.add_row(row)
        print(x)
    else:
        print("No data available.")


class PhoneSpecifications:
  
        
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Spysiddhu@#2004",
      database="phone_specifications"
    )
    self.mycursor = self.mydb.cursor()

  def search(self):
    column = input("Enter the column to search (Model_Name, OS, Memory, Battery, Price, Camera, Review): ")
    value = input("Enter the value to search: ")
    sql = f"SELECT * FROM specifications WHERE {column}=%s"
    val = (value,)
    self.mycursor.execute(sql, val)
    results = self.mycursor.fetchall()
    if results:
      table = PrettyTable()
      table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
      for result in results:
        table.add_row(result)
      print(table)
    else:
      print("No results found.")
 

  def review(self):
    value = input("Enter the model name: ")
    sql = "SELECT review FROM specifications WHERE Model_Name=%s"
    val = (value,)
    self.mycursor.execute(sql, val)
    current_review = self.mycursor.fetchone()[0] # fetch the current review
    new_review = input("Enter your review: ")
    new_review_avg = (float(current_review) + float(new_review)) / 2 # calculate new average
    sql2 = "UPDATE specifications SET Review=%s WHERE Model_Name=%s"
    val2 = (new_review_avg, value)
    self.mycursor.execute(sql2, val2)
    self.mydb.commit()
    print(self.mycursor.rowcount, "record(s) updated.")

    
    


  def compare(self):
    a=input("Enter number of phone to compare : ")
    if a== "1":
        value = input("Enter the model name: ")
        sql = f"SELECT * FROM specifications WHERE Model_name=%s"
        val = (value,)
        self.mycursor.execute(sql, val)
        results = self.mycursor.fetchall()
        if results:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
    elif a == "2":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()
    
        if results1 and results2:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
            
    elif a == "3":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()
    
        if results1 and results2 and results3:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
        

    elif a == "4":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()

        value4 = input("Enter the fourth model name: ")
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)
        results4 = self.mycursor.fetchall()
        
        if results1 and results2 and results3 and results4:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            for result in results4:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")

    elif a == "5":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()

        value4 = input("Enter the fourth model name: ")
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)
        results4 = self.mycursor.fetchall()
        
        value5 = input("Enter the fourth model name: ")
        sql5 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val5 = (value5,)
        self.mycursor.execute(sql5, val5)
        results5 = self.mycursor.fetchall()
        
        if results1 and results2 and results3 and results4 and results5:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            for result in results4:
                table.add_row(result)
            for result in results5:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")

phone_specs = PhoneSpecifications()
display_data()
while True:
  print("1. COMPARE PHONES")
  print("2. SEARCH PHONE SPECIFICATIONS")
  print("3. REVIEW")
  print("4. EXIT")

  choice = input("Enter your choice (1-3): ")
  if choice == "1":
      phone_specs.compare()
  elif choice == "2":
    phone_specs.search()
  elif choice == "3":
    phone_specs.review()
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 3.")


display_data()


