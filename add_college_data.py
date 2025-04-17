import sqlite3

# Connect to your CampusMate database
conn = sqlite3.connect("campusmate.db")
cursor = conn.cursor()

# Add the 35th college
cursor.execute('''
    INSERT INTO colleges (
        sl_no, college_name, location, type_of_college,
        ug_courses, pg_courses, specialization, research,
        university, accreditation, placement_career_support,
        website, activities
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    35,
    "College of Applied Science, Karthikappally",
    "Karthikappally,Haripad, Alappuzha, Kerala",
    "Arts & Science (IHRD)",
    "B.Sc (Computer Science), B.Com (Co-operation), B.Com (Logistics and Supply Chain Management), BBA, BCA",
    "M.Com (Finance)",
    "Computer Science, Electronics, Commerce, Management, Software Development, Embedded Systems, Communication Systems, Data Science, Artificial Intelligence, Network Security, Internet of Things (IoT)",
    "Computer Science, Electronics, Commerce, Management, Software Development, Embedded Systems, Communication Systems, Data Science, Artificial Intelligence, Network Security, Internet of Things (IoT)",
    "University of Kerala",
    "NIL",
    "Placement Cell, Career Guidance, Training Programs, Soft Skill Development, Resume Preparation Assistance, Mock Interviews, Industrial Visits, Higher Studies Support, Alumni Network Support, Placement Drives, Internship Assistance.",
    "https://caskarthikapally.ihrd.ac.in/",
    "NSS, Women Cell, Arts Club, Sports Club, Tourism Club, Bhoomitrasena Club, Anti Narcotic Club, Science Forum, Nature Club, Career Guidance and Placement Cell"
))

conn.commit()
conn.close()
