from dataclasses import dataclass, field
from functools import total_ordering


@total_ordering
@dataclass
class Student:
    name: str
    surname: str
    gender: str
    finished_courses: list = field(default_factory=list)
    courses_in_progress: list = field(default_factory=list)
    grades: dict = field(default_factory=dict)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course: str, grade: int):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_ratings:
                lecturer.lecturer_ratings[course] += [grade]
            else:
                lecturer.lecturer_ratings[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = sum(sum(i) for i in self.grades.values())
        count = sum(len(i) for i in self.grades.values())
        return round(total / count, 1)

    def average_grade_for_course(self, course: str):
        total = sum(self.grades[course])
        count = len(self.grades[course])
        return round(total / count, 1)

    def __str__(self):
        average = self.average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
