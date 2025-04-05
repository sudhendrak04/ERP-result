from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Student
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow React to connect

# Configure database (SQLite example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# API Routes
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        "roll_no": s.roll_no,
        "name": s.name,
        "attendance": s.attendance,
        "ia1": s.ia1,
        "ia2": s.ia2,
        "ese": s.ese,
        "lab_attendance": s.lab_attendance,
        "assignments": s.assignments,
        "practicals": s.practicals,
        "email": s.email
    } for s in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student = Student(
        roll_no=data['roll_no'],
        name=data['name'],
        attendance=data['attendance'],
        ia1=data['ia1'],
        ia2=data['ia2'],
        ese=data['ese'],
        lab_attendance=data['lab_attendance'],
        assignments=data['assignments'],
        practicals=data['practicals'],
        email=data['email']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added!"})

# Add routes for update/delete as needed

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

@app.route('/send-pdf', methods=['POST'])
def send_pdf():
    data = request.json
    student_email = data['email']
    pdf_data = data['pdf']  # PDF content (base64 or bytes)

    # Configure email
    msg = MIMEMultipart()
    msg['Subject'] = 'Your Result'
    msg['From'] = os.getenv('SMTP_EMAIL')
    msg['To'] = student_email

    # Attach PDF
    pdf = MIMEApplication(pdf_data, _subtype="pdf")
    pdf.add_header('Content-Disposition', 'attachment', filename='result.pdf')
    msg.attach(pdf)

    # Send email
    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
        server.starttls()
        server.login(os.getenv('SMTP_EMAIL'), os.getenv('SMTP_PASSWORD'))
        server.sendmail(msg['From'], msg['To'], msg.as_string())

    return jsonify({"message": "Email sent!"})