from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    attendance = db.Column(db.JSON)  # e.g., {"subject1": 90, "subject2": 85}
    ia1 = db.Column(db.Float)
    ia2 = db.Column(db.Float)
    ese = db.Column(db.Float)
    lab_attendance = db.Column(db.Float)
    assignments = db.Column(db.JSON)  # e.g., [{"assignmentNo": 1, "marks": 20}]
    practicals = db.Column(db.JSON)  # e.g., [{"practicalNo": 1, "grade": "A"}]
    email = db.Column(db.String(100))