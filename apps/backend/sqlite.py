# import sqlite3
# import pandas as pd

# # Load the Excel file
# df = pd.read_excel('All_Flight_Data_Final.xlsx')

# # Convert date and time fields to string format
# df['date'] = df['date'].astype(str)
# df['departure_time'] = df['departure_time'].astype(str)
# df['arrival_time'] = df['arrival_time'].astype(str)

# # Connect to SQLite database (or create it if it doesn't exist)
# connection = sqlite3.connect("flight_data.db")

# # Create a cursor object to interact with the database
# cursor = connection.cursor()

# # Create the table for flight data
# table_info = """
# CREATE TABLE IF NOT EXISTS flights (
#     flight_name TEXT,
#     date TEXT,
#     departure_time TEXT,
#     departure_loc TEXT,
#     flight_duration TEXT,
#     stops TEXT,
#     arrival_time TEXT,
#     arrival_loc TEXT,
#     price INTEGER
# )
# """
# cursor.execute(table_info)

# # Insert the records from the dataframe into the SQLite table
# for row in df.itertuples(index=False):
#     cursor.execute('''
#         INSERT INTO flights (flight_name, date, departure_time, departure_loc, flight_duration, stops, arrival_time, arrival_loc, price)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#     ''', row)

# # Display all the records
# print("The inserted records are:")
# data = cursor.execute('''SELECT * FROM flights''')
# for row in data:
#     print(row)

# # Commit your changes and close the connection
# connection.commit()
# connection.close()
# import sqlite3
# import json

# # Connect to SQLite database (or create it if it doesn't exist)
# db_file = "new.db"
# connection = sqlite3.connect(db_file)

# try:
#     # Create a cursor object to interact with the database
#     cursor = connection.cursor()

#     # Create the Professionals table
#     create_professionals_table_query = """
#     CREATE TABLE IF NOT EXISTS Professionals (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         type TEXT,
#         org_or_prac_id TEXT,
#         username_or_business_url TEXT,
#         name TEXT,
#         ranking INTEGER,
#         photo TEXT,
#         category TEXT,
#         sub_category TEXT,
#         rating REAL,
#         total_appointment INTEGER,
#         zone TEXT,
#         branch TEXT,
#         area_of_practice TEXT
#     )
#     """
#     cursor.execute(create_professionals_table_query)

#     # Insert data into the Professionals table
#     professionals_data = {
#         "_Id": None,  # Auto-increment ID
#         "Type": "Organization",
#         "Org or Prac id": "1234567",
#         "username or business url": "user1",
#         "Name": "Hospital 1",
#         "Ranking": 10,
#         "Photo": "url",
#         "Category": "Healthcare",
#         "Sub-category": json.dumps(["Medicine", "Eye"]),  # Store as JSON string
#         "Rating": 4.7,
#         "Total Appointment": 1000,
#         "Zone": json.dumps(["Cal", "Nev", "NY"]),  # Store as JSON string
#         "Branch": json.dumps(["branch 1", "Branch 2"]),  # Store as JSON string
#         "Area of Practice": "local"
#     }

#     insert_professionals_query = """
#     INSERT INTO Professionals (
#         type, org_or_prac_id, username_or_business_url, name, ranking,
#         photo, category, sub_category, rating, total_appointment,
#         zone, branch, area_of_practice
#     )
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """
#     cursor.execute(insert_professionals_query, (
#         professionals_data["Type"],
#         professionals_data["Org or Prac id"],
#         professionals_data["username or business url"],
#         professionals_data["Name"],
#         professionals_data["Ranking"],
#         professionals_data["Photo"],
#         professionals_data["Category"],
#         professionals_data["Sub-category"],
#         professionals_data["Rating"],
#         professionals_data["Total Appointment"],
#         professionals_data["Zone"],
#         professionals_data["Branch"],
#         professionals_data["Area of Practice"]
#     ))

#     # Commit changes
#     connection.commit()

#     # Display all records in the Professionals table
#     print("The inserted records in the Professionals table are:")
#     for row in cursor.execute('SELECT * FROM Professionals'):
#         print(row)

# except Exception as e:
#     print(f"An error occurred: {e}")
#     connection.rollback()  # Rollback changes if an error occurs

# finally:
#     # Close the connection
#     connection.close()
#     print(f"Database connection to '{db_file}' closed.")
import sqlite3
import json

# Connect to SQLite database (or create it if it doesn't exist)
db_file = "new.db"
connection = sqlite3.connect(db_file)

try:
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Sample data to insert into the Professionals table
    professionals_data = [
        {
            "_Id": None,
            "Type": "Organization",
            "Org or Prac id": "1234567",
            "username_or_business_url": "user1",
            "Name": "Hospital 1",
            "Ranking": 10,
            "Photo": "url1",
            "Category": "Healthcare",
            "Sub-category": json.dumps(["Medicine", "Eye"]),
            "Rating": 4.7,
            "Total Appointment": 1000,
            "Zone": json.dumps(["Cal", "Nev", "NY"]),
            "Branch": json.dumps(["branch 1", "Branch 2"]),
            "Area of Practice": "local"
        },
        {
            "_Id": None,
            "Type": "Practitioner",
            "Org or Prac id": "1234565",
            "username_or_business_url": "user2",
            "Name": "Clinic Alpha",
            "Ranking": 11,
            "Photo": "url2",
            "Category": "Doctor",
            "Sub-category": json.dumps(["Cardiology", "Eye"]),
            "Rating": 4.8,
            "Total Appointment": 10000,
            "Zone": json.dumps(["Dhaka", "sylhet"]),
            "Branch": json.dumps(["Uttara", "Akhalia"]),
            "Area of Practice": "local"
        },
        {
            "_Id": None,
            "Type": "Organization",
            "Org or Prac id": "3456789",
            "username_or_business_url": "user3",
            "Name": "Dental Center Pro",
            "Ranking": 9,
            "Photo": "url3",
            "Category": "Dental",
            "Sub-category": json.dumps(["Orthodontics", "Surgery"]),
            "Rating": 4.6,
            "Total Appointment": 800,
            "Zone": json.dumps(["Boston", "NY"]),
            "Branch": json.dumps(["Dental Branch 1"]),
            "Area of Practice": "suburban"
        }
    ]

    # Insert data into the Professionals table
    insert_professionals_query = """
    INSERT INTO Professionals (
        type, org_or_prac_id, username_or_business_url, name, ranking,
        photo, category, sub_category, rating, total_appointment,
        zone, branch, area_of_practice
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    for professional in professionals_data:
        cursor.execute(insert_professionals_query, (
            professional["Type"],
            professional["Org or Prac id"],
            professional["username_or_business_url"],
            professional["Name"],
            professional["Ranking"],
            professional["Photo"],
            professional["Category"],
            professional["Sub-category"],
            professional["Rating"],
            professional["Total Appointment"],
            professional["Zone"],
            professional["Branch"],
            professional["Area of Practice"]
        ))

    # Commit changes
    connection.commit()

    # Display all records in the Professionals table
    print("The inserted records in the Professionals table are:")
    for row in cursor.execute('SELECT * FROM Professionals'):
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
    connection.rollback()  # Rollback changes if an error occurs

finally:
    # Close the connection
    connection.close()
    print(f"Database connection to '{db_file}' closed.")
