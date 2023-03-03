from dataclasses import dataclass, field
from functools import total_ordering


@dataclass
class Mentor:
    name: str
    surname: str
    courses_attached = []


@dataclass
@total_ordering
class Lecturer(Mentor):
    lecturer_ratings: dict = field(default_factory=dict)

    def __str__(self):
        average = self.average_rating()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}"

    def average_rating(self):
        total = sum(sum(i) for i in self.lecturer_ratings.values())
        count = sum(len(i) for i in self.lecturer_ratings.values())
        return round(total / count, 1)

    def average_rating_for_course(self, course: str):
        total = sum(self.lecturer_ratings[course])
        count = len(self.lecturer_ratings[course])
        return round(total / count, 1)

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course: str, grade: int):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

