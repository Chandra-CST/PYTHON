# OOPS Concepts in Python

# 1. CLASS and OBJECT
class Student:
    def __init__(self, name, marks):
        self.name = name        # attribute
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Chandra", 90)
s1.display()


print("\n----------------------\n")
