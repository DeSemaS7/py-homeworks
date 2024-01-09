class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached and (grade <= 10 and grade > 0):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def average_grade(self):
        sum = 0
        count = 0
        for course in self.grades.values():
            for grade in course:
                sum += grade
                count += 1
        if count > 0:
            result = round(sum / count, 1)
        else:
            result = 'не получил оценок'
        return result

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum = 0
        count = 0
        for course in self.grades.values():
            for grade in course:
                sum += grade
                count += 1
        if count > 0:
            result = round(sum / count, 1)
        else:
            result = 'не получил оценок'
        return result
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and (grade <= 10 and grade > 0):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


dima = Student('Di', 'Ma', 'male')
dima.add_courses('Devops')
dima.add_courses('Git')
dima.courses_in_progress += ['Python']
dima.courses_in_progress += ['JS']
petya = Student('Pe', 'Tya', 'male')
petya.courses_in_progress += ['JS']
petya.courses_in_progress += ['Python', 'Git']


prepod = Reviewer('Pre', 'Pod')
doprep = Reviewer('Dop', 'Rep')
lector = Lecturer('Lec', 'Tor')
rotcel = Lecturer('Rot', 'Cel')

prepod.courses_attached += ['Python', 'Git', 'JS']
doprep.courses_attached += ['Python', 'Git', 'JS']
lector.courses_attached += ['Python', 'Git', 'JS']
rotcel.courses_attached += ['Python', 'Git', 'JS']


dima.rate_lector(lector, 'Git', 10)
dima.rate_lector(lector, 'Python', 9)
dima.rate_lector(lector, 'JS', 8)

dima.rate_lector(rotcel, 'Git', 6)
dima.rate_lector(rotcel, 'Python', 7)
dima.rate_lector(rotcel, 'JS', 6)

petya.rate_lector(lector, 'Git', 10)
petya.rate_lector(lector, 'Python', 9)
petya.rate_lector(lector, 'JS', 8)

petya.rate_lector(rotcel, 'Git', 5)
petya.rate_lector(rotcel, 'Python', 6)
petya.rate_lector(rotcel, 'JS', 3)

prepod.rate_student(dima, 'Python', 8)
prepod.rate_student(dima, 'Git', 8)
doprep.rate_student(dima, 'Python', 6)
doprep.rate_student(dima, 'Git', 5)

prepod.rate_student(petya, 'Python', 3)
prepod.rate_student(petya, 'Git', 5)
doprep.rate_student(petya, 'Python', 3)
doprep.rate_student(petya, 'Git', 2)


def rate_students_course(students, course):
    sum = 0
    count = 0
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            for grade in student.grades[course]:
                sum += grade
                count += 1
    if count > 0:
        avg_rate = sum / count
        return avg_rate
    else:
        return 'Курс не найден или не имеет оценок'

def rate_lectors_course(lectors, course):
    sum = 0
    count = 0
    for lector in lectors:
        if isinstance(lector, Lecturer) and course in lector.grades:
            for grade in lector.grades[course]:
                sum += grade
                count += 1
    if count > 0:
        avg_rate = sum / count
        return avg_rate
    else:
        return 'Курс не найден или не имеет оценок'

def compare_students(student1, student2):
    if isinstance(student1, Student) and isinstance(student2, Student):
        if student1.average_grade > student2.average_grade:
            return f"{student1.name} {student1.surname} учится лучше, чем {student2.name} {student2.surname}"
        elif student1.average_grade < student2.average_grade:
            return f"{student2.name} {student2.surname} учится лучше, чем {student1.name} {student1.surname}"
        else:
            return "У обоих студентов одинаковая успеваемость"

def compare_lectors(lector1, lector2):
    if isinstance(lector1, Lecturer) and isinstance(lector2, Lecturer):
        if lector1.average_grade() > lector2.average_grade():
            return f"{lector1.name} {lector1.surname} учит лучше, чем {lector2.name} {lector2.surname}"
        elif lector1.average_grade() < lector2.average_grade():
            return f"{lector2.name} {lector2.surname} учит лучше, чем {lector1.name} {lector1.surname}"
        else:
            return "У обоих лекторов одинаковые оценки"

print(prepod,'\n')

print(lector,'\n')

print(dima,'\n')

print('сравнение успеваемости студентов:', compare_students(dima, petya),'\n')

print('сравнение успеваемости лекторов:', compare_lectors(lector, rotcel),'\n')

print('средний балл студентов по курсу Python:', rate_students_course([petya,dima], 'Python'),'\n')


print('средний балл лекторов по курсу Python:', rate_lectors_course([lector, rotcel], 'JS'),'\n')
#print(rate_students_course([petya,dima], 'Git'))
# print(lector.courses_attached)
#print(lector.grades)
# print(dima.grades, dima.courses_in_progress)
# print(lector.grades, lector.courses_attached)
#
#
