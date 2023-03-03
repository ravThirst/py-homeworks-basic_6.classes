from _mentors import Lecturer, Reviewer
from _students import Student


def average_students_grade_for_course(students: [], course: str):
    return round(sum(i.average_grade_for_course(course) for i in students) / len(students), 1)


def average_lecturer_rating_for_course(lecturers: [], course: str):
    return round(sum(i.average_rating_for_course(course) for i in lecturers) / len(lecturers), 1)


stud1 = Student('Iven', 'Krisko', 'Male')
stud2 = Student('Masha', 'Potova', 'Female')
lec1 = Lecturer('Van', 'Erasdo')
lec2 = Lecturer('Kostya', 'Rasoner')
rev1 = Reviewer('Motero', 'Wonka')
rev2 = Reviewer('Loquad', 'Aoka')

stud1.courses_in_progress.append('Python')
stud2.courses_in_progress.append('Python')
rev1.courses_attached.append('Python')
rev2.courses_attached.append('Python')
lec1.courses_attached.append('Python')
lec2.courses_attached.append('Python')

rev1.rate_hw(stud1, 'Python', 8)
rev2.rate_hw(stud2, 'Python', 7)
stud1.rate_lecturer(lec1, 'Python', 9)
stud2.rate_lecturer(lec2, 'Python', 8)

print(stud1, stud2, lec1, lec2, rev1, rev2, sep='\n\n')

print(stud1 > stud2)
print(stud1 <= stud2)
print(stud1 == stud2)
print(stud1 != stud2)
print(lec1 < lec2)
print(lec1 <= lec2)
print(lec1 == lec2)
print(lec1 != lec2)

print(lec1.average_rating_for_course('Python'))
print(stud1.average_grade_for_course('Python'))
print(average_students_grade_for_course([stud1, stud2], 'Python'))
print(average_lecturer_rating_for_course([lec1, lec2], 'Python'))
