
print("Welcome to Python Academy!")
name = input("What is your name? ")
obtain_marks = list(map(int,input("What is your obtain marks? ").split()))

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.total_marks=400

    def calculate_total_marks(self):
        return sum(self.marks)


    def calculate_percentage(self):
        return (self.calculate_total_marks()/self.total_marks)*100

    def pass_fail_check(self):
        if self.calculate_percentage() >= 30:
            return ("Congratulations! You Pass.")
        else:
            return ("You fail the exam because your percentage is less than 30%.")

    def display_marks_report(self):
        return (f"Name of the student: {self.name}\nThe total marks of {self.name} is {self.calculate_total_marks()}\nThe Percentage of {self.name} is {self.calculate_percentage()}\n{self.pass_fail_check()}")



s1 = Student(name,obtain_marks)
print(s1.display_marks_report())



