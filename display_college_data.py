import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('campusmate.db')
cursor = conn.cursor()

# Function to display all college details from the database
def display_colleges():
    cursor.execute("SELECT * FROM colleges")  # Retrieve all rows from the colleges table
    rows = cursor.fetchall()  # Fetch all records

    # Check if the table is empty
    if not rows:
        print("No data found.")
    else:
        for row in rows:
            print(f"Sl.No: {row[0]}")
            print(f"College Name: {row[1]}")
            print(f"Location: {row[2]}")
            print(f"Type: {row[3]}")
            print(f"UG Courses: {row[4]}")
            print(f"PG Courses: {row[5]}")
            print(f"Specialization: {row[6]}")
            print(f"Research: {row[7]}")
            print(f"University: {row[8]}")
            print(f"Accreditation: {row[9]}")
            print(f"Placement Support: {row[10]}")
            print(f"Website: {row[11]}")
            print(f"Activities: {row[12]}")
            print("-" * 50)  # Separator between each college entry

# Call the function to display all college data
display_colleges()

# Close the connection after displaying the data
conn.close()
