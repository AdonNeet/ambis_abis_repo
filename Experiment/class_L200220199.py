class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    def set_grade(self,grade):
        self.grade = grade


student1 = student("dicky", 18, 100)
student2 = student("ali", 19, 90)

print(student1.name)
print(student1.age)
print(student1.get_grade())
print(student2.name)
print(student2.age)
print(student2.get_grade())
