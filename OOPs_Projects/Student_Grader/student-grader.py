class Student:
    def __init__(self, s_id, name):
        self.s_id = s_id
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def calculate_average(self):
        marks = []
        for value in self.marks.values():
            marks.append(value)
        total = sum(marks)
        avg = total / len(marks)
        return avg


    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            return 'A+'
        elif avg >= 60:
            return 'A'
        elif avg >= 50:
            return 'B'
        elif avg >= 40:
            return 'C'
        else:
            return 'F'

    def view_report(self, s_id):
        return f"Student ID: {s_id}, Student Name: {self.name}\nSubjects: {self.marks}\nAverage: {self.calculate_average()}\nGrade: {self.get_grade()}"

    def show_student_info(self):
        print(f"Student ID: {self.s_id}, Name: {self.name}")
        print(f"Subjects: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        print(f"Grade: {self.get_grade()}")

class GraderSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, s_id, name):
        if s_id not in self.students:
            self.students[s_id] = Student(s_id, name)
            # print(f"New student added.")
        else:
            print(f"Student ID: {s_id} already exists.")

    def add_mark(self, s_id, subject, mark):
        if s_id not in self.students:
            print(f"Student ID: {s_id} does not exist.")
        else:
            self.students[s_id].add_mark(subject, mark)
            # print(f"Marks: ✅")

    def calculate_average(self, s_id):
        if s_id not in self.students:
            return f"Student ID: {s_id} does not exist."
        else:
            avg = self.students[s_id].calculate_average()
            return avg

    def get_grade(self, s_id):
        if s_id not in self.students:
            return "Student ID: {s_id} does not exist."
        else:
            grade = self.students[s_id].get_grade()
            return grade

    def view_report(self, s_id):
        if s_id not in self.students:
            print(f"Student ID: {s_id} does not exist.")
        else:
            report = self.students[s_id].view_report(s_id)
            print(report)

gs = GraderSystem()

gs.add_student(101, "Sarah")
gs.add_student(102, "Johnathan")
gs.add_student(103, "Mosh")

gs.add_mark(101, "English", 60)
gs.add_mark(101, "Physics", 85)

gs.add_mark(102, "English", 85)
gs.add_mark(102, "Physics", 64)

gs.add_mark(103, "English", 77)
gs.add_mark(103, "Physics", 91)

gs.calculate_average(101)
gs.get_grade(101)
gs.view_report(101)

gs.calculate_average(102)
gs.get_grade(102)
gs.view_report(102)

gs.calculate_average(103)
gs.get_grade(103)
gs.view_report(103)





