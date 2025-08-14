#Урок 14.1. Виняток користувача
class GroupFullError(Exception):
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.record_book})"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupFullError("Cannot add more than 10 students to the group")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(s) for s in self.group)
        return f"Group {self.number}:\n{all_students}"

# Перевірка
gr = Group("PD1")

# Додавання 10 студентів
for i in range(10):
    st = Student("Male", 20+i, f"Name{i}", f"Surname{i}", f"RB{i}")
    gr.add_student(st)

print(gr)

# Спроба додати 11-го студента
try:
    extra_student = Student("Female", 21, "Extra", "Student", "RB11")
    gr.add_student(extra_student)
except GroupFullError as e:
    print(f"Error: {e}")
