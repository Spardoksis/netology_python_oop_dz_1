class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in self.courses_in_progress
            and course in lector.courses_attached and
                grade >= 0 and grade <= 10):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        if len(self.grades) == 0:
            return 0
        points = 0
        for course in self.grades:
            points += self.average_per_course(course)
        return points / len(self.grades)

    def average_per_course(self, course):
        if course not in self.grades:
            return 0
        points = 0
        for grade in self.grades[course]:
            points += grade
        return points / len(self.grades[course])

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за "
            f"домашние задания: {self.average()}\n"
            f"Курсы в процессе обучения: "
            f"{', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: "
            f"{', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average() < other.average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return other < self

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return not (self < other) and not (other < self)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        if len(self.grades) == 0:
            return 0
        points = 0
        for course in self.grades:
            points += self.average_per_course(course)
        return points / len(self.grades)

    def average_per_course(self, course):
        if course not in self.grades:
            return 0
        pointers = 0
        for grade in self.grades[course]:
            pointers += grade
        return pointers / len(self.grades[course])

    def __str__(self):
        return (
            f'Имя: {self.name} \n'
            f'Фамилия: {self.surname} \n'
            f'Средняя оценка за лекции: {self.average()}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average() < other.average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return other < self

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return not (self < other) and not (other < self)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


"""
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, 
а также реализуйте две функции:
1. для подсчета средней оценки за домашние задания по всем студентам в рамках 
    конкретного курса (в качестве аргументов принимаем список 
    студентов и название курса);
2. для подсчета средней оценки за лекции всех лекторов в рамках курса 
    (в качестве аргумента принимаем список лекторов и название курса).
"""

student1 = Student('Ivan', 'Ivanov', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Maria', 'Petrova', 'female')
student2.courses_in_progress += ['Java']
student2.finished_courses += ['Git']

reviewer1 = Reviewer('Petr', 'Petrov')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Anna', 'Sidorova')
reviewer2.courses_attached += ['Java']

lecturer1 = Lecturer('Sidor', 'Sidorov')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Elena', 'Ivanova')
lecturer2.courses_attached += ['Java']


print('--Reviewers--')
print(reviewer1)
print()
print(reviewer2)
print()

print('--Students--')
reviewer1.rate_student(student1, 'Python', 10)
reviewer2.rate_student(student2, 'Java', 9)
print(student1)
print()
print(student2)
print()
is_student1_better = student1 > student2
print('Student1 is better: ', is_student1_better)
is_student2_worse = student2 < student1
print('Student2 is worse: ', is_student2_worse)
is_student1_like_student2 = student1 == student2
print('Student1 like Student2: ', is_student1_like_student2) 
print()

print('--Lecturers--')
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Java', 8)
print(lecturer1)
print()
print(lecturer2)
print()
is_lecturer1_better = lecturer1 > lecturer2
print('Lecturer1 is better: ', is_lecturer1_better)
is_lecturer2_worse = lecturer2 < lecturer1
print('Lecturer2 is worse: ', is_lecturer2_worse)
is_lecturer1_like_lecturer2 = lecturer1 == lecturer2
print('Lecturer1 like Lecturer2: ', is_lecturer1_like_lecturer2)
print()

def average_student_rating_on_course(students, course):
    pointers = 0
    students_count = 0
    for student in students:
        if course in student.grades:
            pointers += student.average_per_course(course)
            students_count += 1
    if students_count == 0:
        return 0
    return pointers / students_count


def average_lecturer_rating_on_course(lecturers, course):
    pointers = 0
    lecturers_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            pointers += lecturer.average_per_course(course)
            lecturers_count += 1
    if lecturers_count == 0:
        return 0
    return pointers / lecturers_count


print('Average student rating on course Python: ', sep='')
print(average_student_rating_on_course([student1, student2], 'Python'))
print('Average lecturer rating on course Java: ', sep='')
print(average_lecturer_rating_on_course([lecturer1, lecturer2], 'Java'))
