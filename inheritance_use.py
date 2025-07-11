#INHERITANCE EXAMPLE

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,marks,id):
        super().__init__(name,age)
        self.marks=marks
        self.id=id

    def display_info(self):
        return f"{self.name} is {self.age}years old, with under id no.{self.id} got {self.marks} marks."

s1 = Student("John",19,10,9383)
s2 = Student("Ale",19,15,8420)

print(s1.display_info())
print(s2.display_info())