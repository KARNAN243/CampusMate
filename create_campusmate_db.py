import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("campusmate.db")
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS colleges (
    sl_no INTEGER PRIMARY KEY AUTOINCREMENT,
    college_name TEXT NOT NULL,
    location TEXT,
    college_type TEXT,
    ug_courses TEXT,
    pg_courses TEXT,
    specialization TEXT,
    research TEXT,
    university TEXT,
    accreditation TEXT,
    placement_support TEXT,
    website TEXT,
    activities TEXT
)
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")
