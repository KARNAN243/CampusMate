from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command', '').lower()

    # 1. General Activation Commands
    if command in ["hey campusmate", "start chatbot", "wake up", "hello campusmate"]:
        return jsonify({"response": "CampusMate activated. How can I help you?"})

    # 2. Navigation Commands
    elif "open the website" in command:
        return jsonify({"response": "Opening the official website..."})

    elif "open college details page" in command:
        return jsonify({"response": "Opening college details page..."})

    elif "close the page" in command:
        return jsonify({"response": "Closing the page."})

    elif "go to home page" in command:
        return jsonify({"response": "Redirecting to home page."})

    elif "show all colleges" in command:
        return get_college_names()

    elif "show arts and science colleges" in command:
        return get_college_by_type("Arts & Science")

    elif "show government colleges" in command:
        return get_college_by_type("Government")

    elif "show engineering colleges" in command:
        return get_college_by_type("Engineering")

    # 3. College-Specific Queries
    elif "college name" in command:
        return jsonify({"response": "The name of the college is XYZ College."})

    elif "type of college" in command or "is it government" in command:
        return jsonify({"response": "This is a Government College."})

    elif "courses offered" in command:
        return jsonify({"response": "This college offers B.Sc, B.Com, B.A and M.Sc."})

    elif "fee structure" in command:
        return jsonify({"response": "The average fee is ₹25,000 per year."})

    elif "b.sc in computer science" in command:
        return jsonify({"response": "Yes, B.Sc Computer Science is available."})

    elif "website" in command:
        return jsonify({"response": "Visit: https://www.xyzcollege.ac.in"})

    elif "principal" in command:
        return jsonify({"response": "The principal is Dr. A. Kumar."})

    elif "hostel" in command:
        return jsonify({"response": "Yes, hostel facility is available."})

    elif "scholarship" in command:
        return jsonify({"response": "Yes, scholarships are available for eligible students."})

    elif "placement" in command:
        return jsonify({"response": "Yes, placement training is provided."})

    elif "nss" in command or "ncc" in command:
        return jsonify({"response": "Yes, NSS and NCC units are active."})

    elif "transportation" in command:
        return jsonify({"response": "Yes, college buses are available."})

    # 4. Data Entry Commands
    elif "add a new college" in command:
        return jsonify({"response": "Please provide the details to add the new college."})

    elif "insert college details" in command:
        return jsonify({"response": "Insert function not implemented yet."})

    elif "update the website" in command:
        return jsonify({"response": "Updating college website..."})

    elif "update fees" in command:
        return jsonify({"response": "Updating fee structure..."})

    elif "delete" in command:
        return jsonify({"response": "College record deleted."})

    elif "add a new course" in command:
        return jsonify({"response": "Adding new course to college."})

    elif "remove a course" in command:
        return jsonify({"response": "Removing course from college."})

    elif "edit the principal" in command:
        return jsonify({"response": "Updating principal's name..."})

    elif "change the type" in command:
        return jsonify({"response": "College type updated."})

    # 5. Search & Display Commands
    elif "search college by name" in command:
        return jsonify({"response": "Please provide the name to search."})

    elif "search by course" in command:
        return jsonify({"response": "Please provide the course name."})

    elif "find colleges with hostel" in command:
        return jsonify({"response": "Listing all colleges with hostel..."})

    elif "show all colleges offering b.com" in command:
        return jsonify({"response": "These colleges offer B.Com: XYZ, ABC..."})

    elif "colleges with placements" in command:
        return jsonify({"response": "Here are the colleges with placement support..."})

    elif "kerala university" in command:
        return jsonify({"response": "Here are the colleges affiliated to Kerala University..."})

    # 6. Information Summary Commands
    elif "summary" in command or "overview" in command or "college highlights" in command:
        return jsonify({"response": "XYZ College is known for its strong faculty and placements..."})

    elif "facilities" in command or "features" in command:
        return jsonify({"response": "Library, Computer Lab, Hostel, Sports, Wifi, and Canteen."})

    # 7. Voice/Text Handling Commands
    elif "speak" in command or "voice output" in command or "text-to-speech" in command:
        return jsonify({"response": "Voice output enabled."})

    elif "don’t speak" in command or "disable speech" in command:
        return jsonify({"response": "Speech disabled. I will show only text now."})

    # Default Response
    else:
        return jsonify({"response": "Sorry, I didn’t understand that. Please try again."})

# Example helper function
def get_college_names():
    conn = sqlite3.connect('campusmate.db')
    c = conn.cursor()
    c.execute("SELECT name FROM colleges")
    colleges = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify({"response": "Here are all the colleges:", "colleges": colleges})

def get_college_by_type(college_type):
    conn = sqlite3.connect('campusmate.db')
    c = conn.cursor()
    c.execute("SELECT name FROM colleges WHERE type=?", (college_type,))
    colleges = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify({"response": f"{college_type} Colleges:", "colleges": colleges})

if __name__ == '__main__':
    app.run(debug=True)
