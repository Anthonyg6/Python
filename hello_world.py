class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


Anthony = Student('Anthony', 'A', 26)

print(Anthony.name, Anthony.grade, Anthony.age)

grade = Anthony.grade

print(grade)
