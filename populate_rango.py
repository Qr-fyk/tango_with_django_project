import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
from datetime import date
import django
django.setup()
from rango.models import *
from django.contrib.auth.models import User

def populate():

    students = [
        {'username': 'Ian', 'email': 'ian@example.com', 'password': 'password123', 'YearEnrolled': 2024, 'CurrentYearStudent': 2},
        {'username': 'Sarah', 'email': 'sarah@example.com', 'password': 'password123', 'YearEnrolled': 2023, 'CurrentYearStudent': 3},
        {'username': 'James', 'email': 'james@example.com', 'password': 'password123', 'YearEnrolled': 2022, 'CurrentYearStudent': 4},
        {'username': 'Emily', 'email': 'emily@example.com', 'password': 'password123', 'YearEnrolled': 2024, 'CurrentYearStudent': 2},
        {'username': 'Micheal', 'email': 'michael@example.com', 'password': 'password123', 'YearEnrolled': 2021, 'CurrentYearStudent': 5},
        {'username': 'Sophie', 'email': 'sophie@example.com', 'password': 'password123', 'YearEnrolled': 2023, 'CurrentYearStudent': 3},
        {'username': 'Daniel', 'email': 'daniel@example.com', 'password': 'password123', 'YearEnrolled': 2022, 'CurrentYearStudent': 4},
        {'username': 'Olivia', 'email': 'olivia@example.com', 'password': 'password123', 'YearEnrolled': 2024, 'CurrentYearStudent': 2},
        {'username': 'Ethan', 'email': 'ethan@example.com', 'password': 'password123', 'YearEnrolled': 2023, 'CurrentYearStudent': 3},
        {'username': 'Charlotte', 'email': 'charlotte@example.com', 'password': 'password123', 'YearEnrolled': 2021, 'CurrentYearStudent': 5}
    ]

    Courses = [
        {"CourseID": "EDUC3078P", "CourseName": "Educational Elective 3"},
        {"CourseID": "EDUC4084P", "CourseName": "Educational Elective 4"},
        {"CourseID": "T2G-SCI", "CourseName": "Transition to Glasgow: Sciences"},
        {"CourseID": "BIOL4A", "CourseName": "Advanced Biology A"},
        {"CourseID": "BIOL4B", "CourseName": "Advanced Biology B"},
        {"CourseID": "COMP1001", "CourseName": "Introduction to Computing Science"},
        {"CourseID": "MATH1001", "CourseName": "Calculus 1"},
        {"CourseID": "PHYS1001", "CourseName": "Physics 1"},
        {"CourseID": "CHEM1001", "CourseName": "Fundamentals of Chemistry"},
        {"CourseID": "PSYC1001", "CourseName": "Introduction to Psychology"}
    ]

    Enrolls = [
        {"username": "Ian", "CourseID": "BIOL4A"},
        {"username": "Ian", "CourseID": "MATH1001"},
        {"username": "Sarah", "CourseID": "COMP1001"},
        {"username": "Sarah", "CourseID": "PSYC1001"},
        {"username": "James", "CourseID": "T2G-SCI"},
        {"username": "James", "CourseID": "PHYS1001"},
        {"username": "Emily", "CourseID": "EDUC3078P"},
        {"username": "Emily", "CourseID": "EDUC4084P"},
        {"username": "Micheal", "CourseID": "CHEM1001"},
        {"username": "Micheal", "CourseID": "MATH1001"},
        {"username": "Sophie", "CourseID": "PSYC1001"},
        {"username": "Sophie", "CourseID": "BIOL4B"},
        {"username": "Daniel", "CourseID": "PHYS1001"},
        {"username": "Daniel", "CourseID": "BIOL4A"},
        {"username": "Olivia", "CourseID": "EDUC3078P"},
        {"username": "Olivia", "CourseID": "T2G-SCI"},
        {"username": "Ethan", "CourseID": "BIOL4B"},
        {"username": "Ethan", "CourseID": "CHEM1001"},
        {"username": "Charlotte", "CourseID": "COMP1001"},
        {"username": "Charlotte", "CourseID": "MATH1001"}
    ]

    Notes = [
        {"ID": 1, "username": "Ian", "CourseID": "BIOL4A", "Topics": "Evolution and Gene Pool", "file": "Documents/test1.docx"},
        {"ID": 2, "username": "Sarah", "CourseID": "COMP1001", "Topics": "Fundamentals of Python Programming", "file": "Documents/test2.docx"},
        {"ID": 3, "username": "James", "CourseID": "MATH1001", "Topics": "Limits and Differentiation", "file": "Documents/test3.docx"},
        {"ID": 4, "username": "Emily", "CourseID": "PHYS1001", "Topics": "Newton’s Laws of Motion", "file": "Documents/test4.docx"}
    ]

    edited_notes = [
        {"CourseID": "BIOL4A", "ID": 1, "File": "Edited_Note/etest1.docx", "username": "Charlotte"},
        {"CourseID": "COMP1001", "ID": 2, "File": "Edited_Note/etest2.docx", "username": "James"},
        {"CourseID": "MATH1001", "ID": 3, "File": "Edited_Note/etest3.docx", "username": "Sarah"},
        {"CourseID": "PHYS1001", "ID": 4, "File": "Edited_Note/etest4.docx", "username": "Sophie"}
    ]
    """
    for student_data in students:
        add_student(
            username=student_data['username'],
            email=student_data['email'],
            password=student_data['password'],
            YearEnrolled=student_data['YearEnrolled'],
            CurrentYearStudent=student_data['CurrentYearStudent']
        )
    print("added students")
    for course in Courses:
        courseID = course.get("CourseID")
        CourseName = course.get("CourseName")

        add_course(courseID, CourseName)

    for enroll in Enrolls:
        username = enroll.get("username")
        CourseID = enroll.get("CourseID")

        add_enroll(username, CourseID)

    for note in Notes:
        Id = note.get("ID")
        username = note.get("username")
        CourseID = note.get("CourseID")
        Topic = note.get("Topics")
        file = note.get("file")

        add_note(Id, username, CourseID, Topic, file)
    """

    for edits in edited_notes:
        NoteID = edits['ID']
        CourseID = edits['CourseID']
        file = edits['File']
        username = edits['username']
        add_edit(NoteID, CourseID, file, username)

def add_student(username, email, password, YearEnrolled, CurrentYearStudent):
    # Create or get the User object
    
    user,created = User.objects.get_or_create(
        username=username,
        email = email,
    )
    
    user.set_password(password)  # Set the password
    user.save()

    # Create or get the Students object linked to the User
    student, created = Students.objects.get_or_create(
        user=user,
        defaults={
            'YearEnrolled': YearEnrolled,
            'CurrentYearStudent': CurrentYearStudent,
        }
    )
    
    student.save()
    return student

def add_course(courseID, CourseName):
    c = Courses.objects.get_or_create(CourseID=courseID, CourseName=CourseName)[0]
    c.save()
    return c

def add_enroll(username, CourseID):
    
    print(username)
    student = Students.objects.get(user__username=username)
    course = Courses.objects.get(CourseID=CourseID)
    e = Enrolls.objects.get_or_create(user_id=student.id, CourseID=course)[0]
    e.save()
    return e

def add_note(Id, username, CourseID, Topic, file):
    student = Students.objects.get(user__username=username)
    course = Courses.objects.get(CourseID=CourseID)
    if Id is not None:
        n = Note.objects.update_or_create(
            user=student.id,  # Lookup field
            CourseID=course,  # Lookup field
            defaults={
                'Topics': Topic,
                'file': file,
                'DateUploaded': date.today().isoformat()
            })[0]
    else:
        n = Note.objects.get_or_create(UserID=student.id, CourseID=course, Topics=Topic, file=file, DateUploaded=date.today().isoformat())[0]
    n.save()
    return n

def add_edit(NoteID, CourseID, file, username):
    note = Note.objects.get(NoteID=NoteID)
    course = Courses.objects.get(CourseID=CourseID)
    sid = Students.objects.get(user__username=username)
    student = Students.objects.get(id = sid.id)
    print(course.CourseName)

    e = EditedNotes.objects.get_or_create(
        user=student,
        CourseID=course,
        NoteID=note,
        defaults={
            'file': file,
            'DateUploaded': date.today().isoformat()
        }
    )[0]
    e.save()
    return e


if __name__ == '__main__':
    print("populating rango")
    populate()