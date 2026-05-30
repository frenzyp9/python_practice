class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def introduce(self):
        print(f"Hi! I am {self.name}, {self.age} years old with CGPA {self.cgpa}")

    def is_topper(self):
        if self.cgpa >= 9.0:
            print(self.name, "is a topper!")
        else:
            print(self.name, "is doing great!")

# Create objects
s1 = Student("Prachi", 19, 8.5)
s2 = Student("Rahul", 20, 9.2)

s1.introduce()
s2.introduce()
s1.is_topper()
s2.is_topper()