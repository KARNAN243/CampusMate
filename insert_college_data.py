import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('campusmate.db')
cursor = conn.cursor()

# Create table with appropriate fields
cursor.execute('''
CREATE TABLE IF NOT EXISTS colleges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_name TEXT,
    location TEXT,
    college_type TEXT,
    ug_courses TEXT,
    pg_courses TEXT,
    specialization TEXT,
    research TEXT,
    university TEXT,
    accreditation TEXT,  -- AICTE/UGC/NAAC
    placement_support TEXT,
    website TEXT,
    activities TEXT
);
''')

# Function to insert data from user input for each college
def insert_college_data():
    # Get user input for college details
    college_name = input("Enter College Name: ")
    location = input("Enter Location: ")
    college_type = input("Enter Type of College: ")
    ug_courses = input("Enter UG Courses (comma-separated): ")
    pg_courses = input("Enter PG Courses (comma-separated): ")
    specialization = input("Enter Specialization: ")
    research = input("Enter Research Opportunities: ")
    university = input("Enter University: ")
    accreditation = input("Enter Accreditation (AICTE/UGC/NAAC): ")
    placement_support = input("Enter Placement & Career Support: ")
    website = input("Enter Website URL: ")
    activities = input("Enter Activities (comma-separated): ")

    # Insert data into the database
    cursor.execute('''
    INSERT INTO colleges (college_name, location, college_type, ug_courses, pg_courses, specialization,
                          research, university, accreditation, placement_support, website, activities)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (college_name, location, college_type, ug_courses, pg_courses, specialization,
          research, university, accreditation, placement_support, website, activities))

    # Commit the changes
    conn.commit()
    print("College data inserted successfully.")

# Function to insert data for multiple colleges
def insert_multiple_colleges():
    for _ in range(34):  # Loop to input data for 34 colleges
        print(f"\nEntering details for College {_ + 1}...")
        insert_college_data()

# Start the process
insert_multiple_colleges()

# Close the connection after inserting all data
conn.close()
